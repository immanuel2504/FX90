# `get_hostname` — OpenAPI schema feedback

**Command:** `get_hostname`  
**REST endpoint:** `GET /cloud/hostName`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_hostname` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_hostname` command and compared the `GET /cloud/hostName` response in `openAPISpec.yaml` with the MQTT `get_hostname` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The response returns a single `hostName` field; the casing is correct (`hostName`) but a couple of documentation items are missing.

---

## 1. `hostName` has no description

- In `openAPISpec.yaml`, `hostName` is `type: string` with example `FXR90C60C001`, but there is no description.
- The Zebra IoTC MQTT documentation describes it as the "Hostname of the reader." Please add the description.

---

## 2. No `required` list

- The Zebra IoTC MQTT documentation marks `hostName` as `required` on the payload. `openAPISpec.yaml` has no `required` list — please confirm and add if appropriate.

> Note: the response field is correctly `hostName` (camelCase). This differs from the `set_hostName` **request** body, which uses `hostname` (lowercase) — see the separate `set_hostName` feedback for that casing question.

---

## Note

The MQTT `get_hostname` command in the Zebra IoTC documentation is the complete reference. This is a small request to add a description (and optionally the `required` list) to the `GET /cloud/hostName` response schema.
