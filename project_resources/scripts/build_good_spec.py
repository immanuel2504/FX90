"""
Build the "good" OpenAPI file from RestDeveloperfile.yaml.

Four things, in this order:

  1. BACKFILL operationIds  - 12 operations have none. Their names are taken from the
     matching file in RestAPI/operation_descriptions/.
  2. INJECT descriptions    - replace each operation's one-line description with the full
     markdown from RestAPI/operation_descriptions/<operationId>.md (70 files, 1:1).
  3. EXTRACT inline schemas - every inline request/response body becomes a PascalCase
     component and the body becomes a $ref. Nested blocks that are SEMANTICALLY IDENTICAL
     across copies become one shared component; blocks that merely look alike but differ in
     types/enums/required/constraints are deliberately NOT merged.
  4. PRUNE orphans          - drop any component not reachable from an operation.

Then it verifies: resolving every $ref in the output must reproduce the original request /
response schemas byte-for-byte. Nothing about the API may change.

Usage:
    python build_good_spec.py [-o OUT] [--dry-run]
"""

from __future__ import annotations

import argparse
import copy
import glob
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

import yaml

ROOT = Path(r"c:\Users\Admin\Desktop\FXR90")
DESC_DIR = ROOT / "RestAPI" / "operation_descriptions"
METHODS = ("get", "put", "post", "delete", "patch")

# Keys that carry meaning. Two blocks may only share a component if these all match.
SEMANTIC = ("type", "enum", "required", "minimum", "maximum", "pattern", "format",
            "minLength", "maxLength", "minItems", "maxItems", "uniqueItems",
            "minProperties", "maxProperties", "additionalProperties", "default",
            "readOnly", "writeOnly", "oneOf", "anyOf", "allOf", "not", "nullable",
            "patternProperties", "const", "items", "properties")

# Curated names for the shared nested blocks, keyed by their sorted property list.
# Where one property list maps to several genuinely different shapes, the list gives a
# distinct name to each - they are NOT merged (rule 5).
SHARED_NAMES = {
    "cleanSession,clientId,debug,keepAlive,qos,reconnectDelay,reconnectDelayMax": ["MqttAdditionalOptions"],
    "hostName,port,protocol": ["MqttEndpoint"],
    "CACertificateFileLocation,installedCertificateName,installedCertificateType,keyAlgorithm,"
    "keyFormat,privateKeyFileLocation,publicKeyFileLocation,verifyHostName,verifyPeer": ["TlsSecurity"],
    "additional,enableSecurity,endpoint,publishTopic,security,subscribeTopic":
        ["ConnectionOptions", "ConnectionOptionsRequest"],
    "free,total,used": ["FlashPartitionUsage"],
    "maxEventRetentionTimeInMin,maxNumEvents,throttle": ["RetentionConfig", "RetentionConfigConstrained"],
    "authentication,certificate,innerAuthentication,password,username": ["EnterpriseAuthConfig"],
    "correlationFieldName,enable,responseTopic": ["DataAckConfig"],
    "dhcp,dnsAddress,domainName,gatewayAddress,ipAddress,subnetMask": ["Ipv4InterfaceConfig"],
    "dhcp,dnsAddress,domainName,gatewayAddress,ipAddress,prefix": ["Ipv6InterfaceConfig"],
    "sel,session,tagPopulation,target": ["Gen2QueryParams"],
    "batching,dataAck,retention": ["ConnectionAdditionalOptions"],
    "apn,enableIPv6,preferredNetworkType": ["SimConfig"],
    "rssi,serviceUuids128,serviceUuids16": ["BleAdditionalFilters"],
    "altBeacon,eddystone,generic,iBeacon": ["BleProtocolConfig"],
    "major,minor,txPower,uuid": ["IBeaconFilter"],
    "beaconId,major,mfgId,minor,refRssi": ["AltBeaconFilter"],
    "ephemeralId,frameType,instance,namespace,txPower,url": ["EddystoneFilter"],
    "address,addressType,alias,name": ["GenericBleFilter"],
}


# ---------------------------------------------------------------- helpers
def pascal(s: str) -> str:
    return "".join(w[:1].upper() + w[1:] for w in re.sub(r"[^0-9a-zA-Z]+", " ", s or "").split())


