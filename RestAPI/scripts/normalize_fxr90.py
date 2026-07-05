#!/usr/bin/env python3
"""Normalize RestAPI/FXR90.yaml to OpenAPI 3.0 (safe atomic write)."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REST_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from oas30_normalize import normalize_openapi_document

MONOLITH = REST_DIR / "FXR90.yaml"


def to_plain(obj):
    if isinstance(obj, dict):
        return {k: to_plain(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [to_plain(v) for v in obj]
    return obj


def main() -> None:
    doc = yaml.safe_load(MONOLITH.read_text(encoding="utf-8"))
    doc = normalize_openapi_document(doc)
    plain = to_plain(doc)
    tmp = MONOLITH.with_suffix(".yaml.tmp")
    with tmp.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(
            plain,
            fh,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=4096,
        )
    tmp.replace(MONOLITH)
    print(f"Normalized {MONOLITH.name} -> openapi {plain.get('openapi')}")


if __name__ == "__main__":
    main()
