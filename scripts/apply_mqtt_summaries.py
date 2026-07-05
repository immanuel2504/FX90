#!/usr/bin/env python3
"""Apply human-readable operation summaries to docs/openapi_md.json."""
from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMAND_SCHEMAS = ROOT / "Command Schemas.json"
TAG_CONFIG = ROOT / "tag_config.json"
OPENAPI_MD = ROOT / "docs" / "openapi_md.json"


def load_tag_config() -> dict:
    return json.loads(TAG_CONFIG.read_text(encoding="utf-8"))


def load_display_names() -> dict[str, str]:
    doc = json.loads(COMMAND_SCHEMAS.read_text(encoding="utf-8"))
    return {
        tag["name"]: tag["x-displayName"]
        for tag in doc.get("tags", [])
        if tag.get("name") and tag.get("x-displayName")
    }


def fallback_summary(op_name: str) -> str:
    spaced = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", op_name.replace("-", "_"))
    return spaced.replace("_", " ").title()


def resolve_summary(
    op_name: str,
    display_names: dict[str, str],
    overrides: dict[str, str],
    aliases: dict[str, str],
) -> str:
    if op_name in overrides:
        return overrides[op_name]
    tag_name = aliases.get(op_name, op_name)
    if tag_name in display_names:
        return display_names[tag_name]
    for key, label in display_names.items():
        if key.lower() == tag_name.lower():
            return label
    return fallback_summary(op_name)


def apply_to_openapi_md() -> int:
    if not OPENAPI_MD.is_file():
        raise SystemExit(f"Missing {OPENAPI_MD}")
    if not COMMAND_SCHEMAS.is_file():
        raise SystemExit(f"Missing {COMMAND_SCHEMAS}")
    if not TAG_CONFIG.is_file():
        raise SystemExit(f"Missing {TAG_CONFIG}")

    tag_config = load_tag_config()
    overrides = tag_config.get("display_name_overrides", {})
    aliases = tag_config.get("display_name_aliases", {})
    display_names = load_display_names()
    doc = json.loads(OPENAPI_MD.read_text(encoding="utf-8"), object_pairs_hook=OrderedDict)
    changed = 0

    for path, methods in doc.get("paths", {}).items():
        op_name = path.lstrip("/")
        operation = methods.get("post")
        if not isinstance(operation, dict):
            continue
        new_summary = resolve_summary(op_name, display_names, overrides, aliases)
        if operation.get("summary") != new_summary:
            operation["summary"] = new_summary
            changed += 1

    if changed:
        OPENAPI_MD.write_text(
            json.dumps(doc, indent=4, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return changed


def main() -> None:
    tag_config = load_tag_config()
    overrides = tag_config.get("display_name_overrides", {})
    aliases = tag_config.get("display_name_aliases", {})
    display_names = load_display_names()
    changed = apply_to_openapi_md()
    print(f"Loaded {len(display_names)} display names from Command Schemas.json")
    print(f"Loaded {len(overrides)} override(s) and {len(aliases)} alias(es) from tag_config.json")
    print(f"Updated {changed} operation summary(ies) in {OPENAPI_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
