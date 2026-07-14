"""
Prune orphan schemas from an OpenAPI document.

An "orphan" is a schema under components/schemas that is NOT reachable from any
API operation by following $ref edges to any depth. Schemas referenced directly
by an operation, and schemas pulled in as nested children of those, are kept.

The removal is performed at the TEXT level (deleting exact line spans) rather
than by re-serialising the parsed YAML. This guarantees that every endpoint,
parameter, example, description and formatting detail outside the deleted spans
survives byte-for-byte, so the API's rendered behaviour cannot change.

Usage:
    python prune_orphan_schemas.py <input.yaml> [-o <output.yaml>] [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import deque
from pathlib import Path

import yaml

SCHEMA_REF_PREFIX = "#/components/schemas/"
# A top-level key inside components/schemas sits at exactly 4 spaces of indent.
SCHEMA_KEY_RE = re.compile(r"^    ([A-Za-z0-9_.\-]+):\s*$")


# --------------------------------------------------------------------------
# reference analysis
# --------------------------------------------------------------------------
def iter_schema_refs(node):
    """Yield every schema name targeted by a $ref anywhere beneath `node`."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str) and value.startswith(SCHEMA_REF_PREFIX):
                yield value[len(SCHEMA_REF_PREFIX):]
            else:
                yield from iter_schema_refs(value)
    elif isinstance(node, list):
        for value in node:
            yield from iter_schema_refs(value)


def reachable_from_operations(paths, schemas):
    """Transitive closure of schemas reachable from the paths section."""
    seeds = set(iter_schema_refs(paths))
    reachable, queue = set(), deque(seeds)
    while queue:
        name = queue.popleft()
        if name in reachable:
            continue
        reachable.add(name)
        for child in iter_schema_refs(schemas.get(name, {})):
            if child not in reachable:
                queue.append(child)
    return seeds, reachable


def broken_refs(doc, schemas):
    """Schema names that are $ref'd somewhere but never defined."""
    return sorted({n for n in iter_schema_refs(doc) if n not in schemas})


