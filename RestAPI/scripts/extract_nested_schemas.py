"""Extract deeply nested inline object schemas into named $ref components.

Swagger UI misaligns deeply nested inline schemas. This module flattens them so
each object with properties becomes its own component schema (linked via $ref).
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from collections import OrderedDict

SCHEMA_OBJECT_KEYS = frozenset({"properties", "items", "oneOf", "anyOf", "allOf"})


def segment_to_pascal(segment) -> str:
    if isinstance(segment, int) or (isinstance(segment, str) and segment.isdigit()):
        return f"Port{segment}"
    text = str(segment)
    if text == "Item":
        return "Item"
    parts = [p for p in re.split(r"[-_\s]+", text) if p]
    return "".join(p[:1].upper() + p[1:] for p in parts)


def make_subschema_name(root_name: str, path: list) -> str:
    suffix = "".join(segment_to_pascal(part) for part in path)
    name = f"{root_name}{suffix}"
    if len(name) > 120:
        digest = hashlib.sha1(json.dumps(path, sort_keys=True).encode()).hexdigest()[:8]
        name = f"{root_name}{suffix[:80]}{digest}"
    return name


def _is_ref(node) -> bool:
    return isinstance(node, dict) and "$ref" in node


def _is_object_schema(node) -> bool:
    if not isinstance(node, dict) or _is_ref(node):
        return False
    if "properties" in node:
        return True
    return node.get("type") == "object" and any(
        key in node for key in ("properties", "additionalProperties")
    )


def _canonical_for_dedup(node) -> str:
    """Stable hash key ignoring descriptions and examples."""

    def strip(obj):
        if isinstance(obj, dict):
            if "$ref" in obj:
                return {"$ref": obj["$ref"]}
            out = {}
            for key, value in sorted(obj.items()):
                if key in {
                    "description",
                    "title",
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


def _visit(node, root_name: str, path: list, registry: dict, hash_index: dict):
    if not isinstance(node, dict):
        return node
    if _is_ref(node):
        return node

    node = copy.deepcopy(node)

    for composite in ("oneOf", "anyOf", "allOf"):
        if composite in node and isinstance(node[composite], list):
            node[composite] = [
                _visit(branch, root_name, path + [f"{composite}{idx}"], registry, hash_index)
                if isinstance(branch, dict)
                else branch
                for idx, branch in enumerate(node[composite])
            ]

    if "items" in node and isinstance(node["items"], dict):
        item_path = path + ["Item"]
        node["items"] = _visit(node["items"], root_name, item_path, registry, hash_index)

    if not _is_object_schema(node):
        return node

    properties = node.get("properties")
    if isinstance(properties, dict):
        new_props = OrderedDict()
        for prop_name, prop_schema in properties.items():
            child_path = path + [prop_name]
            new_props[prop_name] = _visit(
                prop_schema, root_name, child_path, registry, hash_index
            )
        node["properties"] = new_props

    if len(path) >= 1:
        return _register_schema(root_name, path, node, registry, hash_index)

    return node


def _register_schema(root_name: str, path: list, node: dict, registry: dict, hash_index: dict):
    canonical = _canonical_for_dedup(node)
    if canonical in hash_index:
        existing = hash_index[canonical]
        return OrderedDict([("$ref", f"#/components/schemas/{existing}")])

    name = make_subschema_name(root_name, path)
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


def flatten_schema(name: str, schema, registry: dict, hash_index: dict):
    if not isinstance(schema, dict):
        return schema
    if _is_ref(schema):
        return schema
    return _visit(schema, name, [], registry, hash_index)


def extract_nested_schemas(schemas: dict) -> tuple[dict, int]:
    """Return flattened schemas dict and count of newly extracted sub-schemas."""
    if not isinstance(schemas, dict):
        return schemas, 0

    registry = OrderedDict()
    hash_index: dict[str, str] = {}
    original_names = list(schemas.keys())

    for name in original_names:
        schema = schemas[name]
        if isinstance(schema, dict) and not _is_ref(schema):
            registry[name] = flatten_schema(name, schema, registry, hash_index)

    for name in original_names:
        if name not in registry:
            registry[name] = schemas[name]

    extracted_count = len(registry) - len(original_names)
    return registry, extracted_count


def apply_to_document(doc: dict) -> tuple[dict, int]:
    components = doc.get("components")
    if not isinstance(components, dict):
        return doc, 0
    schemas = components.get("schemas")
    if not isinstance(schemas, dict):
        return doc, 0

    flattened, count = extract_nested_schemas(schemas)
    doc = copy.deepcopy(doc)
    doc.setdefault("components", OrderedDict())
    doc["components"]["schemas"] = flattened
    return doc, count
