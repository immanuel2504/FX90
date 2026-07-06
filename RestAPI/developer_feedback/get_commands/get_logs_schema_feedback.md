# `get_logs` — OpenAPI schema feedback

**Command:** `get_logs`  
**REST endpoint:** `GET /cloud/logs`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_logs` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_logs` command and compared the `GET /cloud/logs` response in `openAPISpec.yaml` with the MQTT `get_logs` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The shape matches, but the two enumerated fields have no `enum` and there are no descriptions.

---

## 1. `components[].componentName` has no `enum`

- In `openAPISpec.yaml`, `componentName` is `type: string` with no `enum`.
- The Zebra IoTC MQTT documentation constrains it to `enum: [radio_control, reader_gateway]`. Please add the same `enum`.

---

## 2. `components[].level` has no `enum`

- In `openAPISpec.yaml`, `level` is `type: string` with no `enum`.
- The Zebra IoTC MQTT documentation constrains it to `enum: [DEBUG, INFO, WARNING, ERROR]`. Please add the same `enum`.

---

## 3. Missing descriptions

- `componentName`, `level`, and `radioPacketLog` have no descriptions.
- The Zebra IoTC MQTT documentation describes them (e.g. `radioPacketLog` = "Indicates whether radio packet logging is enabled"; `componentName` notes that for `radio_control` only `INFO` is supported, while `reader_gateway` supports `INFO`, `DEBUG`, `WARNING`, `ERROR`). Please port these descriptions.

---

## Note

The MQTT `get_logs` command in the Zebra IoTC documentation is the complete reference. This mirrors the `set_logs` feedback: please add the `componentName`/`level` `enum`s and the descriptions to the `GET /cloud/logs` response schema.
