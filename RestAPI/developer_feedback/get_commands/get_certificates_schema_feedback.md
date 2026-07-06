# `get_certificates` — OpenAPI schema feedback

**Command:** `get_certificates`  
**REST endpoint:** `GET /cloud/certificates`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_certificates` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_certificates` command and compared the `GET /cloud/certificates` response in `openAPISpec.yaml` with the MQTT `get_certificates` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The response is an array of certificate objects; the fields match but are under-specified.

---

## 1. `type` has no `enum`

- In `openAPISpec.yaml`, each certificate's `type` is `type: string` with example `server`, but there is no `enum`.
- The Zebra IoTC MQTT documentation constrains `type` to `enum: [server, client, app]`. Please add the same `enum`.

---

## 2. Fields have no descriptions

- The certificate fields (`name`, `type`, `installTime`, `issuerName`, `publickey`, `serial`, `subjectName`, `validityStart`, `validityEnd`) have no descriptions.
- The Zebra IoTC MQTT documentation describes each one (e.g. `name` = "Certificate name on the reader", `validityEnd` = "Certificate validity end date"). Please port the descriptions.

---

## 3. No `required` list on the item

- The Zebra IoTC MQTT documentation marks all certificate fields as `required` for each array item. `openAPISpec.yaml` has no `required` list — please confirm and add if appropriate.

---

## Note

The MQTT `get_certificates` command in the Zebra IoTC documentation is the complete reference. This is a request to add the `type` `enum` (`server`, `client`, `app`), field descriptions, and the item-level `required` list.
