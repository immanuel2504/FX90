#!/usr/bin/env python3
"""Apply human-readable operation summaries from Command Schemas.json."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

REST = Path(__file__).resolve().parent.parent
ROOT = REST.parent
PATHS = REST / "paths"
COMMAND_SCHEMAS = ROOT / "Command Schemas.json"
REST_MQTT_MAP = REST / "mappings" / "rest_mqtt_map.json"
HTTP = frozenset({"get", "put", "post", "delete", "patch", "head", "options", "trace"})

# MQTT command aliases where rest_mqtt_map label differs from Command Schemas tag name
MQTT_TAG_ALIASES = {
    "get_supportedStandardList": "get_SupportedStandardlist",
    "get_SupportedStandardList": "get_SupportedStandardlist",
}

# REST-only or missing from Command Schemas tags
OPERATION_SUMMARY_OVERRIDES = {
    "localRestLogin": "Reader Login",
    "getPreSelection": "Get Pre-Selection",
    "setPreSelection": "Set Pre-Selection",
    "updatePassword": "Change Password",
    "setImportCloudConfig": "Import Cloud Configuration",
    "getReaderCapabilities": "Get Reader Capabilities",
    "getEsimConfig": "Get eSIM Configuration",
    "setEsimConfig": "Set eSIM Configuration",
    "getImpinjGen2X": "Get Impinj Gen2X Configuration",
    "setImpinjGen2X": "Set Impinj Gen2X Configuration",
    "getBleConfig": "Get BLE Configuration",
    "setBleConfig": "Set BLE Configuration",
    "status": "Pass-Through Command",
    "setRegion": "Set Reader Region Configuration",
    "getAvailableWifiNetworks": "Get Available Wi-Fi Networks",
    "getNetworkInterfaces": "Get Network Interfaces",
    "getReadPoints": "Get Read Points",
    "getGpsCoordinates": "Get GPS Coordinates",
    "setDataToRG": "Set Data to RG",
}


def load_display_names() -> dict[str, str]:
    doc = json.loads(COMMAND_SCHEMAS.read_text(encoding="utf-8"))
    return {
        tag["name"]: tag["x-displayName"]
        for tag in doc.get("tags", [])
        if tag.get("name") and tag.get("x-displayName")
    }


def load_operation_summaries() -> dict[str, str]:
    display = load_display_names()
    mapping = json.loads(REST_MQTT_MAP.read_text(encoding="utf-8"))
    summaries: dict[str, str] = dict(OPERATION_SUMMARY_OVERRIDES)

    for entry in mapping.get("restToMqtt", []):
        operation_id = entry.get("operationId")
        mqtt_command = entry.get("mqttCommand")
        if not operation_id:
            continue
        tag_name = MQTT_TAG_ALIASES.get(mqtt_command, mqtt_command)
        label = display.get(tag_name)
        if label:
            summaries[operation_id] = label

    return summaries


def apply_to_paths(summaries: dict[str, str]) -> int:
    changed = 0
    for path_file in sorted(PATHS.rglob("*.yaml")):
        doc = yaml.safe_load(path_file.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            continue
        file_changed = False
        for method, operation in doc.items():
            if method not in HTTP or not isinstance(operation, dict):
                continue
            operation_id = operation.get("operationId")
            if not operation_id or operation_id not in summaries:
                continue
            new_summary = summaries[operation_id]
            if operation.get("summary") != new_summary:
                operation["summary"] = new_summary
                file_changed = True
        if file_changed:
            path_file.write_text(
                yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, default_flow_style=False),
                encoding="utf-8",
            )
            changed += 1
    return changed


def main() -> None:
    if not COMMAND_SCHEMAS.is_file():
        raise SystemExit(f"Missing {COMMAND_SCHEMAS}")
    summaries = load_operation_summaries()
    changed = apply_to_paths(summaries)
    print(f"Loaded {len(summaries)} operation summary labels from Command Schemas.json")
    print(f"Updated {changed} path file(s)")


if __name__ == "__main__":
    main()
