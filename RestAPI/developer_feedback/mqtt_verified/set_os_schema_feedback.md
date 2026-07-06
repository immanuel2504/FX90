# `set_os` — OpenAPI schema feedback

**Command:** `set_os`  
**REST endpoint:** `PUT /cloud/os`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_os` command and found a few documentation gaps. `authenticationType` already has an `enum` — thank you.

---

## 1. Example does not match the schema (`options` vs `authenticationOptions`)

- The schema defines the credentials object as `options` (containing `username`/`password`).
- The `set_os` example uses `authenticationOptions` instead of `options`.
- **The Zebra IoTC MQTT documentation confirms the correct field name is `options`** (with `required: [username, password]`). So the schema field name is right and only the **example** is wrong — please fix the example to use `options`.

---

## 2. Field descriptions and missing optional fields

- The request fields (`options.username`, `options.password`, `url`) have no descriptions in `openAPISpec.yaml`.
- The Zebra IoTC MQTT documentation already has descriptions, plus extra fields not in `openAPISpec.yaml`: `verifyPeer`, `verifyHost`, `CACertificateFileLocation`, `CACertificateFileContent`, `headers.Authorization`, and `retry`. If these apply to REST, please add them and align descriptions.

---

## 3. PUT response has no schema

- The `200` response is `description: OK` only, with no `content`/`schema`.
- Could a response schema be added for consistency with other commands?

---

## Question

Please confirm whether the credentials object should be named `options` or `authenticationOptions`, so the schema and example can be aligned.
