# `get_preSelection` / `set_preSelection` — OpenAPI schema feedback

**Commands:** `get_preSelection`, `set_preSelection`  
**REST endpoints:** `GET /cloud/preSelection`, `PUT /cloud/preSelection`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_preSelection` and `set_preSelection` commands (`/cloud/preSelection` REST endpoints) and found a few documentation gaps. The API contract itself is consistent, but some schema metadata could be improved.

---

## 1. `get_preSelection` — GET response (`preSelection`)

- The field is defined as `type: string`, but there is no `enum`.
- The example shows `"disabled"`, however the schema does not specify whether the valid values are only `"enabled"` and `"disabled"` or whether other string values are allowed.
- If only specific values are supported, could you please add an `enum` to the schema? Otherwise, the current schema is technically a free-form string.

---

## 2. Field descriptions

- The developer OpenAPI specification (`openAPISpec.yaml`) does not include descriptions for the `preSelection` fields, while our generated REST specification does.
- It would be helpful to add field descriptions in the source specification so the documentation is complete and consistent.

---

## 3. `set_preSelection` — PUT response

- The response schema is defined as `type: string` (empty string example), but it has no description explaining the expected response.
- Could a description be added to clarify why the endpoint returns an empty string?

---

## Question

Please let me know whether the GET `preSelection` value is intentionally an unrestricted string or whether it should be limited to specific values such as `"enabled"` and `"disabled"`. That will determine whether an `enum` should be added to the schema.
