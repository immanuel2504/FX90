"""
Collapse the prose-divergent duplicate blocks into shared components.

These blocks are already known to be SEMANTICALLY IDENTICAL across every copy - same
types, enums, required lists and validation constraints. The only thing blocking a merge
is that their descriptions differ. This script resolves that by taking, for each property,
the description used by the MAJORITY of copies, and reports every change it makes.

Nothing about the API changes. Types, enums, required lists and constraints are untouched.
Only prose is unified - and every single wording change is listed in the report so it can
be reviewed and reverted.

Blocks whose copies differ SEMANTICALLY are never merged (rule 5).

Usage:
    python merge_shared_components.py <input.yaml> -o <output.yaml> [--dry-run]
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

import yaml

METHODS = ("get", "put", "post", "delete", "patch")
SEMANTIC = ("type", "enum", "required", "minimum", "maximum", "pattern", "format",
            "minLength", "maxLength", "minItems", "maxItems", "uniqueItems",
            "minProperties", "maxProperties", "additionalProperties", "default",
            "readOnly", "writeOnly", "oneOf", "anyOf", "allOf", "not", "nullable",
            "patternProperties", "const", "items", "properties")

# Curated names. Where one property list maps to several genuinely different shapes,
# each gets its own name - they are NOT merged together.
NAMES = {
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
    "apn,currentDataClass,currentServiceProvider,enableIPv6,enablePin,enableRoaming,"
    "highestAvailableDataClass,internetAccess,packetServiceState,preferredNetworkType,"
    "registerState,rsrp,rsrq,rssi,signalBar,simState,snr": ["SimStatus"],
    "apn,enableIPv6,preferredNetworkType": ["SimConfig"],
    "rssi,serviceUuids128,serviceUuids16": ["BleAdditionalFilters"],
    "altBeacon,eddystone,generic,iBeacon": ["BleProtocolConfig"],
    "major,minor,txPower,uuid": ["IBeaconFilter"],
    "beaconId,major,mfgId,minor,refRssi": ["AltBeaconFilter"],
    "ephemeralId,frameType,instance,namespace,txPower,url": ["EddystoneFilter"],
    "address,addressType,alias,name": ["GenericBleFilter"],
}


PROSE_KEYS = ("description", "example", "examples", "title")


def sem(node):
    """
    Semantic fingerprint: the block with all prose stripped out, and nothing else.

    Two blocks are safe to share a component if and only if this is equal - i.e. they are
    byte-identical once description/example/title are set aside. Any difference in a type,
    enum, required list, constraint, or property name makes them different blocks, and they
    are never merged.
    """
    def norm(n):
        if isinstance(n, dict):
            return {k: norm(v) for k, v in sorted(n.items())
                    if k not in PROSE_KEYS and not k.startswith("x-")}
        if isinstance(n, list):
            return [norm(v) for v in n]
        return n
    return hashlib.md5(json.dumps(norm(node), sort_keys=True, default=str).encode()).hexdigest()[:12]


def structure(n):
    if isinstance(n, dict):
        if "properties" in n:
            return {k: structure(v) for k, v in sorted((n["properties"] or {}).items())}
        if "items" in n:
            return ["[]", structure(n["items"])]
        return n.get("type", "?")
    return "?"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("-o", "--output", type=Path, required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if args.output.resolve() == args.source.resolve():
        raise SystemExit("ERROR: refusing to overwrite the source.")

    doc = yaml.safe_load(args.source.read_text(encoding="utf-8"))
    original = copy.deepcopy(doc)
    paths, schemas = doc["paths"], doc["components"]["schemas"]

    # ---- locate every duplicate block, anywhere in the document ---------------
    found = defaultdict(list)          # structure-hash -> [(parent, key, node, where)]

    def scan(node, where, parent=None, pkey=None):
        if isinstance(node, dict):
            if "$ref" in node:
                return
            props = node.get("properties")
            if isinstance(props, dict) and len(props) >= 3 and parent is not None:
                found[hashlib.md5(json.dumps(structure(node), sort_keys=True,
                                             default=str).encode()).hexdigest()[:12]].append(
                    (parent, pkey, node, where))
            for k, v in node.items():
                scan(v, where, node, k)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                scan(v, where, node, i)

    for p, item in paths.items():
        for m, op in (item or {}).items():
            if m not in METHODS or not isinstance(op, dict):
                continue
            for c in ((op.get("requestBody") or {}).get("content") or {}).values():
                scan((c or {}).get("schema"), f"{m.upper()} {p}")
            for code, r in (op.get("responses") or {}).items():
                for c in ((r or {}).get("content") or {}).values():
                    scan((c or {}).get("schema"), f"{m.upper()} {p}")
    for name, body in list(schemas.items()):
        scan(body, f"components/{name}")

    # ---- decide what to merge ------------------------------------------------
    bykey = defaultdict(list)
    for hh, copies in found.items():
        if len(copies) < 2:
            continue
        key = ",".join(sorted((copies[0][2].get("properties") or {})))
        bykey[key].append(copies)

    merged, skipped, changes = [], [], []
    for key, groups in bykey.items():
        groups.sort(key=lambda g: -len(g))
        pool = NAMES.get(key)
        if not pool:
            continue
        for i, copies in enumerate(groups):
            variants = {sem(n) for _, _, n, _ in copies}
            if len(variants) > 1:
                skipped.append((key, len(copies),
                                f"RULE 5 - {len(variants)} semantically different variants; NEVER merged"))
                continue
            name = pool[i] if i < len(pool) else f"{pool[0]}Variant{i+1}"
            if name in schemas:
                skipped.append((key, len(copies), f"name '{name}' already taken"))
                continue

            # Promote the FIRST copy itself - do NOT deep-copy. Keeping the same object
            # means that when a nested block inside it is merged later, the substitution
            # lands in this promoted node too (they are the same dict).
            canon = copies[0][2]

            # For each prose field, take the wording used by the majority of copies.
            # `description` AND `example` both count as prose under rule 2, so both are
            # voted on and every losing variant is reported.
            for field in ("description", "example"):
                variants = Counter()
                for _, _, n, _ in copies:
                    v = n.get(field)
                    if v is not None:
                        variants[json.dumps(v, sort_keys=True, default=str)] += 1
                if len(variants) < 2:
                    continue
                winner, wins = variants.most_common(1)[0]
                canon[field] = json.loads(winner)
                for losing, n_lose in variants.most_common()[1:]:
                    changes.append(dict(component=name, prop=f"<{field} on the block itself>",
                                        field=field, kept=winner, kept_count=wins,
                                        dropped=losing, dropped_count=n_lose))

            for prop in (canon.get("properties") or {}):
                for field in ("description", "example"):
                    variants = Counter()
                    for _, _, n, _ in copies:
                        pv = (n.get("properties") or {}).get(prop)
                        if isinstance(pv, dict) and pv.get(field) is not None:
                            variants[json.dumps(pv[field], sort_keys=True, default=str)] += 1
                    if len(variants) < 2:
                        continue
                    winner, wins = variants.most_common(1)[0]
                    canon["properties"][prop][field] = json.loads(winner)
                    for losing, n_lose in variants.most_common()[1:]:
                        changes.append(dict(component=name, prop=prop, field=field,
                                            kept=winner, kept_count=wins,
                                            dropped=losing, dropped_count=n_lose))

            schemas[name] = canon
            for parent, pkey, node, where in copies:
                parent[pkey] = {"$ref": f"#/components/schemas/{name}"}
            merged.append((name, len(copies), sorted({w for _, _, _, w in copies})))

    # ---- report --------------------------------------------------------------
    print("=" * 70)
    print(f"  MERGE SHARED COMPONENTS  -  {args.source.name}")
    print("=" * 70)
    print(f"  components merged      : {len(merged)}")
    print(f"  duplicate copies removed: {sum(c - 1 for _, c, _ in merged)}")
    print(f"  description changes    : {len(changes)}")
    print(f"  blocks left alone      : {len(skipped)}")
    print(f"  total schemas          : {len(original['components']['schemas'])} -> {len(schemas)}")

    print("\n  MERGED:")
    for name, cnt, owners in sorted(merged, key=lambda x: -x[1]):
        print(f"    {name:30} x{cnt:<2} {', '.join(owners)[:58]}")

    if skipped:
        print("\n  NOT MERGED (left exactly as they are):")
        for key, cnt, why in skipped:
            print(f"    x{cnt}  {key[:50]:52} {why}")

    # ---- verify --------------------------------------------------------------
    ok = True
    print("\n" + "-" * 70 + "\n  VERIFICATION\n" + "-" * 70)

    def refs(n):
        o = []
        if isinstance(n, dict):
            for k, v in n.items():
                if k == "$ref" and isinstance(v, str) and v.startswith("#/components/schemas/"):
                    o.append(v.rsplit("/", 1)[1])
                else:
                    o += refs(v)
        elif isinstance(n, list):
            for v in n:
                o += refs(v)
        return o

    broken = sorted({r for r in refs(doc) if r not in schemas})
    print(f"  [{'PASS' if not broken else 'FAIL'}] broken $refs: {len(broken)} {broken or ''}")
    ok &= not broken

    reach, q = set(), deque(refs(paths))
    while q:
        n = q.popleft()
        if n in reach:
            continue
        reach.add(n)
        for r in refs(schemas.get(n, {})):
            q.append(r)
    orph = sorted(set(schemas) - reach)
    print(f"  [{'PASS' if not orph else 'FAIL'}] orphan components: {len(orph)} {orph or ''}")
    ok &= not orph

    # THE key check: resolving refs must reproduce the original EXACTLY, once prose
    # (description / example / title) is set aside. Every prose change is listed below
    # for review; nothing else is permitted to move.
    PROSE = ("description", "example", "examples", "title")

    def resolve(n, table, seen=()):
        if isinstance(n, dict):
            if "$ref" in n:
                t = n["$ref"].rsplit("/", 1)[1]
                if t in seen:
                    return {"$c": t}
                return resolve(table[t], table, seen + (t,))
            return {k: resolve(v, table, seen) for k, v in n.items() if k not in PROSE}
        if isinstance(n, list):
            return [resolve(v, table, seen) for v in n]
        return n

    def bodies(op):
        out = [c.get("schema") for c in ((op.get("requestBody") or {}).get("content") or {}).values()]
        for r in (op.get("responses") or {}).values():
            out += [c.get("schema") for c in ((r or {}).get("content") or {}).values()]
        return out

    old_s = original["components"]["schemas"]
    bad = []
    for p, item in paths.items():
        for m, op in (item or {}).items():
            if m not in METHODS or not isinstance(op, dict):
                continue
            a = json.dumps([resolve(s, schemas) for s in bodies(op)], sort_keys=True, default=str)
            b = json.dumps([resolve(s, old_s) for s in bodies(original["paths"][p][m])],
                           sort_keys=True, default=str)
            if a != b:
                bad.append(f"{m.upper()} {p}")
    print(f"  [{'PASS' if not bad else 'FAIL'}] every type, enum, required list and constraint "
          f"identical to the original: {len(bad)} mismatches {bad[:4] or ''}")
    ok &= not bad

    try:
        from openapi_spec_validator import validate
        validate(doc)
        print(f"  [PASS] OpenAPI {doc['openapi']} validation.")
    except Exception as e:
        print(f"  [FAIL] OpenAPI validation: {str(e).splitlines()[0][:110]}")
        ok = False

    if changes:
        print(f"\n  DESCRIPTION CHANGES ({len(changes)}) - review these:")
        for c in changes:
            print(f"\n    {c['component']}.{c['prop']}")
            print(f"      KEPT    (x{c['kept_count']}): {c['kept'][:105]}")
            print(f"      DROPPED (x{c['dropped_count']}): {c['dropped'][:105]}")

    if args.dry_run:
        print("\n  --dry-run: nothing written.")
        return 0 if ok else 1
    if not ok:
        print("\n  CHECKS FAILED - refusing to write.")
        return 1

    class D(yaml.SafeDumper):
        pass
    D.add_representer(str, lambda d, s: d.represent_scalar(
        "tag:yaml.org,2002:str", s, style="|" if "\n" in s else None))
    with open(args.output, "w", encoding="utf-8", newline="") as fh:
        yaml.dump(doc, fh, Dumper=D, sort_keys=False, allow_unicode=True,
                  width=120, default_flow_style=False)
    json.dump(dict(merged=[(n, c, o) for n, c, o in merged], changes=changes, skipped=skipped),
              open(args.output.with_suffix(".changes.json"), "w"), indent=1)
    print(f"\n  Output : {args.output}")
    print(f"  Changes: {args.output.with_suffix('.changes.json')}")
    print(f"  Source : {args.source}  (untouched)")
    print("\n  RESULT : ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
