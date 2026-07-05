#!/usr/bin/env python3
"""Generate RestAPI/mappings/endpoint_checklist.md for PUT + parameterized GET endpoints."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

REST = Path(__file__).resolve().parent.parent
BUNDLED = REST / "FXR90-rest-api.yaml"
OUT = REST / "mappings" / "endpoint_checklist.md"

COMPLEX_OPS = {
    "setImpinjGen2X",
    "setBleConfig",
    "setImportCloudConfig",
    "setMode",
    "startInventory",
    "setUpdateCertificate",
    "setConfig",
    "updateNetwork",
    "setReqToUserApp",
    "setCableLossCompensation",
    "stopInventory",
    "getSupportedStandardList",
}
MODERATE_OPS = {
    "setInstallUserApp",
    "setLogs",
    "setOS",
    "setAppLed",
    "setAutostartUserApp",
    "setStartUserApp",
    "setStopUserApp",
    "setUninstallUserApp",
    "setRefreshCertificate",
    "updatePassword",
}


def tier(operation_id: str) -> str:
    if operation_id in COMPLEX_OPS:
        return "complex"
    if operation_id in MODERATE_OPS:
        return "moderate"
    return "simple"


def resolve_schema(schemas: dict, node, seen: set[str] | None = None):
    if seen is None:
        seen = set()
    if not isinstance(node, dict):
        return node
    ref = node.get("$ref")
    if ref:
        name = ref.rsplit("/", 1)[-1]
        if name in seen:
            return {"type": "object"}
        return resolve_schema(schemas, schemas.get(name, {}), seen | {name})
    out = dict(node)
    if "properties" in out:
        out["properties"] = {
            k: resolve_schema(schemas, v, seen) for k, v in out["properties"].items()
        }
    if "items" in out:
        out["items"] = resolve_schema(schemas, out["items"], seen)
    return out


def schema_field_summary(schemas: dict, schema_name: str | None) -> tuple[str, str, str]:
    if not schema_name or schema_name not in schemas:
        return "—", "—", "—"
    resolved = resolve_schema(schemas, schemas[schema_name])
    props = resolved.get("properties") or {}
    required = set(resolved.get("required") or [])
    req = ", ".join(f"`{k}`" for k in props if k in required) or "*(none at top level)*"
    opt = ", ".join(f"`{k}`" for k in props if k not in required) or "*(none at top level)*"
    nested = []
    for key, val in props.items():
        if isinstance(val, dict) and (
            val.get("type") == "object"
            or "properties" in val
            or "$ref" in val
            or val.get("type") == "array"
        ):
            nested.append(f"`{key}`")
    nested_note = ", ".join(nested) if nested else "—"
    return req, opt, nested_note


def collect_params(path: str, op: dict, path_item: dict) -> list[tuple[str, str, bool]]:
    params: list[tuple[str, str, bool]] = []
    seen: set[str] = set()
    for source in (path_item.get("parameters") or [], op.get("parameters") or []):
        for param in source:
            if not isinstance(param, dict):
                continue
            name = param.get("name")
            if not name or name in seen:
                continue
            seen.add(name)
            params.append((name, param.get("in", "?"), bool(param.get("required"))))
    for name in re.findall(r"\{([^}]+)\}", path):
        if name not in seen:
            params.append((name, "path", True))
    return params


def body_schema_name(op: dict) -> tuple[str | None, bool]:
    rb = op.get("requestBody")
    if not rb:
        return None, False
    content = (rb.get("content") or {}).get("application/json") or {}
    schema = content.get("schema") or {}
    ref = schema.get("$ref")
    name = ref.rsplit("/", 1)[-1] if ref else None
    return name, bool(rb.get("required", False))


def fmt_params(params: list[tuple[str, str, bool]]) -> str:
    if not params:
        return "—"
    parts = []
    for name, loc, required in params:
        flag = "required" if required else "optional"
        parts.append(f"`{name}` ({loc}, {flag})")
    return ", ".join(parts)


def main() -> None:
    doc = yaml.safe_load(BUNDLED.read_text(encoding="utf-8"))
    schemas = doc.get("components", {}).get("schemas", {})
    rows = []

    for path, path_item in sorted(doc.get("paths", {}).items()):
        for method in ("get", "put"):
            if method not in path_item:
                continue
            op = path_item[method]
            params = collect_params(path, op, path_item)
            if method == "get" and not params:
                continue

            operation_id = op.get("operationId", "")
            schema_name, body_required_flag = body_schema_name(op)
            req_fields, opt_fields, nested = schema_field_summary(schemas, schema_name)
            has_body = schema_name is not None or bool(op.get("requestBody"))
            body_cell = "No body"
            if has_body:
                label = "Required" if body_required_flag else "Optional"
                body_cell = f"{label} JSON (`{schema_name}`)" if schema_name else f"{label} JSON"

            rows.append(
                {
                    "method": method.upper(),
                    "path": path,
                    "operation_id": operation_id,
                    "summary": op.get("summary", ""),
                    "tier": tier(operation_id),
                    "read_schema": "Yes" if operation_id in COMPLEX_OPS else "No",
                    "params": fmt_params(params),
                    "body": body_cell,
                    "required_fields": req_fields,
                    "optional_fields": opt_fields,
                    "nested_objects": nested,
                }
            )

    lines = [
        "# FXR90 REST Endpoint Checklist (33 commands)",
        "",
        "Quick reference for **32 PUT** endpoints plus **1 GET with a parameter**.",
        "Generated from `FXR90-rest-api.yaml`.",
        "",
        "**Auth:** all endpoints below require **Bearer token** unless noted otherwise.",
        "",
        "## Legend",
        "",
        "| Column | Meaning |",
        "|---|---|",
        "| **Tier** | `simple` = small/trivial body · `moderate` = few fields or path param · `complex` = large/nested schema or long workflow docs |",
        "| **Read schema first** | Open the Swagger request schema and examples before calling |",
        "| **Required fields** | Top-level JSON fields marked required in OpenAPI (nested objects may contain additional required fields) |",
        "",
        "## Summary",
        "",
        f"| Tier | Count |",
        f"|---|---:|",
        f"| Simple | {sum(1 for r in rows if r['tier'] == 'simple')} |",
        f"| Moderate | {sum(1 for r in rows if r['tier'] == 'moderate')} |",
        f"| Complex | {sum(1 for r in rows if r['tier'] == 'complex')} |",
        f"| **Total** | **{len(rows)}** |",
        "",
        "## Full checklist",
        "",
        "| # | Method | Path | Operation ID | Tier | Read schema first | Params | Body | Required fields (top-level) | Optional fields (top-level) | Nested objects |",
        "|---:|---|---|---|---|---|---|---|---|---|---|",
    ]

    for index, row in enumerate(rows, 1):
        lines.append(
            f"| {index} | {row['method']} | `{row['path']}` | `{row['operation_id']}` | "
            f"{row['tier']} | {row['read_schema']} | {row['params']} | {row['body']} | "
            f"{row['required_fields']} | {row['optional_fields']} | {row['nested_objects']} |"
        )

    lines.extend(
        [
            "",
            "## Complex endpoints — read schema first",
            "",
            "These 12 endpoints have the largest schemas or multi-step behavior. "
            "Always expand the request model in Swagger UI before calling:",
            "",
        ]
    )
    for row in rows:
        if row["read_schema"] == "Yes":
            lines.append(
                f"- **{row['method']} `{row['path']}`** (`{row['operation_id']}`) — {row['summary']}"
            )

    lines.extend(
        [
            "",
            "## Simple endpoints — quick calls",
            "",
            "Safe starting points for integration testing (still send valid JSON where a body exists):",
            "",
        ]
    )
    for row in rows:
        if row["tier"] == "simple":
            lines.append(
                f"- **{row['method']} `{row['path']}`** (`{row['operation_id']}`) — {row['summary']}"
            )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(rows)} endpoints)")


if __name__ == "__main__":
    main()
