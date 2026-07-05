"""Normalize OpenAPI 3.1 / JSON Schema 2020 constructs to OpenAPI 3.0."""
from __future__ import annotations

from collections import OrderedDict

HTTP_METHODS = frozenset(
    {"get", "put", "post", "delete", "patch", "head", "options", "trace"}
)

# Stoplight / editor metadata — hide from Swagger UI schema panels
VENDOR_EXTENSION_PREFIX = "x-"

# Removed from component schemas (and nested property schemas) for cleaner Swagger UI
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
                        OrderedDict(
                            [
                                ("type", "array"),
                                ("items", branch["items"]),
                            ]
                        )
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
    """Move DELETE requestBody fields to query parameters (OAS 3.0 semantic rule)."""
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
    """Remove examples and vendor extensions from schema trees (Swagger UI cleanup)."""
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


def _sanitize_path_schemas(paths: dict) -> None:
    """Strip schema-level examples from request/response bodies; keep media-type examples."""
    for path_item in paths.values():
        if not isinstance(path_item, dict):
            continue
        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            for body_key in ("requestBody",):
                body = operation.get(body_key)
                if isinstance(body, dict):
                    _sanitize_media_content(body.get("content"))
            for response in (operation.get("responses") or {}).values():
                if isinstance(response, dict):
                    _sanitize_media_content(response.get("content"))


def _sanitize_media_content(content) -> None:
    if not isinstance(content, dict):
        return
    for media_obj in content.values():
        if isinstance(media_obj, dict) and "schema" in media_obj:
            media_obj["schema"] = _strip_schema_doc_noise(media_obj["schema"])


def sanitize_for_swagger_ui(doc: dict) -> dict:
    """Remove schema examples and x-* metadata from components and inline path schemas."""
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
