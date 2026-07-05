#!/usr/bin/env python3
"""Maintenance: camelCase operationIds, doc grammar, channelData casing."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

REST = Path(__file__).resolve().parent.parent
PATHS = REST / "paths"
MONOLITH = REST / "FXR90.yaml"
OPENAPI = REST / "openapi.yaml"
OP_DESC = REST / "operation_descriptions"
HTTP = frozenset({"get", "put", "post", "delete", "patch", "head", "options", "trace"})

OPERATION_ID_MAP = {
    "localrestlogin": "localRestLogin",
    "getAppled": "getAppLed",
    "setAppled": "setAppLed",
    "getGPIStatus": "getGpiStatus",
    "getSupportedregionlist": "getSupportedRegionList",
    "getSupportedstandardlist": "getSupportedStandardList",
    "setConfigMqtt": "setConfig",
    "setImportcloudconfig": "setImportCloudConfig",
    "getCablelosscompensation": "getCableLossCompensation",
    "setCablelosscompensation": "setCableLossCompensation",
    "setUpdatecertificate": "setUpdateCertificate",
    "setRefreshcertificate": "setRefreshCertificate",
    "getAvailablewifinetworks": "getAvailableWifiNetworks",
    "getNetworkinterfaces": "getNetworkInterfaces",
    "getReadpoints": "getReadPoints",
    "setRevertbackos": "revertBackOS",
    "setInstalluserapp": "setInstallUserApp",
    "setStartuserapp": "setStartUserApp",
    "setStopuserapp": "setStopUserApp",
    "setAutostartuserapp": "setAutostartUserApp",
    "getUserapps": "getUserApps",
    "setReqtouserapp": "setReqToUserApp",
    "setUninstalluserapp": "setUninstallUserApp",
    "getTimezone": "getTimeZone",
    "setTimezone": "setTimeZone",
    "setOs": "setOS",
    "getReadercapabilities": "getReaderCapabilities",
}

LEGACY_MD_RENAMES = {
    "GET__cloud__preSelection": "getPreSelection",
    "PUT__cloud__preSelection": "setPreSelection",
    "GET__cloud__updatePassword": "updatePassword",
    "PUT__cloud__updatePassword": "updatePassword",
    "GET__cloud__gpo": "getGpoStatus",
    "GET__cloud__eSimConfig": "getEsimConfig",
    "GET__cloud__ntpServer": "getNtpServer",
    "GET__cloud__logs__syslog": "getLogsSyslog",
    "DELETE__cloud__logs__syslog": "delLogsSyslog",
    "GET__cloud__logs__RcLog": "getRcLog",
    "GET__cloud__logs__RgWarningLog": "getRgWarningLog",
    "GET__cloud__logs__RgErrorLog": "getRgErrorLog",
    "GET__cloud__logs__radioPacketLog": "getRadioPacketLog",
    "DELETE__cloud__logs__radioPacketLog": "delRadioPacketLog",
}

OPENING_LINE_FIXES = {
    "setAppLed.md": "The `PUT /cloud/app-led` REST endpoint updates application LED state.",
    "setAppled.md": "The `PUT /cloud/app-led` REST endpoint updates application LED state.",
    "setGpo.md": "The `PUT /cloud/gpo` REST endpoint updates GPO port state.",
    "setConfig.md": "The `PUT /cloud/config` REST endpoint updates reader configuration.",
    "setConfigMqtt.md": "The `PUT /cloud/config` REST endpoint updates reader configuration.",
    "setOS.md": "The `PUT /cloud/os` REST endpoint updates OS software on the device.",
    "setOs.md": "The `PUT /cloud/os` REST endpoint updates OS software on the device.",
    "reboot.md": "The `PUT /cloud/reboot` REST endpoint restarts the reader.",
    "setPreSelection.md": "The `PUT /cloud/preSelection` REST endpoint enables or disables the rxSawFilter.",
    "setTimeZone.md": "The `PUT /cloud/timeZone` REST endpoint sets the reader timezone.",
    "setTimezone.md": "The `PUT /cloud/timeZone` REST endpoint sets the reader timezone.",
    "setCableLossCompensation.md": "The `PUT /cloud/cableLossCompensation` REST endpoint sets cable loss compensation.",
    "setCablelosscompensation.md": "The `PUT /cloud/cableLossCompensation` REST endpoint sets cable loss compensation.",
    "setHostName.md": "The `PUT /cloud/hostName` REST endpoint sets the reader hostname.",
    "setLogs.md": "The `PUT /cloud/logs` REST endpoint configures log settings.",
    "setEsimConfig.md": "The `PUT /cloud/eSimConfig` REST endpoint sets the eSIM configuration.",
    "updatePassword.md": "The `PUT /cloud/updatePassword` REST endpoint changes the password on the reader.",
    "updateNetwork.md": "The `PUT /cloud/network` REST endpoint updates network configuration, including Wi-Fi hotspot (uap0) settings.",
}

INTERNAL_NOTE_RE = re.compile(
    r"^\s*[-*]?\s*Keep REST behavior aligned with the documented reader workflow\.?\s*$",
    re.MULTILINE | re.IGNORECASE,
)
PERFORM_BULLET_RE = re.compile(
    r"^\s*[-*]?\s*Perform the operation through the REST API using bearer-token authentication\.?\s*$",
    re.MULTILINE | re.IGNORECASE,
)
BOILERPLATE_USE_BLOCK = re.compile(
    r"\n\*{0,2}Use this endpoint to:\*{0,2}\n\n(?:- .+\n)+",
    re.MULTILINE,
)


def load_yaml(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if text.startswith("# AUTO-GENERATED"):
        text = "\n".join(text.splitlines()[2:]) + "\n"
    return yaml.safe_load(text)


def dump_yaml(path: Path, doc: dict, header: str = "") -> None:
    with path.open("w", encoding="utf-8") as fh:
        if header:
            fh.write(header)
        yaml.safe_dump(doc, fh, sort_keys=False, allow_unicode=True, default_flow_style=False, width=4096)


def rename_md_file(old_name: str, new_name: str) -> None:
    if old_name.lower() == new_name.lower() and old_name != new_name:
        tmp = OP_DESC / f"__tmp__{new_name}"
        if tmp.exists():
            tmp.unlink()
        (OP_DESC / old_name).rename(tmp)
        tmp.rename(OP_DESC / new_name)
        return
    old_path = OP_DESC / old_name
    new_path = OP_DESC / new_name
    if not old_path.is_file() or old_path == new_path:
        return
    if new_path.is_file():
        old_path.unlink()
        return
    old_path.rename(new_path)


def rename_operation_description_files() -> None:
    for old_id, new_id in OPERATION_ID_MAP.items():
        rename_md_file(f"{old_id}.md", f"{new_id}.md")
    for legacy, canonical in LEGACY_MD_RENAMES.items():
        rename_md_file(f"{legacy}.md", f"{canonical}.md")
    for legacy in LEGACY_MD_RENAMES:
        path = OP_DESC / f"{legacy}.md"
        if path.is_file():
            path.unlink()


def polish_markdown_text(text: str, filename: str) -> str:
    if filename in OPENING_LINE_FIXES:
        lines = text.splitlines()
        if lines:
            lines[0] = OPENING_LINE_FIXES[filename]
            text = "\n".join(lines)

    for old_id, new_id in OPERATION_ID_MAP.items():
        text = re.sub(rf"\b{re.escape(old_id)}\b", new_id, text)
    for legacy, canonical in LEGACY_MD_RENAMES.items():
        text = text.replace(legacy, canonical)

    text = INTERNAL_NOTE_RE.sub("", text)
    text = PERFORM_BULLET_RE.sub("", text)
    text = BOILERPLATE_USE_BLOCK.sub("\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def fix_operation_descriptions() -> None:
    rename_operation_description_files()
    for md in sorted(OP_DESC.glob("*.md")):
        if md.name.lower() == "readme.md" or md.name.startswith("__tmp__"):
            continue
        original = md.read_text(encoding="utf-8-sig")
        polished = polish_markdown_text(original, md.name)
        if polished != original:
            md.write_text(polished, encoding="utf-8")


def replace_in_obj(obj, old: str, new: str) -> None:
    if isinstance(obj, dict):
        for k, v in list(obj.items()):
            if k == "operationId" and v == old:
                obj[k] = new
            else:
                replace_in_obj(v, old, new)
    elif isinstance(obj, list):
        for item in obj:
            replace_in_obj(item, old, new)


def fix_channeldata(obj) -> int:
    n = 0
    if isinstance(obj, dict):
        for key in list(obj.keys()):
            if key == "channeldata":
                obj["channelData"] = obj.pop(key)
                n += 1
            else:
                n += fix_channeldata(obj[key])
    elif isinstance(obj, list):
        for item in obj:
            n += fix_channeldata(item)
    return n


def apply_operation_ids_to_yaml(path: Path) -> int:
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    changed = 0
    for method, op in (doc or {}).items():
        if method not in HTTP or not isinstance(op, dict):
            continue
        oid = op.get("operationId")
        if oid in OPERATION_ID_MAP:
            op["operationId"] = OPERATION_ID_MAP[oid]
            changed += 1
    if changed:
        path.write_text(
            yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, default_flow_style=False),
            encoding="utf-8",
        )
    return changed


def main() -> None:
    path_changes = sum(apply_operation_ids_to_yaml(p) for p in PATHS.rglob("*.yaml"))
    channel_fixes = 0

    if MONOLITH.is_file():
        doc = load_yaml(MONOLITH)
        for old, new in OPERATION_ID_MAP.items():
            replace_in_obj(doc, old, new)
        channel_fixes += fix_channeldata(doc)
        dump_yaml(MONOLITH, doc)

    if OPENAPI.is_file():
        raw = OPENAPI.read_text(encoding="utf-8")
        header = ""
        if raw.startswith("# AUTO-GENERATED"):
            header = "\n".join(raw.splitlines()[:2]) + "\n"
        doc = yaml.safe_load(raw)
        for old, new in OPERATION_ID_MAP.items():
            replace_in_obj(doc, old, new)
        channel_fixes += fix_channeldata(doc)
        dump_yaml(OPENAPI, doc, header=header)

    fix_operation_descriptions()
    print(f"Path files updated: {path_changes} operation(s)")
    print(f"channeldata -> channelData fixes: {channel_fixes}")
    print("Operation description files updated.")


if __name__ == "__main__":
    main()
