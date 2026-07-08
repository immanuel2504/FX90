#!/usr/bin/env python3
"""
build_openapi.py
================
Build the REST API spec from ``RestAPI/paths/`` (your editable source).
On every run it:
 * auto-generates ``RestAPI/openapi.yaml`` from ``FXR90.yaml`` + ``paths/``,
 * inlines each path file into one bundled document,
 * merges ``RestAPI/operation_descriptions/*.md`` into operation descriptions,
 * flattens deeply nested inline schemas into named ``$ref`` components (Swagger UI),
 * writes ``RestAPI/FXR90-rest-api.yaml`` for Swagger UI,
then validates references (and ``openapi-spec-validator`` when installed).
You only edit ``RestAPI/paths/``. Do not edit ``openapi.yaml`` or
``FXR90-rest-api.yaml`` — both are generated.
Run:
   python RestAPI/scripts/build_openapi.py
"""
from __future__ import annotations
import copy
import hashlib
import json
import re
import shutil
from collections import OrderedDict
from pathlib import Path
import yaml

HTTP_METHODS = frozenset(
   {"get", "put", "post", "delete", "patch", "head", "options", "trace"}
)

_INTERNAL_NOTE_RE = re.compile(
    r"^\s*[-*]?\s*Keep REST behavior aligned with the documented reader workflow\.?\s*$",
    re.MULTILINE | re.IGNORECASE,
)
_PERFORM_BULLET_RE = re.compile(
    r"^\s*[-*]?\s*Perform the operation through the REST API using bearer-token authentication\.?\s*$",
    re.MULTILINE | re.IGNORECASE,
)
_BOILERPLATE_USE_BLOCK = re.compile(
    r"\n\*{0,2}Use this endpoint to:\*{0,2}\n\n(?:- .+\n)+",
    re.MULTILINE,
)
_SCHEMA_REVIEW_RE = re.compile(
    r"^\s*Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint\.?\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def sanitize_operation_description(text: str) -> str:
    text = _INTERNAL_NOTE_RE.sub("", text)
    text = _PERFORM_BULLET_RE.sub("", text)
    text = _SCHEMA_REVIEW_RE.sub("", text)
    text = _BOILERPLATE_USE_BLOCK.sub("\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return f"{text}\n" if text else ""


# --- Nested schema extraction (Swagger UI layout) ---------------------------------


def _segment_to_pascal(segment) -> str:
    if isinstance(segment, int) or (isinstance(segment, str) and segment.isdigit()):
        return f"Port{segment}"
    text = str(segment)
    if text == "Item":
        return "Item"
    parts = [p for p in re.split(r"[-_\s]+", text) if p]
    return "".join(p[:1].upper() + p[1:] for p in parts)


def _make_subschema_name(root_name: str, path: list) -> str:
    suffix = "".join(_segment_to_pascal(part) for part in path)
    name = f"{root_name}{suffix}"
    if len(name) > 120:
        digest = hashlib.sha1(json.dumps(path, sort_keys=True).encode()).hexdigest()[:8]
        name = f"{root_name}{suffix[:80]}{digest}"
    return name


def _schema_is_ref(node) -> bool:
    return isinstance(node, dict) and "$ref" in node


def _schema_is_object(node) -> bool:
    if not isinstance(node, dict) or _schema_is_ref(node):
        return False
    if "properties" in node:
        return True
    return node.get("type") == "object" and any(
        key in node for key in ("properties", "additionalProperties")
    )


def _schema_canonical_for_dedup(node) -> str:
    def strip(obj):
        if isinstance(obj, dict):
            if "$ref" in obj:
                return {"$ref": obj["$ref"]}
            out = {}
            for key, value in sorted(obj.items()):
                # Keep description/title in the dedup hash: schemas that differ
                # in documentation must stay separate components, otherwise the
                # first-registered wording silently overwrites the others
                # (e.g. flash/ram error+warning blocks all inheriting the CPU text).
                if key in {
                    "example",
                    "examples",
                    "x-examples",
                    "default",
                } or (isinstance(key, str) and key.startswith("x-")):
                    continue
                out[key] = strip(value)
            return out
        if isinstance(obj, list):
            return [strip(item) for item in obj]
        return obj

    return json.dumps(strip(node), sort_keys=True, separators=(",", ":"))


def _copy_schema_meta(node: dict) -> OrderedDict:
    meta = OrderedDict()
    for key in ("type", "description", "required", "nullable", "title", "enum", "default"):
        if key in node:
            meta[key] = copy.deepcopy(node[key])
    return meta


def _visit_nested_schema(node, root_name: str, path: list, registry: dict, hash_index: dict):
    if not isinstance(node, dict):
        return node
    if _schema_is_ref(node):
        return node

    node = copy.deepcopy(node)

    for composite in ("oneOf", "anyOf", "allOf"):
        if composite in node and isinstance(node[composite], list):
            node[composite] = [
                _visit_nested_schema(branch, root_name, path + [f"{composite}{idx}"], registry, hash_index)
                if isinstance(branch, dict)
                else branch
                for idx, branch in enumerate(node[composite])
            ]

    if "items" in node and isinstance(node["items"], dict):
        node["items"] = _visit_nested_schema(
            node["items"], root_name, path + ["Item"], registry, hash_index
        )

    if not _schema_is_object(node):
        return node

    properties = node.get("properties")
    if isinstance(properties, dict):
        node["properties"] = OrderedDict(
            (prop_name, _visit_nested_schema(prop_schema, root_name, path + [prop_name], registry, hash_index))
            for prop_name, prop_schema in properties.items()
        )

    if len(path) >= 1:
        return _register_nested_schema(root_name, path, node, registry, hash_index)

    return node


def _register_nested_schema(root_name: str, path: list, node: dict, registry: dict, hash_index: dict):
    canonical = _schema_canonical_for_dedup(node)
    if canonical in hash_index:
        existing = hash_index[canonical]
        return OrderedDict([("$ref", f"#/components/schemas/{existing}")])

    name = _make_subschema_name(root_name, path)
    while name in registry:
        name = f"{name}Ref"

    extracted = _copy_schema_meta(node)
    if "properties" in node:
        extracted["properties"] = node["properties"]
    if "items" in node and "properties" not in extracted:
        extracted["items"] = node["items"]
    for composite in ("oneOf", "anyOf", "allOf"):
        if composite in node:
            extracted[composite] = node[composite]

    registry[name] = extracted
    hash_index[canonical] = name
    return OrderedDict([("$ref", f"#/components/schemas/{name}")])


def _flatten_schema(name: str, schema, registry: dict, hash_index: dict):
    if not isinstance(schema, dict):
        return schema
    if _schema_is_ref(schema):
        return schema
    return _visit_nested_schema(schema, name, [], registry, hash_index)


def extract_nested_schemas(schemas: dict) -> tuple[dict, int]:
    if not isinstance(schemas, dict):
        return schemas, 0

    registry = OrderedDict()
    hash_index: dict[str, str] = {}
    original_names = list(schemas.keys())

    for name in original_names:
        schema = schemas[name]
        if isinstance(schema, dict) and not _schema_is_ref(schema):
            registry[name] = _flatten_schema(name, schema, registry, hash_index)

    for name in original_names:
        if name not in registry:
            registry[name] = schemas[name]

    return registry, len(registry) - len(original_names)


# --- OpenAPI 3.0 normalization (Swagger UI compatibility) -------------------------

VENDOR_EXTENSION_PREFIX = "x-"
SCHEMA_DOC_STRIP_KEYS = frozenset({"example", "examples", "x-examples"})


def _is_schema_object(node: dict) -> bool:
    if "$ref" in node:
        return True
    return any(
        key in node
        for key in ("type", "properties", "items", "oneOf", "anyOf", "allOf", "enum")
    )


def _fix_tag_metadata_items(obj: dict) -> dict:
    items = obj.get("items")
    if not isinstance(items, dict):
        return obj
    type_val = items.get("type")
    if not isinstance(type_val, list):
        return obj
    if "enum" not in items or "properties" not in items:
        return obj

    enum_vals = items.pop("enum")
    props = items.pop("properties")
    items.pop("type", None)
    items.clear()
    items["oneOf"] = [
        OrderedDict([("type", "string"), ("enum", enum_vals)]),
        OrderedDict([("type", "object"), ("properties", props)]),
    ]
    return obj


def _fix_malformed_selects(obj: dict) -> dict:
    if "selects" in obj and isinstance(obj["selects"], dict):
        selects = obj["selects"]
        if selects.get("type") == "array" and isinstance(selects.get("oneOf"), list):
            one_of = []
            for branch in selects["oneOf"]:
                if isinstance(branch, dict) and "items" in branch and "type" not in branch:
                    one_of.append(
                        OrderedDict([("type", "array"), ("items", branch["items"])])
                    )
                else:
                    one_of.append(branch)
            rebuilt = OrderedDict()
            if "description" in selects:
                rebuilt["description"] = selects["description"]
            rebuilt["oneOf"] = one_of
            obj["selects"] = rebuilt
    return obj


def normalize_for_oas30(obj):
    if isinstance(obj, dict):
        obj = OrderedDict(obj)

        if "examples" in obj and _is_schema_object(obj):
            obj.pop("examples", None)

        if "example" in obj and _is_schema_object(obj):
            obj.pop("example", None)

        type_val = obj.get("type")
        if isinstance(type_val, list):
            non_null = [t for t in type_val if t != "null"]
            has_null = "null" in type_val
            if len(non_null) == 1:
                obj["type"] = non_null[0]
                if has_null:
                    obj["nullable"] = True
            elif non_null:
                obj.pop("type", None)
                obj["oneOf"] = [OrderedDict([("type", t)]) for t in non_null]
                if has_null:
                    obj["nullable"] = True
            else:
                obj.pop("type", None)
                obj["nullable"] = True

        enum_val = obj.get("enum")
        if isinstance(enum_val, list):
            deduped = []
            seen = []
            for item in enum_val:
                if item not in seen:
                    seen.append(item)
                    deduped.append(item)
            obj["enum"] = deduped

        for bound, limit in (("exclusiveMinimum", "minimum"), ("exclusiveMaximum", "maximum")):
            val = obj.get(bound)
            if isinstance(val, bool):
                continue
            if isinstance(val, (int, float)):
                obj.setdefault(limit, val)
                obj[bound] = True

        obj = _fix_tag_metadata_items(obj)
        obj = _fix_malformed_selects(obj)

        for key, value in obj.items():
            obj[key] = normalize_for_oas30(value)
        return obj

    if isinstance(obj, list):
        return [normalize_for_oas30(item) for item in obj]
    return obj


def fix_delete_request_bodies(paths: dict, schemas: dict | None = None) -> int:
    fixed = 0
    schemas = schemas or {}

    for path_item in paths.values():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            if method != "delete" or "requestBody" not in operation:
                continue

            body = operation.get("requestBody", {})
            content = body.get("content", {}) if isinstance(body, dict) else {}
            json_content = content.get("application/json", {})
            schema = json_content.get("schema", {}) if isinstance(json_content, dict) else {}

            if isinstance(schema, dict) and "$ref" in schema:
                ref = schema["$ref"]
                if ref.startswith("#/components/schemas/"):
                    ref_name = ref.rsplit("/", 1)[-1]
                    schema = schemas.get(ref_name, schema)

            props = schema.get("properties", {}) if isinstance(schema, dict) else {}
            if not isinstance(props, dict) or not props:
                operation.pop("requestBody", None)
                fixed += 1
                continue

            params = list(operation.get("parameters") or [])
            existing = {(p.get("in"), p.get("name")) for p in params if isinstance(p, dict)}
            for prop_name, prop_schema in props.items():
                if ("query", prop_name) in existing or ("path", prop_name) in existing:
                    continue
                params.append(
                    OrderedDict(
                        [
                            ("name", prop_name),
                            ("in", "query"),
                            ("required", prop_name in (schema.get("required") or [])),
                            (
                                "schema",
                                prop_schema if isinstance(prop_schema, dict) else OrderedDict(),
                            ),
                        ]
                    )
                )
            operation["parameters"] = params
            operation.pop("requestBody", None)
            fixed += 1
    return fixed


def _strip_schema_doc_noise(obj):
    if isinstance(obj, dict):
        obj = OrderedDict(obj)
        for key in list(obj.keys()):
            if key in SCHEMA_DOC_STRIP_KEYS or (
                isinstance(key, str) and key.startswith(VENDOR_EXTENSION_PREFIX)
            ):
                obj.pop(key, None)
        for key, value in obj.items():
            obj[key] = _strip_schema_doc_noise(value)
        return obj
    if isinstance(obj, list):
        return [_strip_schema_doc_noise(item) for item in obj]
    return obj


def _sanitize_media_content(content) -> None:
    if not isinstance(content, dict):
        return
    for media_obj in content.values():
        if isinstance(media_obj, dict) and "schema" in media_obj:
            media_obj["schema"] = _strip_schema_doc_noise(media_obj["schema"])


def _sanitize_path_schemas(paths: dict) -> None:
    for path_item in paths.values():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            body = operation.get("requestBody")
            if isinstance(body, dict):
                _sanitize_media_content(body.get("content"))
            for response in (operation.get("responses") or {}).values():
                if isinstance(response, dict):
                    _sanitize_media_content(response.get("content"))


def sanitize_for_swagger_ui(doc: dict) -> dict:
    components = doc.get("components")
    if isinstance(components, dict):
        schemas = components.get("schemas")
        if isinstance(schemas, dict):
            for name in list(schemas.keys()):
                schemas[name] = _strip_schema_doc_noise(schemas[name])
    if isinstance(doc.get("paths"), dict):
        _sanitize_path_schemas(doc["paths"])
    return doc


def normalize_openapi_document(doc: dict, *, openapi_version: str = "3.0.3") -> dict:
    doc = normalize_for_oas30(doc)
    doc = sanitize_for_swagger_ui(doc)
    doc["openapi"] = openapi_version
    schemas = doc.get("components", {}).get("schemas", {})
    if isinstance(doc.get("paths"), dict):
        fix_delete_request_bodies(doc["paths"], schemas if isinstance(schemas, dict) else None)
    return doc


REST_DIR = Path(__file__).resolve().parent.parent
ROOT_IN = REST_DIR / "openapi.yaml"
BUNDLED_OUT = REST_DIR / "FXR90-rest-api.yaml"
SCHEMAS_DIR = REST_DIR / "schemas"
PATHS_DIR = REST_DIR / "paths"
OP_DESCRIPTIONS_DIR = REST_DIR / "operation_descriptions"
MONOLITH = REST_DIR / "FXR90.yaml"
TAG_TO_FOLDER = {
   "Login": "login",
   "System": "system",
   "Network": "network",
   "Control": "control",
   "Region": "region",
   "Gpio": "gpio",
   "App-led": "led",
   "Logs": "logs",
   "Date&Time": "datetime",
   "Certificate": "certificates",
   "Firmware": "firmware",
   "userapp": "userapps",
   "Ble": "ble",
   "ImpinjGen2X": "impinj",
}
PATH_FOLDER_OVERRIDE = {
   "/cloud/cloudConfig": "system",
}
AUTO_GENERATED_HEADER = (
   "# AUTO-GENERATED by RestAPI/scripts/build_openapi.py — do not edit.\n"
   "# Edit RestAPI/paths/ and run: python RestAPI/scripts/build_openapi.py\n"
)
def _represent_ordereddict(dumper, data):
   return dumper.represent_mapping("tag:yaml.org,2002:map", data.items())
yaml.add_representer(OrderedDict, _represent_ordereddict)
yaml.SafeDumper.add_representer(OrderedDict, _represent_ordereddict)
def load_yaml(path: Path):
   with path.open("r", encoding="utf-8") as fh:
       return yaml.safe_load(fh)
def dump_yaml(path: Path, data, *, header: str = "") -> None:
   path.parent.mkdir(parents=True, exist_ok=True)
   with path.open("w", encoding="utf-8") as fh:
       if header:
           fh.write(header)
       yaml.safe_dump(
           data,
           fh,
           sort_keys=False,
           allow_unicode=True,
           default_flow_style=False,
           width=4096,
       )
def path_filename(api_path: str) -> str:
   segments = [s for s in api_path.strip("/").split("/") if s]
   if segments and segments[0] == "cloud":
       segments = segments[1:]
   cleaned = [s.replace("{", "").replace("}", "") for s in segments]
   return "_".join(cleaned) if cleaned else "root"
def folder_for_path(api_path: str, item: dict) -> str:
   if api_path in PATH_FOLDER_OVERRIDE:
       return PATH_FOLDER_OVERRIDE[api_path]
   for method, op in item.items():
       if isinstance(op, dict) and op.get("tags"):
           tag = str(op["tags"][0]).strip()
           return TAG_TO_FOLDER.get(tag, "misc")
   return "misc"
def path_file_for_api_path(api_path: str, path_item: dict, paths_dir: Path) -> Path:
   folder = folder_for_path(api_path, path_item)
   fname = path_filename(api_path)
   return paths_dir / folder / f"{fname}.yaml"
def build_openapi_root(monolith: dict, paths_dir: Path, existing_root: dict | None = None) -> tuple[OrderedDict, list[str]]:
   paths = monolith.get("paths", {})
   schemas = OrderedDict(monolith.get("components", {}).get("schemas", {}))
   if existing_root:
       existing_schemas = existing_root.get("components", {}).get("schemas", {})
       for name, schema in existing_schemas.items():
           if name not in schemas:
               schemas[name] = schema
   root = OrderedDict()
   root["openapi"] = "3.0.3"
   root["info"] = monolith.get("info", {})
   if "externalDocs" in monolith:
       root["externalDocs"] = monolith["externalDocs"]
   if "servers" in monolith:
       root["servers"] = monolith["servers"]
   if "tags" in monolith:
       root["tags"] = monolith["tags"]
   root_paths = OrderedDict()
   missing: list[str] = []
   for api_path, item in paths.items():
       path_file = path_file_for_api_path(api_path, item, paths_dir)
       if not path_file.is_file():
           missing.append(str(path_file.relative_to(paths_dir.parent)))
           continue
       rel = path_file.relative_to(paths_dir.parent).as_posix()
       root_paths[api_path] = {"$ref": f"./{rel}"}
   root["paths"] = root_paths
   components = OrderedDict()
   sec = monolith.get("components", {}).get("securitySchemes")
   if sec:
       components["securitySchemes"] = sec
   components["schemas"] = schemas
   root["components"] = components
   return root, missing
def schema_name_from_ref(ref: str) -> str:
   return Path(ref).name[: -len(".yaml")] if ref.endswith(".yaml") else Path(ref).name
def normalize_schema_ref(ref: str) -> str:
   if ref.startswith("#/components/schemas/"):
       return ref
   if ref.endswith(".yaml"):
       return f"#/components/schemas/{schema_name_from_ref(ref)}"
   if "#/components/schemas/" in ref:
       return f"#/components/schemas/{ref.split('/components/schemas/')[-1]}"
   return ref
def load_rest_operation_descriptions() -> dict[str, str]:
   descriptions: dict[str, str] = {}
   if not OP_DESCRIPTIONS_DIR.is_dir():
       return descriptions
   for path in sorted(OP_DESCRIPTIONS_DIR.iterdir()):
       if path.suffix.lower() != ".md" or path.name.lower() == "readme.md":
           continue
       if path.name.startswith("_"):
           continue
       text = sanitize_operation_description(path.read_text(encoding="utf-8-sig").strip())
       if text:
           descriptions[path.stem] = text
   return descriptions
def description_key(method: str, api_path: str, operation_id: str | None) -> str:
   if operation_id:
       return operation_id
   safe = api_path.strip("/").replace("/", "__")
   return f"{method.upper()}__{safe}"
def apply_operation_descriptions(
   path_item: dict,
   api_path: str,
   descriptions: dict[str, str],
) -> int:
   applied = 0
   for method, operation in path_item.items():
       if method not in HTTP_METHODS or not isinstance(operation, dict):
           continue
       key = description_key(method, api_path, operation.get("operationId"))
       md = descriptions.get(key)
       if md:
           operation["description"] = md
           applied += 1
   return applied
def to_internal_refs(node):
   if isinstance(node, dict):
       return {
           key: normalize_schema_ref(value) if key == "$ref" and isinstance(value, str) else to_internal_refs(value)
           for key, value in node.items()
       }
   if isinstance(node, list):
       return [to_internal_refs(v) for v in node]
   return node
def collect_refs(node, out):
   if isinstance(node, dict):
       for key, value in node.items():
           if key == "$ref" and isinstance(value, str) and value.startswith("#/components/schemas/"):
               out.add(value.split("/")[-1])
           else:
               collect_refs(value, out)
   elif isinstance(node, list):
       for v in node:
           collect_refs(v, out)
def rewrite_path_file_refs(path: Path) -> bool:
   text = path.read_text(encoding="utf-8")
   original = text
   for line in text.splitlines():
       if "$ref:" not in line or "schemas/" not in line:
           continue
       ref = line.split("$ref:", 1)[1].strip()
       if not ref.endswith(".yaml"):
           continue
       name = schema_name_from_ref(ref)
       text = text.replace(f"$ref: {ref}", f"$ref: ../../openapi.yaml#/components/schemas/{name}")
   if text != original:
       path.write_text(text, encoding="utf-8")
       return True
   return False
def cleanup_legacy_layout() -> None:
   if PATHS_DIR.is_dir():
       fixes = sum(1 for p in PATHS_DIR.rglob("*.yaml") if rewrite_path_file_refs(p))
       if fixes:
           print(f"Legacy fix     : updated {fixes} path file(s) with old schemas/ refs")
   if SCHEMAS_DIR.exists():
       shutil.rmtree(SCHEMAS_DIR)
       print("Legacy fix     : removed RestAPI/schemas/")
def generate_openapi_yaml() -> int:
   """Regenerate openapi.yaml from FXR90.yaml metadata and paths/ files."""
   if not MONOLITH.is_file():
       raise SystemExit(f"Missing {MONOLITH.name} (needed to generate openapi.yaml)")
   if not PATHS_DIR.is_dir():
       raise SystemExit(f"Missing {PATHS_DIR.relative_to(REST_DIR.parent)} — nothing to build")
   doc = load_yaml(MONOLITH)
   existing_root = load_yaml(ROOT_IN) if ROOT_IN.is_file() else None
   root, missing = build_openapi_root(doc, PATHS_DIR, existing_root)
   if missing:
       print("\nMissing path file(s) (expected under RestAPI/paths/):")
       for rel in missing:
           print(f"  {rel}")
       raise SystemExit(1)
   dump_yaml(ROOT_IN, root, header=AUTO_GENERATED_HEADER)
   return len(root.get("paths", {}))
def flatten_operation_schemas(root: OrderedDict) -> int:
   """Extract nested inline schemas so Swagger UI renders cleaner $ref links."""
   schemas = root.get("components", {}).get("schemas")
   if not isinstance(schemas, dict):
       return 0
   flattened, count = extract_nested_schemas(schemas)
   root.setdefault("components", OrderedDict())
   root["components"]["schemas"] = flattened
   return count
def load_schema_entry(name: str, ref_obj, base: Path) -> dict:
   if not isinstance(ref_obj, dict):
       raise ValueError(f"Cannot load schema {name!r}: {ref_obj!r}")
   if "$ref" not in ref_obj:
       return to_internal_refs(ref_obj)
   ref = ref_obj["$ref"]
   if isinstance(ref, str) and ref.endswith(".yaml"):
       return to_internal_refs(load_yaml((base / ref).resolve()))
   if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
       return ref_obj
   raise ValueError(f"Cannot load schema {name!r}: {ref_obj!r}")
def main() -> None:
   cleanup_legacy_layout()
   path_refs = generate_openapi_yaml()
   root = load_yaml(ROOT_IN)
   extracted = flatten_operation_schemas(root)
   dump_yaml(ROOT_IN, root, header=AUTO_GENERATED_HEADER)
   if extracted:
       print(f"Schema flatten : extracted {extracted} nested sub-schema(s)")
   op_descriptions = load_rest_operation_descriptions()
   bundled = OrderedDict()
   for key in ("openapi", "info", "externalDocs", "servers", "tags"):
       if key in root:
           bundled[key] = root[key]
   paths_out = OrderedDict()
   op_count = 0
   desc_applied = 0
   for path, ref_obj in root.get("paths", {}).items():
       ref = ref_obj["$ref"]
       item = load_yaml((ROOT_IN.parent / ref).resolve())
       desc_applied += apply_operation_descriptions(item, path, op_descriptions)
       paths_out[path] = to_internal_refs(item)
       op_count += sum(1 for m in paths_out[path] if m in HTTP_METHODS)
   bundled["paths"] = paths_out
   components = OrderedDict()
   src_components = root.get("components", {})
   if "securitySchemes" in src_components:
       components["securitySchemes"] = src_components["securitySchemes"]
   schemas_out = OrderedDict()
   for name, ref_obj in src_components.get("schemas", {}).items():
       schemas_out[name] = load_schema_entry(name, ref_obj, ROOT_IN.parent)
   components["schemas"] = schemas_out
   bundled["components"] = components
   bundled = normalize_openapi_document(bundled)
   with BUNDLED_OUT.open("w", encoding="utf-8") as fh:
       fh.write(
           "# AUTO-GENERATED by RestAPI/scripts/build_openapi.py — do not edit.\n"
           "# Edit RestAPI/paths/ and rebuild.\n"
       )
       yaml.safe_dump(
           bundled,
           fh,
           sort_keys=False,
           allow_unicode=True,
           default_flow_style=False,
           width=4096,
       )
   declared = set(schemas_out.keys())
   used: set = set()
   collect_refs(paths_out, used)
   collect_refs(schemas_out, used)
   missing = sorted(used - declared)
   print(f"Generated      : {ROOT_IN.name} ({path_refs} path refs)")
   print(f"Paths          : {len(paths_out)}")
   print(f"Operations     : {op_count}")
   print(f"Schemas        : {len(schemas_out)}")
   print(f"Refs used       : {len(used)}")
   print(f"REST op docs    : {len(op_descriptions)} file(s), {desc_applied} operation(s) updated")
   print(f"Bundled output  : {BUNDLED_OUT.name}")
   if missing:
       print("\nBROKEN REFERENCES (no matching schema):")
       for m in missing:
           print(f"  #/components/schemas/{m}")
   else:
       print("Reference check : OK (all $ref targets resolve)")
   try:
       from openapi_spec_validator import validate as _validate  # type: ignore
       _validate(load_yaml(BUNDLED_OUT))
       print("openapi-spec-validator: VALID")
   except ImportError:
       print("openapi-spec-validator: not installed (skipped optional deep validation)")
   except Exception as exc:  # noqa: BLE001
       print(f"openapi-spec-validator: ISSUES -> {exc}")
   if missing:
       raise SystemExit(1)
if __name__ == "__main__":
   main()
