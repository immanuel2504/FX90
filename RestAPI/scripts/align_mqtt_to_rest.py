#!/usr/bin/env python3
"""Align MQTT split schemas to REST openAPISpec2.yaml field-for-field.

Updates the payload schemas referenced by schemas/commands and schemas/response
(including schemas/references/* targets). For each mapped REST operation:

- Replace payload property shapes with REST (properties, types, enums, descriptions)
- Sync object-level ``required`` lists
- Remove MQTT-only properties not present in REST
- Add REST-only properties

Usage:
    python RestAPI/scripts/align_mqtt_to_rest.py --dry-run
    python RestAPI/scripts/align_mqtt_to_rest.py --apply
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any

import yaml

import compare_rest_mqtt_schemas as cmp

ROOT = cmp.ROOT
CMD_DIR = ROOT / "schemas" / "commands"
RESP_DIR = ROOT / "schemas" / "response"

# Endpoints handled manually (inline replacement) or skipped intentionally.
MANUAL = {
    "PUT /cloud/updatePassword",
    "PUT /cloud/mode",
    "PUT /cloud/pass-through",
    "DELETE /cloud/certificates/{certname}",
    "PUT /cloud/certificates/{certname}",
    "PUT /cloud/apps/{appname}/start",
    "PUT /cloud/apps/{appname}/stop",
    "PUT /cloud/apps/{appname}/autostart",
    "PUT /cloud/apps/{appname}/pass-through",
    "PUT /cloud/apps/{appname}/uninstall",
}


def load_structured(path: Path) -> Any:
    with path.open(encoding="utf-8-sig") as f:
        if path.suffix.lower() in (".yaml", ".yml"):
            return yaml.safe_load(f)
        return json.load(f)


def dump_structured(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as f:
        if path.suffix.lower() in (".yaml", ".yml"):
            yaml.safe_dump(
                data,
                f,
                sort_keys=False,
                allow_unicode=True,
                default_flow_style=False,
                width=4096,
            )
        else:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")


def strip_schema(node: Any) -> Any:
    """Remove OpenAPI-only keys; keep JSON Schema shape."""
    if isinstance(node, list):
        return [strip_schema(x) for x in node]
    if not isinstance(node, dict):
        return node
    skip = {
        "example",
        "examples",
        "x-examples",
        "x-stoplight",
        "x-internal",
        "nullable",
        "discriminator",
        "xml",
        "deprecated",
        "readOnly",
        "writeOnly",
    }
    out: dict[str, Any] = {}
    for k, v in node.items():
        if k in skip:
            continue
        if k == "properties" and isinstance(v, dict):
            out[k] = {pk: strip_schema(pv) for pk, pv in v.items()}
        elif k in ("items", "additionalProperties") and isinstance(v, dict):
            out[k] = strip_schema(v)
        elif k in ("oneOf", "anyOf", "allOf") and isinstance(v, list):
            out[k] = [strip_schema(x) for x in v]
        else:
            out[k] = strip_schema(v)
    return out


def merge_rest_onto_mqtt(mqtt: dict[str, Any], rest: dict[str, Any]) -> dict[str, Any]:
    """Align mqtt schema node to rest schema node."""
    if not isinstance(rest, dict):
        return mqtt
    if not isinstance(mqtt, dict):
        mqtt = {}

    rest = strip_schema(rest)
    merged = copy.deepcopy(mqtt)

    for key in ("type", "description", "title", "format", "minimum", "maximum", "minItems", "maxItems"):
        if key in rest:
            merged[key] = copy.deepcopy(rest[key])

    if "enum" in rest:
        merged["enum"] = copy.deepcopy(rest["enum"])

    if "required" in rest:
        merged["required"] = copy.deepcopy(rest["required"])
    elif "properties" in rest and "required" in merged:
        # REST omits empty required — drop if REST has no required list
        if not rest.get("required"):
            merged.pop("required", None)

    if "properties" in rest:
        mqtt_props = merged.get("properties") or {}
        rest_props = rest["properties"]
        new_props: dict[str, Any] = {}
        for name, rsub in rest_props.items():
            msub = mqtt_props.get(name, {})
            if isinstance(rsub, dict) and (
                rsub.get("type") == "object"
                or rsub.get("properties")
                or rsub.get("oneOf")
                or rsub.get("allOf")
                or rsub.get("anyOf")
            ):
                new_props[name] = merge_rest_onto_mqtt(
                    msub if isinstance(msub, dict) else {},
                    rsub,
                )
            elif isinstance(rsub, dict) and rsub.get("type") == "array" and isinstance(rsub.get("items"), dict):
                mitems = msub.get("items", {}) if isinstance(msub, dict) else {}
                arr = copy.deepcopy(rsub)
                arr["items"] = merge_rest_onto_mqtt(
                    mitems if isinstance(mitems, dict) else {},
                    rsub["items"],
                )
                new_props[name] = arr
            else:
                new_props[name] = copy.deepcopy(strip_schema(rsub))
        merged["properties"] = new_props
    elif "properties" in merged and "properties" not in rest:
        merged.pop("properties", None)

    if "items" in rest and isinstance(rest["items"], dict):
        merged["items"] = merge_rest_onto_mqtt(
            (merged.get("items") or {}) if isinstance(merged.get("items"), dict) else {},
            rest["items"],
        )

    for combiner in ("oneOf", "anyOf", "allOf"):
        if combiner in rest:
            merged[combiner] = copy.deepcopy(strip_schema(rest[combiner]))

    # Drop MQTT-only keys at this level when rest is object-shaped
    if "properties" in rest:
        allowed = set(rest.keys()) | {"properties", "required", "type", "description", "title", "enum"}
        for k in list(merged.keys()):
            if k not in allowed and k.startswith(("x-", "example")):
                merged.pop(k, None)

    return merged


class PayloadEditor:
    def __init__(self) -> None:
        self.dirty: dict[Path, Any] = {}
        self.changes: list[str] = []

    def _root(self, path: Path) -> Any:
        if path not in self.dirty:
            self.dirty[path] = load_structured(path)
        return self.dirty[path]

    def resolve_ref_target(self, ref: str, base: Path) -> tuple[Path, dict[str, Any]] | None:
        if ref.startswith("#/"):
            return None
        target = (base.parent / ref).resolve()
        if not target.is_file():
            return None
        return target, self._root(target)

    def find_payload_roots(self, split_file: Path, is_response: bool) -> list[tuple[Path, list[str]]]:
        """Return (file, path_parts) to payload schema nodes to update."""
        data = self._root(split_file)
        payload = (data.get("properties") or {}).get("payload")
        if payload is None:
            return []

        roots: list[tuple[Path, list[str]]] = []

        def walk(node: Any, base: Path, parts: list[str]) -> None:
            if isinstance(node, dict) and "$ref" in node:
                resolved = self.resolve_ref_target(node["$ref"], base)
                if resolved:
                    tf, _ = resolved
                    walk(self._root(tf), tf, [])
                return
            if isinstance(node, dict) and "oneOf" in node:
                for i, variant in enumerate(node["oneOf"]):
                    if isinstance(variant, dict):
                        ref = variant.get("$ref", "")
                        if isinstance(ref, str) and "error" in ref.lower():
                            continue
                        if "$ref" in variant:
                            resolved = self.resolve_ref_target(variant["$ref"], split_file)
                            if resolved:
                                tf, tnode = resolved
                                if is_response and isinstance(tnode, dict) and tnode.get("title", "").lower() == "failure":
                                    continue
                                roots.append((tf, []))
                        else:
                            roots.append((split_file, parts + ["oneOf", str(i)]))
                return
            if isinstance(node, dict) and not parts:
                roots.append((split_file, []))

        if isinstance(payload, dict):
            if "$ref" in payload:
                resolved = self.resolve_ref_target(payload["$ref"], split_file)
                if resolved:
                    roots.append((resolved[0], []))
            elif "oneOf" in payload:
                for variant in payload["oneOf"]:
                    if isinstance(variant, dict) and "$ref" in variant:
                        ref = variant["$ref"]
                        if "error" in ref.lower():
                            continue
                        resolved = self.resolve_ref_target(ref, split_file)
                        if resolved:
                            roots.append((resolved[0], []))
            else:
                roots.append((split_file, []))
        return roots

    def set_node(self, path: Path, parts: list[str], value: dict[str, Any]) -> None:
        data = self._root(path)
        if not parts:
            if isinstance(data, dict):
                # Preserve title/x-stoplight/examples on yaml reference files
                keep = {k: data[k] for k in data if k.startswith("x-") or k in ("examples", "example")}
                data.clear()
                data.update(value)
                data.update(keep)
            return
        # nested oneOf index path not used currently
        raise NotImplementedError(parts)

    def align_endpoint(self, endpoint: str, rest_schema: dict[str, Any], split_file: Path, is_response: bool) -> None:
        if not rest_schema:
            return
        roots = self.find_payload_roots(split_file, is_response)
        if not roots:
            return
        for file_path, parts in roots:
            before = json.dumps(self._root(file_path), sort_keys=True, default=str)
            current = self._root(file_path)
            if parts:
                continue
            aligned = merge_rest_onto_mqtt(current if isinstance(current, dict) else {}, rest_schema)
            self.set_node(file_path, parts, aligned)
            after = json.dumps(self._root(file_path), sort_keys=True, default=str)
            if before != after:
                self.changes.append(f"{endpoint} -> {file_path.relative_to(ROOT)}")

    def write_all(self) -> None:
        for path, data in self.dirty.items():
            dump_structured(path, data)


def inline_get_mode_response(editor: PayloadEditor) -> None:
    """Replace get_mode success payload with REST GET /cloud/mode inline schema."""
    spec = cmp.load_yaml(cmp.REST_SPEC)
    paths = spec.get("paths") or {}
    op = paths["/cloud/mode"]["get"]
    rest_schema = cmp.resolve_schema(
        op["responses"]["200"]["content"]["application/json"]["schema"],
        spec,
    )
    path = RESP_DIR / "control" / "get_mode_response.json"
    data = editor._root(path)
    success = strip_schema(rest_schema)
    success["title"] = "success"
    payload = data["properties"]["payload"]
    new_one_of = []
    for variant in payload["oneOf"]:
        ref = variant.get("$ref", "")
        if isinstance(ref, str) and "error" in ref.lower():
            new_one_of.append(variant)
        else:
            new_one_of.append(success)
    payload["oneOf"] = new_one_of
    editor.changes.append("GET /cloud/mode -> inline REST schema in get_mode_response.json")
    editor.dirty[path] = data


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    spec = cmp.load_yaml(cmp.REST_SPEC)
    mapping = json.loads(cmp.MAP_JSON.read_text(encoding="utf-8"))
    ops = cmp.build_rest_operations(spec, mapping)

    editor = PayloadEditor()

    for op in ops:
        endpoint = f"{op['method']} {op['path']}"
        if endpoint in MANUAL:
            continue
        mqtt_command = op.get("mqtt_command") or ""
        if not mqtt_command:
            continue

        if op["method"] in ("PUT", "POST", "PATCH", "DELETE"):
            rest_schema = cmp.extract_rest_request_schema(op["operation"], spec)
            split = cmp.find_mqtt_file(CMD_DIR, mqtt_command)
            if split:
                editor.align_endpoint(endpoint, rest_schema, split, is_response=False)
        else:
            rest_schema = cmp.extract_rest_response_schema(op["operation"], spec)
            split = cmp.find_mqtt_file(RESP_DIR, mqtt_command, "_response")
            if split:
                editor.align_endpoint(endpoint, rest_schema, split, is_response=True)

    inline_get_mode_response(editor)

    print(f"Aligned endpoints: {len(editor.changes)}")
    for c in editor.changes:
        print(f"  {c}")
    print(f"Files touched: {len(editor.dirty)}")

    if args.apply and not args.dry_run:
        editor.write_all()
        print("\nAPPLIED.")
    else:
        print("\nDRY RUN — re-run with --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
