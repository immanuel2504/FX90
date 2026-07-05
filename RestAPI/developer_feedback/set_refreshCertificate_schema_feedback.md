# `set_refreshCertificate` — OpenAPI schema feedback

**Command:** `set_refreshCertificate`  
**REST endpoint:** `PUT /cloud/certificates/{certname}`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_refreshCertificate` command and found a few documentation gaps. The `name` field is already well described (REST vs MQTT usage) — thank you.

---

## 1. `type` has no `enum` or description

- `type` is `type: string` with example `server`, but there is no `enum` or description.
- Could you confirm the valid certificate types (e.g. `server`, `client`) and add an `enum`?

---

## 2. PUT response has no schema

- The `200` response is `description: OK` only, with no `content`/`schema`.
- Could a response schema be added for consistency with other commands?

---

## Question

Please confirm the valid values for `type`.
