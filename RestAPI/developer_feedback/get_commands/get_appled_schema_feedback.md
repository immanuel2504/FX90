# `get_appled` — OpenAPI schema feedback

**Command:** `get_appled`  
**REST endpoint:** `GET /cloud/app-led`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_appled` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_appled` command and compared the `GET /cloud/app-led` response in `openAPISpec.yaml` with the MQTT `get_appled` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The Zebra IoTC MQTT documentation is more specific; a couple of items are missing on the REST side.

---

## 1. `status` has no `enum`

- In `openAPISpec.yaml`, `status` is `type: string` with example `DEFAULT`, but there is no `enum`.
- The Zebra IoTC MQTT documentation constrains `status` to `enum: [DEFAULT, NOT_DEFAULT]` (`default: DEFAULT`). Please add the same `enum`/`default` so consumers know the only two valid states.

---

## 2. `status` has no description

- The field has no description in `openAPISpec.yaml`.
- The Zebra IoTC MQTT documentation describes it as the "Current App LED configuration status reported by the reader." Please add a description.

---

## Note

The MQTT `get_appled` command in the Zebra IoTC documentation is the complete reference. This is a request to add the `status` `enum` (`DEFAULT`, `NOT_DEFAULT`) and a description to the `GET /cloud/app-led` response schema.
