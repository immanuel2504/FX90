# `get_version` — OpenAPI schema feedback

**Command:** `get_version`  
**REST endpoint:** `GET /cloud/version`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_version` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_version` command and compared the `GET /cloud/version` response in `openAPISpec.yaml` with the MQTT `get_version` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The fields match, but the REST schema is missing an `enum` and field descriptions.

---

## 1. `model` has no `enum`

- In `openAPISpec.yaml`, `model` is `type: string` with example `FXR90`, but there is no `enum`.
- The Zebra IoTC MQTT documentation constrains `model` to `enum: [FXR90, FX7500, FX9600, ATR7000]`. Please add the same `enum`.

---

## 2. Fields have no descriptions

- None of the response fields (`availableOsUpgrades`, `cloudAgentApplication`, `model`, `radioControlApplication`, `radioFirmware`, `readerApplication`, `revertBackFirmware`, `serialNumber`) have descriptions.
- The Zebra IoTC MQTT documentation describes each one (e.g. `serialNumber` = "Unique serial number assigned to the reader", `radioFirmware` = "Firmware version running on the RFID radio module"). Please port these descriptions.

---

## Note

The MQTT `get_version` command in the Zebra IoTC documentation is the complete reference. This is a request to add the `model` `enum` and field descriptions to the `GET /cloud/version` response schema.
