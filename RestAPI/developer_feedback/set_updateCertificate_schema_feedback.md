# `set_updateCertificate` — OpenAPI schema feedback

**Command:** `set_updateCertificate`  
**REST endpoint:** `PUT /cloud/certificates`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_updateCertificate` command and found a few documentation gaps. `authenticationType` already has an `enum` — thank you.

---

## 1. `type` has no `enum`

- `type` is `type: string` with example `client`, but there is no `enum`.
- **`Command Schemas.json` already defines this** as `enum: [client, server, app]` with the description "Certificate type. Allowed values: client, server, app." Please copy the same `enum` (note `app` is a third valid value) into `openAPISpec.yaml`.

---

## 2. Field descriptions

- Most request fields (`authenticationOptions.username`, `authenticationOptions.password`, `name`, `pfxPassword`, `type`, `url`) have no descriptions.
- Adding descriptions would improve clarity.

---

## 3. No `required` fields declared

- No request fields are marked `required`.
- **`Command Schemas.json` already declares** `required: [name, type, url]` (with `minLength: 1`). Please align `openAPISpec.yaml` to the same.

---

## 4. PUT response has no schema

- The `200` response is `description: OK` only, with no `content`/`schema`.
- Could a response schema be added for consistency with other commands?

---

## Note

The MQTT `set_updateCertificate` schema in `Command Schemas.json` is complete (enum, required, descriptions). This is really a request to bring `openAPISpec.yaml` in line with it.
