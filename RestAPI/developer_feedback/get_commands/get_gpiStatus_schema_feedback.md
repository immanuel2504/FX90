# `get_gpiStatus` — OpenAPI schema feedback

**Command:** `get_gpiStatus`  
**REST endpoint:** `GET /cloud/gpi`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_gpiStatus` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_gpiStatus` command and compared the `GET /cloud/gpi` response in `openAPISpec.yaml` with the MQTT `get_gpiStatus` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The response is mostly well specified — each port already has `enum: [HIGH, LOW]` — but a couple of smaller items are missing.

---

## 1. Per-port fields have no descriptions

- The port keys (`1`, `2`, `3`, `4`) are `type: string` with `enum: [HIGH, LOW]` but no descriptions.
- The Zebra IoTC MQTT documentation describes each as e.g. "State of GPI port 1. Allowed values: HIGH, LOW." Please add the same descriptions.

---

## 2. No `required` ports

- `openAPISpec.yaml` marks none of the ports as `required`.
- The Zebra IoTC MQTT documentation marks ports `1` and `2` as `required` (these are present on all supported reader types). Please confirm and add `required: ['1', '2']` if applicable to FXR90.

---

## Note

The MQTT `get_gpiStatus` command in the Zebra IoTC documentation is the complete reference. The `enum`s are already correct; this is a request to add per-port descriptions and confirm the `required` ports.
