# `get_impinjGen2X` — OpenAPI schema feedback

**Command:** `get_impinjGen2X`  
**REST endpoint:** `GET /cloud/impinjGen2X`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_impinjGen2X` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_impinjGen2X` command and compared the `GET /cloud/impinjGen2X` response in `openAPISpec.yaml` with the MQTT `get_impinjGen2X` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. This response is generally well documented (descriptions, enums, and per-feature objects for `fastID`, `tagProtect`, `tagFocus`, `tagQuieting`). One field is missing from the schema.

---

## 1. `fastID.tidSelector` is missing from the response schema

- In `openAPISpec.yaml`, the `fastID` object defines only `enabled` (with `required: [enabled]`); it has no `tidSelector` property.
- However, the endpoint's own example (`fastID_configured`) returns `tidSelector: 'TID[0]'`, and the Zebra IoTC MQTT documentation defines `fastID.tidSelector` as `type: string` with `enum: [TID[0], TID[1], TID[2], TID[3]]` and description "TID word selector mask, if one was configured."
- Because the field appears in the example (and in MQTT) but not in `properties`, it is currently undocumented. Please add `tidSelector` to the `fastID` object with the same `enum` and description. (The `PUT /cloud/impinjGen2X` request already defines `fastID.tidSelector`, so this aligns GET with PUT.)

---

## Note

The MQTT `get_impinjGen2X` command in the Zebra IoTC documentation is the complete reference. This is a targeted request to add the missing `fastID.tidSelector` property (enum `TID[0]`–`TID[3]`) to the `GET /cloud/impinjGen2X` response schema; the rest of the schema already matches.
