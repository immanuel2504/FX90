#!/usr/bin/env python3
"""Sync REST (RestDeveloperfile.yaml) descriptions + required flags into MQTT schemas.

Non-destructive: only updates ``description`` and object ``required`` lists on
fields that already exist in MQTT, matched by field path. Never deletes, renames,
or changes enum *values* (those are handled manually after verification).

Targets the doc-build source of truth: split ``schemas/commands`` /
``schemas/response`` files and the ``schemas/references/*`` payloads they $ref.

Usage:
    python RestAPI/scripts/sync_rest_to_mqtt.py --dry-run
    python RestAPI/scripts/sync_rest_to_mqtt.py --apply
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

import compare_rest_mqtt_schemas as cmp

ROOT = cmp.ROOT
CMD_DIR = ROOT / "schemas" / "commands"
RESP_DIR = ROOT / "schemas" / "response"

# Endpoints whose REST schema is a simplified/inline or broken view — do NOT sync.
SKIP_ENDPOINTS = {
    "GET /cloud/mode",
    "PUT /cloud/mode",
    "GET /cloud/config",
    "PUT /cloud/config",
    "GET /cloud/readerCapabilities",
    "GET /cloud/network",
    "PUT /cloud/network",
    "GET /cloud/status",
    "PUT /cloud/updatePassword",
    "GET /cloud/cableLossCompensation",
    "PUT /cloud/cableLossCompensation",
}


def load_structured(path: Path) -> Any:
    with path.open(encoding="utf-8-sig") as f:
        if path.suffix.lower() in (".yaml", ".yml"):
            return yaml.safe_load(f)
        return json.load(f)


def dump_structured(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as f:
        if path.suffix.lower() in (".yaml", ".yml"):
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False, width=4096)
        else:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")


def find_split_file(base: Path, mqtt_command: str, suffix: str = "") -> Path | None:
    stem = f"{mqtt_command}{suffix}"
    for cand in (stem, mqtt_command.replace("-", "_") + suffix):
        matches = list(base.rglob(f"{cand}.json"))
        if matches:
            return matches[0]
    return None


class Editor:
    """Edits a schema node tree spread across files via $ref, writing back per file."""

    def __init__(self) -> None:
        self.dirty: dict[Path, Any] = {}
        self.changes: list[str] = []

    def _root(self, path: Path) -> Any:
        if path not in self.dirty:
            self.dirty[path] = load_structured(path)
        return self.dirty[path]

    def resolve_ref(self, ref: str, base_file: Path) -> tuple[Path, Any] | None:
        if ref.startswith("#/"):
            return None  # local component ref not used in split MQTT files
        target = (base_file.parent / ref).resolve()
        if not target.is_file():
            return None
        return target, self._root(target)

    def sync_object(
        self,
        node: Any,
        base_file: Path,
        rest_fields: dict[str, dict[str, Any]],
        prefix: str,
        endpoint: str,
    ) -> None:
        if not isinstance(node, dict):
            return

        if "$ref" in node:
            resolved = self.resolve_ref(node["$ref"], base_file)
            if resolved:
                tf, tnode = resolved
                self.sync_object(tnode, tf, rest_fields, prefix, endpoint)
            return

        for combiner in ("oneOf", "anyOf", "allOf"):
            if combiner in node and isinstance(node[combiner], list):
                for sub in node[combiner]:
                    self.sync_object(sub, base_file, rest_fields, prefix, endpoint)

        if node.get("type") == "array" and isinstance(node.get("items"), dict):
            self.sync_object(node["items"], base_file, rest_fields, f"{prefix}[]" if prefix else "[]", endpoint)

        props = node.get("properties")
        if isinstance(props, dict):
            # Align this object's required list to REST for props present here.
            rest_required_here = []
            for name in props:
                path = f"{prefix}.{name}" if prefix else name
                rf = rest_fields.get(path)
                if rf and rf.get("required_rest"):
                    rest_required_here.append(name)
            if rest_required_here or "required" in node:
                new_req = sorted(rest_required_here)
                old_req = sorted(node.get("required", []) or [])
                if new_req != old_req:
                    node["required"] = new_req
                    self.changes.append(
                        f"{endpoint}: required@{prefix or '<root>'} {old_req} -> {new_req} [{base_file.name}]"
                    )

            for name, sub in props.items():
                path = f"{prefix}.{name}" if prefix else name
                rf = rest_fields.get(path)
                if rf and isinstance(sub, dict) and "$ref" not in sub:
                    rest_desc = rf.get("description")
                    if rest_desc:
                        old = sub.get("description")
                        if old != rest_desc:
                            sub["description"] = rest_desc
                            self.changes.append(
                                f"{endpoint}: desc@{path} [{base_file.name}]"
                            )
                self.sync_object(sub, base_file, rest_fields, path, endpoint)

    def write_all(self) -> None:
        for path, data in self.dirty.items():
            dump_structured(path, data)


def build_rest_required_flags(schema: dict[str, Any]) -> dict[str, dict[str, Any]]:
    fields = cmp.collect_fields_from_variants(schema)
    cmp.mark_required(fields, schema, "required_rest")
    return fields


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes")
    ap.add_argument("--dry-run", action="store_true", help="preview only")
    args = ap.parse_args()
    do_write = args.apply and not args.dry_run

    spec = cmp.load_yaml(cmp.REST_SPEC)
    mapping = json.loads(cmp.MAP_JSON.read_text(encoding="utf-8"))
    ops = cmp.build_rest_operations(spec, mapping)

    editor = Editor()
    skipped: list[str] = []

    for op in ops:
        endpoint = f"{op['method']} {op['path']}"
        if endpoint in SKIP_ENDPOINTS:
            skipped.append(endpoint)
            continue
        mqtt_command = op["mqtt_command"]
        if not mqtt_command:
            continue

        if op["method"] in ("PUT", "POST", "PATCH", "DELETE"):
            rest_schema = cmp.extract_rest_request_schema(op["operation"], spec)
            split = find_split_file(CMD_DIR, mqtt_command)
            if not split:
                continue
            data = editor._root(split)
            payload = (data.get("properties") or {}).get("payload")
            if payload is None:
                continue
            rest_fields = build_rest_required_flags(rest_schema)
            editor.sync_object(payload, split, rest_fields, "", endpoint)
        else:
            rest_schema = cmp.extract_rest_response_schema(op["operation"], spec)
            split = find_split_file(RESP_DIR, mqtt_command, "_response")
            if not split:
                continue
            data = editor._root(split)
            payload = (data.get("properties") or {}).get("payload")
            if payload is None:
                continue
            rest_fields = build_rest_required_flags(rest_schema)
            # For responses, sync the success variant(s); skip error payloads.
            if isinstance(payload, dict) and "oneOf" in payload:
                for variant in payload["oneOf"]:
                    if isinstance(variant, dict) and "$ref" in variant and "error" in variant["$ref"].lower():
                        continue
                    editor.sync_object(variant, split, rest_fields, "", endpoint)
            else:
                editor.sync_object(payload, split, rest_fields, "", endpoint)

    print(f"Endpoints skipped (structural/broken): {len(skipped)}")
    for e in skipped:
        print(f"  SKIP {e}")
    print(f"\nProposed changes: {len(editor.changes)}")
    for c in editor.changes:
        print(f"  {c}")
    print(f"\nFiles touched: {len(editor.dirty)}")

    if do_write:
        editor.write_all()
        print("\nAPPLIED.")
    else:
        print("\nDRY RUN (no files written). Re-run with --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