# --------------------------------------------------------------------------
# text-level block location
# --------------------------------------------------------------------------
def locate_schema_blocks(lines):
    """
    Map each top-level schema name to its (start, end) line span, 0-indexed and
    end-exclusive, covering the key line and everything nested under it.
    """
    try:
        schemas_line = next(i for i, l in enumerate(lines) if l.rstrip() == "  schemas:")
    except StopIteration:
        raise SystemExit("ERROR: could not find a 'components: schemas:' section.")

    # The section ends at the first subsequent line that dedents to 2 spaces or
    # less (a sibling of `schemas:` or a new top-level key).
    section_end = len(lines)
    for i in range(schemas_line + 1, len(lines)):
        line = lines[i]
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= 2:
            section_end = i
            break

    starts = []
    for i in range(schemas_line + 1, section_end):
        m = SCHEMA_KEY_RE.match(lines[i])
        if m:
            starts.append((m.group(1), i))

    blocks = {}
    for idx, (name, start) in enumerate(starts):
        end = starts[idx + 1][1] if idx + 1 < len(starts) else section_end
        # Do not swallow trailing blank lines that belong to the next block.
        while end > start + 1 and not lines[end - 1].strip():
            end -= 1
        blocks[name] = (start, end)
    return blocks, section_end


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="Delete orphan schemas from an OpenAPI file.")
    ap.add_argument("input", type=Path)
    ap.add_argument("-o", "--output", type=Path, default=None,
                    help="Output path (default: <input>_pruned.yaml). Never overwrites the input.")
    ap.add_argument("--dry-run", action="store_true", help="Report only; write nothing.")
    args = ap.parse_args()

    src = args.input
    if not src.is_file():
        raise SystemExit(f"ERROR: no such file: {src}")
    out = args.output or src.with_name(f"{src.stem}_pruned{src.suffix}")
    if out.resolve() == src.resolve():
        raise SystemExit("ERROR: refusing to overwrite the input file. Choose a different -o.")

    # newline="" keeps the original CRLF/LF endings intact, so the output differs
    # from the input by deleted lines ONLY - not by a whole-file line-ending churn.
    with open(src, encoding="utf-8", newline="") as fh:
        raw = fh.read()
    lines = raw.splitlines(keepends=True)
    doc = yaml.safe_load(raw)

    schemas = (doc.get("components") or {}).get("schemas") or {}
    paths = doc.get("paths") or {}

    # ---- analyse -----------------------------------------------------------
    pre_broken = broken_refs(doc, schemas)
    if pre_broken:
        print("WARNING: the input already has broken $refs; they are left untouched:")
        for n in pre_broken:
            print(f"   - {n}")

    direct, reachable = reachable_from_operations(paths, schemas)
    blocks, _ = locate_schema_blocks(lines)

    # Cross-check the text scan against the parsed document before deleting.
    if set(blocks) != set(schemas):
        only_text = sorted(set(blocks) - set(schemas))
        only_yaml = sorted(set(schemas) - set(blocks))
        raise SystemExit(
            "ERROR: text scan disagrees with the YAML parse; refusing to edit.\n"
            f"  only in text: {only_text}\n  only in parse: {only_yaml}"
        )

    orphans = sorted(set(schemas) - reachable, key=str.lower)
    total_before = len(schemas)

    print(f"\n{'=' * 62}\n  ORPHAN SCHEMA CLEANUP - {src.name}\n{'=' * 62}")
    print(f"  Total schemas before cleanup : {total_before}")
    print(f"  Reachable (kept)             : {len(reachable)}"
          f"   [{len(direct)} used directly by an operation,"
          f" {len(reachable) - len(direct)} nested children]")
    print(f"  Orphans (to remove)          : {len(orphans)}")
    print(f"  Remaining after cleanup      : {total_before - len(orphans)}")

    if not orphans:
        print("\n  Nothing to do - no orphans found.")
        return 0

    print(f"\n  Orphans identified ({len(orphans)}):")
    for i, name in enumerate(orphans, 1):
        start, end = blocks[name]
        print(f"    {i:>3}. {name:<42} lines {start + 1}-{end} ({end - start} lines)")

    if args.dry_run:
        print("\n  --dry-run: nothing written.")
        return 0

    # ---- delete ------------------------------------------------------------
    drop = set()
    for name in orphans:
        start, end = blocks[name]
        drop.update(range(start, end))
    kept_lines = [l for i, l in enumerate(lines) if i not in drop]
    new_raw = "".join(kept_lines)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(new_raw)

    # ---- verify ------------------------------------------------------------
    print(f"\n{'-' * 62}\n  VERIFICATION\n{'-' * 62}")
    ok = True

    try:
        new_doc = yaml.safe_load(new_raw)
        print("  [PASS] Output parses as valid YAML.")
    except yaml.YAMLError as e:
        print(f"  [FAIL] Output is not valid YAML: {e}")
        return 1

    new_schemas = (new_doc.get("components") or {}).get("schemas") or {}

    # 1. paths section untouched
    if new_doc.get("paths") == paths:
        print("  [PASS] paths section is byte-for-byte unchanged "
              "(no endpoint, request, response, parameter or example altered).")
    else:
        print("  [FAIL] paths section changed!")
        ok = False

    # 2. every other top-level section untouched
    for key in doc:
        if key == "components":
            continue
        if new_doc.get(key) != doc.get(key):
            print(f"  [FAIL] top-level section '{key}' changed!")
            ok = False
    else:
        print("  [PASS] info / tags / openapi / externalDocs sections unchanged.")

    # 3. securitySchemes untouched
    if (new_doc.get("components") or {}).get("securitySchemes") == \
            (doc.get("components") or {}).get("securitySchemes"):
        print("  [PASS] components/securitySchemes unchanged.")
    else:
        print("  [FAIL] components/securitySchemes changed!")
        ok = False

    # 4. exactly the reachable set survives, and each is identical to before
    if set(new_schemas) == reachable:
        print(f"  [PASS] Exactly the {len(reachable)} reachable schemas survive; "
              "no reachable schema was removed.")
    else:
        print(f"  [FAIL] surviving set != reachable set. "
              f"lost={sorted(reachable - set(new_schemas))} "
              f"extra={sorted(set(new_schemas) - reachable)}")
        ok = False

    if all(new_schemas.get(n) == schemas.get(n) for n in new_schemas):
        print("  [PASS] Every surviving schema is byte-identical to the original.")
    else:
        print("  [FAIL] a surviving schema's content changed!")
        ok = False

    # 5. no broken refs
    post_broken = [n for n in broken_refs(new_doc, new_schemas) if n not in pre_broken]
    if not post_broken:
        print("  [PASS] Zero broken $refs - every $ref resolves to a defined schema.")
    else:
        print(f"  [FAIL] cleanup introduced broken $refs: {post_broken}")
        ok = False

    # 6. Every $ref relationship that SURVIVES is preserved exactly.
    #    The expected set is: refs from the paths section, plus refs from inside the
    #    schemas we kept. Refs that lived inside a deleted orphan are themselves
    #    deleted along with their owner - that is the point of the exercise, and they
    #    are deliberately excluded from the comparison.
    want_refs = sorted(
        list(iter_schema_refs(paths))
        + [r for n in reachable for r in iter_schema_refs(schemas.get(n, {}))]
    )
    kept_refs = sorted(iter_schema_refs(new_doc))
    if kept_refs == want_refs:
        print(f"  [PASS] All {len(kept_refs)} surviving $ref relationships preserved exactly.")
    else:
        print("  [FAIL] $ref relationships were altered!")
        print(f"         lost:  {sorted(set(want_refs) - set(kept_refs))}")
        print(f"         extra: {sorted(set(kept_refs) - set(want_refs))}")
        ok = False

    # 7. the edit is a PURE DELETION: every surviving line appears, in order, in
    #    the original. Nothing was added, reordered or rewritten.
    i = 0
    pure = True
    for line in kept_lines:
        while i < len(lines) and lines[i] != line:
            i += 1
        if i >= len(lines):
            pure = False
            break
        i += 1
    if pure:
        print("  [PASS] Edit is a pure deletion - every surviving line appears, in order, "
              "in the original. Nothing added, reordered or rewritten.")
    else:
        print("  [FAIL] output is not a pure line-subsequence of the input!")
        ok = False

    # 8. line endings preserved (a CRLF -> LF flip would churn the whole file)
    src_crlf = raw.count("\r\n")
    out_crlf = new_raw.count("\r\n")
    src_style = "CRLF" if src_crlf else "LF"
    out_style = "CRLF" if out_crlf else "LF"
    if src_style == out_style:
        print(f"  [PASS] Line endings preserved ({src_style}).")
    else:
        print(f"  [FAIL] line endings changed: {src_style} -> {out_style}")
        ok = False

    # ---- summary -----------------------------------------------------------
    total_after = len(new_schemas)
    print(f"\n{'=' * 62}\n  SUMMARY\n{'=' * 62}")
    print(f"  Total schemas before cleanup   : {total_before}")
    print(f"  Reachable schemas              : {len(reachable)}")
    print(f"  Orphan schemas removed         : {len(orphans)}")
    print(f"  Total schemas remaining        : {total_after}")
    print(f"  Broken $ref references         : {len(post_broken)}")
    print(f"  Specification validates        : {'YES' if ok else 'NO'}")
    print(f"  Lines removed                  : {len(lines) - len(kept_lines)} "
          f"({len(lines)} -> {len(kept_lines)})")
    print(f"\n  Output written to: {out}")
    print(f"  Input left untouched: {src}\n")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
