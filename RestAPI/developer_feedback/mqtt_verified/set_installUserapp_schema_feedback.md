# `set_installUserapp` — OpenAPI schema feedback

**Command:** `set_installUserapp`  
**REST endpoint:** `PUT /cloud/apps/install`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_installUserapp` command against the Zebra IoTC MQTT documentation and `openAPISpec.yaml` and found a field naming mismatch plus a few gaps. `authenticationType` already has an `enum` — thank you.

---

## 1. Credentials field name mismatch: `authenticationOptions` vs `options`

- `openAPISpec.yaml` defines the credentials object as **`authenticationOptions`** (`username`/`password`).
- The Zebra IoTC MQTT documentation defines it as **`options`** (`username`/`password`, with `required: [username, password]`).
- These do not match. Could you confirm the correct field name the device expects and align `openAPISpec.yaml` to it? (the Zebra IoTC MQTT documentation suggests `options`.)

---

## 2. Missing optional fields present in the Zebra IoTC MQTT documentation

- The Zebra IoTC MQTT documentation documents additional fields not present in `openAPISpec.yaml`: `verifyPeer`, `verifyHost`, `CACertificateFileLocation`, `CACertificateFileContent`, `headers.Authorization`, and `retry`.
- If these are supported over REST, could they be added to `openAPISpec.yaml`?

---

## 3. Field descriptions and `required`

- The request fields in `openAPISpec.yaml` have no descriptions, and no fields are marked `required` (e.g. `filename`, `url` appear necessary).
- The Zebra IoTC MQTT documentation already has descriptions for these fields — please align.

---

## Question

Please confirm the correct credentials field name (`authenticationOptions` vs `options`) and which fields are required for a successful install.
