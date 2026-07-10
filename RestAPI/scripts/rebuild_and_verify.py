#!/usr/bin/env python3
"""Regenerate API docs and verify REST vs MQTT schema alignment.

Runs, in order:
  1. MQTT docs  -> docs/openapi_md.json  (from schemas/)
  2. REST docs  -> RestAPI/FXR90-rest-api.yaml  (from RestDeveloperfile.yaml)
  3. Field report -> project_resources/analysis_reports/rest_vs_mqtt_field_report.xlsx

Usage:
    python RestAPI/scripts/rebuild_and_verify.py
    python RestAPI/scripts/rebuild_and_verify.py --skip-rest
    python RestAPI/scripts/rebuild_and_verify.py --skip-mqtt
    python RestAPI/scripts/rebuild_and_verify.py --strict
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MQTT_GEN = ROOT / "scripts" / "generate_openapi_tags_md.py"
REST_BUILD = ROOT / "RestAPI" / "scripts" / "build_fxr90_rest_api.py"
COMPARE = ROOT / "RestAPI" / "scripts" / "compare_rest_mqtt_schemas.py"
MQTT_OUT = ROOT / "docs" / "openapi_md.json"
REST_OUT = ROOT / "RestAPI" / "FXR90-rest-api.yaml"
REPORT_OUT = ROOT / "project_resources" / "analysis_reports" / "rest_vs_mqtt_field_report.xlsx"


def run_step(label: str, cmd: list[str]) -> int:
    print(f"\n=== {label} ===")
    print(" ".join(cmd))
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        print(f"FAILED: {label} (exit {result.returncode})", file=sys.stderr)
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate MQTT/REST docs and compare REST vs MQTT schemas."
    )
    parser.add_argument(
        "--skip-mqtt",
        action="store_true",
        help="Skip regenerating docs/openapi_md.json",
    )
    parser.add_argument(
        "--skip-rest",
        action="store_true",
        help="Skip regenerating RestAPI/FXR90-rest-api.yaml",
    )
    parser.add_argument(
        "--skip-compare",
        action="store_true",
        help="Skip REST vs MQTT field comparison report",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any step fails or field issues are found",
    )
    args = parser.parse_args()

    python = sys.executable
    exit_code = 0

    if not args.skip_mqtt:
        code = run_step("Regenerate MQTT docs", [python, str(MQTT_GEN)])
        exit_code = max(exit_code, code)
        if MQTT_OUT.is_file():
            print(f"  -> {MQTT_OUT.relative_to(ROOT)}")
        else:
            print(f"  WARNING: expected output missing: {MQTT_OUT}", file=sys.stderr)
            exit_code = max(exit_code, 1)

    if not args.skip_rest:
        code = run_step("Regenerate REST docs", [python, str(REST_BUILD)])
        exit_code = max(exit_code, code)
        if REST_OUT.is_file():
            print(f"  -> {REST_OUT.relative_to(ROOT)}")
        else:
            print(f"  WARNING: expected output missing: {REST_OUT}", file=sys.stderr)
            exit_code = max(exit_code, code)

    if not args.skip_compare:
        code = run_step("Compare REST vs MQTT schemas", [python, str(COMPARE)])
        exit_code = max(exit_code, code)
        if REPORT_OUT.is_file():
            print(f"  -> {REPORT_OUT.relative_to(ROOT)}")
        else:
            print(f"  WARNING: expected report missing: {REPORT_OUT}", file=sys.stderr)
            exit_code = max(exit_code, 1)

        if args.strict:
            try:
                import openpyxl
            except ImportError:
                print("  strict: openpyxl not installed; cannot read issue count", file=sys.stderr)
            else:
                wb = openpyxl.load_workbook(REPORT_OUT, read_only=True)
                issue_count = sum(1 for _ in wb["All Issues"].iter_rows(min_row=2))
                print(f"  Field issues: {issue_count}")
                if issue_count:
                    exit_code = max(exit_code, 1)

    print("\nDone.")
    return exit_code if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
