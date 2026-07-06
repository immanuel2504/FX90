# `get_networkInterfaces` — OpenAPI schema feedback

**Command:** `get_networkInterfaces`  
**REST endpoint:** `GET /cloud/networkInterfaces`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_networkInterfaces` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_networkInterfaces` command and compared the `GET /cloud/networkInterfaces` response in `openAPISpec.yaml` with the MQTT `get_networkInterfaces` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The shape matches (`availableNetworkInterfaces` array of strings); only a small documentation item is missing.

---

## 1. `availableNetworkInterfaces` has no description

- In `openAPISpec.yaml`, `availableNetworkInterfaces` is `type: array` of `string` with no description.
- The Zebra IoTC MQTT documentation describes it as "Available network interface names reported by the reader." Please add the description.

---

## 2. No `required` list

- The Zebra IoTC MQTT documentation marks `availableNetworkInterfaces` as `required`. `openAPISpec.yaml` has no `required` list — please confirm and add if appropriate.

---

## Note

The MQTT `get_networkInterfaces` command in the Zebra IoTC documentation is the complete reference. This endpoint is well typed; the only ask is a field description (and optionally the `required` list).