def fingerprint(node, keys=SEMANTIC) -> str:
    """Hash of everything that carries meaning. Prose (description/example/title) excluded."""
    def norm(n):
        if isinstance(n, dict):
            return {k: norm(v) for k, v in sorted(n.items()) if k in keys}
        if isinstance(n, list):
            return [norm(v) for v in n]
        return n
    return hashlib.md5(json.dumps(norm(node), sort_keys=True, default=str).encode()).hexdigest()[:12]


def structure(node) -> str:
    """Hash of property names + nesting only - used to find candidate duplicates cheaply."""
    def norm(n):
        if isinstance(n, dict):
            if "properties" in n:
                return {k: norm(v) for k, v in sorted((n["properties"] or {}).items())}
            if "items" in n:
                return ["[]", norm(n["items"])]
            return n.get("type", "?")
        return "?"
    return hashlib.md5(json.dumps(norm(node), sort_keys=True, default=str).encode()).hexdigest()[:12]


def iter_ops(paths):
    for p, item in paths.items():
        for m, op in (item or {}).items():
            if m in METHODS and isinstance(op, dict):
                yield p, m, op


def bodies_of(op):
    """Yield (container_dict, label, code) for every content schema on an operation."""
    for ct, c in ((op.get("requestBody") or {}).get("content") or {}).items():
        if isinstance(c, dict):
            yield c, "request", ""
    for code, r in (op.get("responses") or {}).items():
        for ct, c in ((r or {}).get("content") or {}).items():
            if isinstance(c, dict):
                yield c, "response", str(code)


class BlockDumper(yaml.SafeDumper):
    """Keeps long/multi-line strings as readable block scalars instead of one long line."""


def _str_repr(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


BlockDumper.add_representer(str, _str_repr)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?", type=Path, default=ROOT / "RestDeveloperfile.yaml",
                    help="OpenAPI file to build from (default: RestDeveloperfile.yaml)")
    ap.add_argument("-o", "--output", type=Path, default=None)
    ap.add_argument("--in-place", action="store_true",
                    help="Write back over the source. A .bak copy is made first.")
    ap.add_argument("--set-openapi", metavar="VER", default=None,
                    help="Correct the declared OpenAPI version (e.g. 3.1.0). Use when the file "
                         "declares one version but its endpoints use another version's features.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    SRC = args.source
    if not SRC.is_file():
        raise SystemExit(f"ERROR: no such file: {SRC}")

    if args.in_place:
        out = SRC
    else:
        out = args.output or SRC.with_name(f"{SRC.stem}_final{SRC.suffix}")
        if out.resolve() == SRC.resolve():
            raise SystemExit("ERROR: output equals source. Pass --in-place if that is intended.")
    args.output = out

    doc = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    original = copy.deepcopy(doc)
    paths = doc["paths"]
    schemas = doc.setdefault("components", {}).setdefault("schemas", {})

    log = {"backfilled": [], "described": [], "created": [], "shared": [], "pruned": [],
           "not_merged": [], "unmatched_md": [], "openapi": []}

    # ---------- 0. correct the declared OpenAPI version -----------------------
    if args.set_openapi and doc.get("openapi") != args.set_openapi:
        log["openapi"].append(f"{doc.get('openapi')} -> {args.set_openapi}")
        doc["openapi"] = args.set_openapi

    # ---------- 1. backfill operationIds from the description filenames -------
    md_files = {Path(f).stem: Path(f) for f in glob.glob(str(DESC_DIR / "*.md"))}
    md_ci = {k.lower(): k for k in md_files}

    # operations already carrying an id
    claimed = set()
    for p, m, op in iter_ops(paths):
        oid = op.get("operationId")
        if oid and oid.lower() in md_ci:
            claimed.add(md_ci[oid.lower()])

    # the remaining md files belong, 1:1, to the operations with no operationId
    unclaimed = sorted(set(md_files) - claimed)
    missing = [(p, m, op) for p, m, op in iter_ops(paths) if not op.get("operationId")]

    # The 12 operations without an operationId map 1:1 onto the 12 md files that no
    # existing operationId claims. Spelled out explicitly rather than guessed - the log
    # paths ("/cloud/logs/RcLog" -> "getRcLog") do not follow a derivable rule.
    BACKFILL = {
        ("get", "/cloud/gpo"): "getGpoStatus",
        ("get", "/cloud/preSelection"): "getPreSelection",
        ("put", "/cloud/preSelection"): "setPreSelection",
        ("get", "/cloud/logs/syslog"): "getLogsSyslog",
        ("delete", "/cloud/logs/syslog"): "delLogsSyslog",
        ("get", "/cloud/logs/RcLog"): "getRcLog",
        ("get", "/cloud/logs/RgWarningLog"): "getRgWarningLog",
        ("get", "/cloud/logs/RgErrorLog"): "getRgErrorLog",
        ("get", "/cloud/logs/radioPacketLog"): "getRadioPacketLog",
        ("delete", "/cloud/logs/radioPacketLog"): "delRadioPacketLog",
        ("get", "/cloud/ntpServer"): "getNtpServer",
        ("get", "/cloud/eSimConfig"): "getEsimConfig",
    }
    for p, m, op in missing:
        cand = BACKFILL.get((m, p))
        if not cand:
            continue
        if cand not in unclaimed:
            raise SystemExit(f"ERROR: {m.upper()} {p} -> '{cand}' is not an unclaimed "
                             f"description file. Unclaimed: {unclaimed}")
        op["operationId"] = cand
        unclaimed.remove(cand)
        claimed.add(cand)
        log["backfilled"].append(f"{m.upper()} {p} -> operationId: {cand}")

    if unclaimed:
        raise SystemExit(f"ERROR: description files matched to no operation: {unclaimed}")

    still = [f"{m.upper()} {p}" for p, m, op in iter_ops(paths) if not op.get("operationId")]
    if still:
        raise SystemExit("ERROR: could not derive an operationId for: " + ", ".join(still))

    # ---------- 2. inject the markdown descriptions --------------------------
    for p, m, op in iter_ops(paths):
        oid = op["operationId"]
        key = md_ci.get(oid.lower())
        if not key:
            log["unmatched_md"].append(f"{m.upper()} {p} ({oid})")
            continue
        text = md_files[key].read_text(encoding="utf-8").strip()
        if text:
            op["description"] = text
            log["described"].append(f"{m.upper()} {p} <- {key}.md")

    # ---------- 3a. find shareable nested blocks ------------------------------
    nested = defaultdict(list)   # structure-hash -> [(parent, key, node, owner)]

    def scan(node, owner, parent=None, pkey=None):
        if isinstance(node, dict):
            if "$ref" in node:
                return
            props = node.get("properties")
            if isinstance(props, dict) and len(props) >= 3 and parent is not None:
                nested[structure(node)].append((parent, pkey, node, owner))
            for k, v in node.items():
                scan(v, owner, node, k)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                scan(v, owner, node, i)

    for p, m, op in iter_ops(paths):
        for c, kind, code in bodies_of(op):
            s = c.get("schema")
            if isinstance(s, dict) and "$ref" not in s:
                scan(s, f"{m.upper()} {p}")

    share_map = {}       # id(node) -> component name
    bykey = defaultdict(list)
    for h, copies in nested.items():
        if len(copies) < 2:
            continue
        key = ",".join(sorted((copies[0][2].get("properties") or {})))
        bykey[key].append((h, copies))

    def exact(n):
        """Full deep hash - INCLUDING description/example/title."""
        return hashlib.md5(json.dumps(n, sort_keys=True, default=str).encode()).hexdigest()[:12]

    for key, groups in bykey.items():
        groups.sort(key=lambda g: -len(g[1]))
        pool = SHARED_NAMES.get(key)
        for i, (h, copies) in enumerate(groups):
            sem = {fingerprint(n) for _, _, n, _ in copies}
            owners = sorted({o for _, _, _, o in copies})

            if len(sem) > 1:
                # Rule 5: same property names, DIFFERENT meaning (types/enums/required/
                # constraints). Never merge - each keeps its own definition.
                log["not_merged"].append(
                    f"[RULE 5 - semantics differ] {key[:56]} : {len(copies)} copies, "
                    f"{len(sem)} variants [{', '.join(owners[:3])}]")
                continue

            # Semantically identical. But rule 2 forbids changing any description or
            # example, so we may only share when the copies are byte-identical too.
            groups_exact = defaultdict(list)
            for tup in copies:
                groups_exact[exact(tup[2])].append(tup)

            if len(groups_exact) > 1:
                # Rule 2 blocks the merge: identical meaning, different prose. Picking a
                # winner would rewrite what some endpoints document. Left inline; flagged.
                log["not_merged"].append(
                    f"[RULE 2 - prose differs] {key[:56]} : {len(copies)} copies, "
                    f"{len(groups_exact)} different description sets "
                    f"[{', '.join(owners[:3])}] - NEEDS A HUMAN DECISION on which "
                    f"description wins before these can share one component")
                continue

            if not pool:
                continue                      # no curated name -> leave inline
            name = pool[i] if i < len(pool) else f"{pool[0]}Variant{i+1}"
            schemas[name] = copy.deepcopy(copies[0][2])
            for _, _, n, _ in copies:
                share_map[id(n)] = name
            log["shared"].append(
                f"{name}  <- {len(copies)} byte-identical copies  [{', '.join(owners)}]")

    # ---------- 3b. replace shared blocks with $refs --------------------------
    def substitute(node):
        if isinstance(node, dict):
            for k, v in list(node.items()):
                if isinstance(v, dict) and id(v) in share_map:
                    node[k] = {"$ref": f"#/components/schemas/{share_map[id(v)]}"}
                else:
                    substitute(v)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                if isinstance(v, dict) and id(v) in share_map:
                    node[i] = {"$ref": f"#/components/schemas/{share_map[id(v)]}"}
                else:
                    substitute(v)

    for p, m, op in iter_ops(paths):
        for c, kind, code in bodies_of(op):
            s = c.get("schema")
            if isinstance(s, dict) and "$ref" not in s:
                substitute(s)

    # ---------- 3c. lift each top-level body into its own component ----------
    used = Counter()
    for p, m, op in iter_ops(paths):
        base = pascal(op["operationId"])
        for c, kind, code in bodies_of(op):
            s = c.get("schema")
            if not isinstance(s, dict) or "$ref" in s:
                continue
            name = f"{base}Request" if kind == "request" else (
                f"{base}Response" if code in ("200", "") else f"{base}Response{code}")
            used[name] += 1
            if used[name] > 1:
                name = f"{name}{used[name]}"
            schemas[name] = s
            c["schema"] = {"$ref": f"#/components/schemas/{name}"}
            log["created"].append(f"{name:38} <- {m.upper()} {p} {kind} {code}".rstrip())

    # ---------- 4. prune orphans ---------------------------------------------
    def refs_in(n):
        out = []
        if isinstance(n, dict):
            for k, v in n.items():
                if k == "$ref" and isinstance(v, str) and v.startswith("#/components/schemas/"):
                    out.append(v.rsplit("/", 1)[1])
                else:
                    out += refs_in(v)
        elif isinstance(n, list):
            for v in n:
                out += refs_in(v)
        return out

    reach, q = set(), deque(refs_in(paths))
    while q:
        n = q.popleft()
        if n in reach:
            continue
        reach.add(n)
        for r in refs_in(schemas.get(n, {})):
            q.append(r)
    for n in sorted(set(schemas) - reach):
        del schemas[n]
        log["pruned"].append(n)

    # ---------- verification --------------------------------------------------
    print("=" * 68)
    print("  BUILD GOOD SPEC  -  " + SRC.name)
    print("=" * 68)
    print(f"  operationIds backfilled     : {len(log['backfilled'])}")
    print(f"  descriptions injected       : {len(log['described'])} / 70 md files")
    print(f"  shared components created   : {len(log['shared'])}")
    print(f"  body components created     : {len(log['created'])}")
    print(f"  orphan schemas pruned       : {len(log['pruned'])}")
    print(f"  blocks deliberately NOT merged: {len(log['not_merged'])}")
    print(f"  total schemas in output     : {len(schemas)}")

    ok = True
    print("\n" + "-" * 68 + "\n  VERIFICATION\n" + "-" * 68)

    # every $ref resolves
    broken = sorted({r for r in refs_in(doc) if r not in schemas})
    print(f"  [{'PASS' if not broken else 'FAIL'}] broken $refs: {len(broken)} {broken or ''}")
    ok &= not broken

    # no orphans left
    reach2, q = set(), deque(refs_in(paths))
    while q:
        n = q.popleft()
        if n in reach2:
            continue
        reach2.add(n)
        for r in refs_in(schemas.get(n, {})):
            q.append(r)
    orph = sorted(set(schemas) - reach2)
    print(f"  [{'PASS' if not orph else 'FAIL'}] orphan components: {len(orph)} {orph or ''}")
    ok &= not orph

    # THE key check: resolving all $refs must reproduce the original schemas exactly
    def resolve(n, table, seen=()):
        """Inline every $ref against `table` so the two sides can be compared like-for-like."""
        if isinstance(n, dict):
            if "$ref" in n:
                t = n["$ref"].rsplit("/", 1)[1]
                if t in seen:
                    return {"$circular": t}
                return resolve(table[t], table, seen + (t,))
            return {k: resolve(v, table, seen) for k, v in n.items()}
        if isinstance(n, list):
            return [resolve(v, table, seen) for v in n]
        return n

    old_schemas = original["components"]["schemas"]
    mismatch = []
    for (p, m, op) in iter_ops(paths):
        oop = original["paths"][p][m]
        new = [resolve(c.get("schema"), schemas) for c, _, _ in bodies_of(op)]
        old = [resolve(c.get("schema"), old_schemas) for c, _, _ in bodies_of(oop)]
        if json.dumps(new, sort_keys=True, default=str) != json.dumps(old, sort_keys=True, default=str):
            mismatch.append(f"{m.upper()} {p}")
    print(f"  [{'PASS' if not mismatch else 'FAIL'}] resolved schemas identical to original: "
          f"{len(paths)} paths, {len(mismatch)} mismatches {mismatch[:5] or ''}")
    ok &= not mismatch

    # nothing outside paths/components touched (except a deliberate version correction)
    for k in original:
        if k in ("paths", "components"):
            continue
        if k == "openapi" and args.set_openapi:
            continue
        if original[k] != doc.get(k):
            print(f"  [FAIL] top-level section '{k}' changed")
            ok = False
    if log["openapi"]:
        print(f"  [NOTE] openapi version corrected: {log['openapi'][0]} (requested via --set-openapi)")
    print("  [PASS] info / tags / externalDocs unchanged.")
    if original["components"].get("securitySchemes") != doc["components"].get("securitySchemes"):
        print("  [FAIL] securitySchemes changed")
        ok = False
    else:
        print("  [PASS] components/securitySchemes unchanged.")

    # OpenAPI 3.1 validation
    try:
        from openapi_spec_validator import validate
        validate(doc)
        print("  [PASS] OpenAPI 3.1 validation (openapi-spec-validator).")
    except Exception as e:
        print(f"  [FAIL] OpenAPI validation: {str(e).splitlines()[0][:120]}")
        ok = False

    if log["not_merged"]:
        print("\n  Deliberately NOT merged (rule 5 - same shape, different semantics):")
        for t in log["not_merged"]:
            print("    - " + t)

    if args.dry_run:
        print("\n  --dry-run: nothing written.")
        return 0 if ok else 1

    if not ok:
        print("\n  CHECKS FAILED - refusing to write. Nothing was changed.")
        return 1

    if args.in_place:
        backup = SRC.with_suffix(SRC.suffix + ".bak")
        backup.write_bytes(SRC.read_bytes())
        print(f"\n  Backup : {backup}")

    with open(args.output, "w", encoding="utf-8", newline="") as fh:
        yaml.dump(doc, fh, Dumper=BlockDumper, sort_keys=False,
                  allow_unicode=True, width=120, default_flow_style=False)

    print(f"\n  Output : {args.output}")
    print(f"  Source : {SRC}" + ("  (overwritten in place)" if args.in_place else "  (untouched)"))
    json.dump(log, open(args.output.with_suffix(".report.json"), "w"), indent=1)
    print(f"  Report : {args.output.with_suffix('.report.json')}")
    print(f"\n  RESULT : {'ALL CHECKS PASSED' if ok else 'CHECKS FAILED - do not ship'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
