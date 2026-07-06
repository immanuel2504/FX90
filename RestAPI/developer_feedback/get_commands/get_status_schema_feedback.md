# `get_status` — OpenAPI schema feedback

**Command:** `get_status`  
**REST endpoint:** `GET /cloud/status`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_status` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_status` command and compared the `GET /cloud/status` response in `openAPISpec.yaml` with the MQTT `get_status` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The `impinjGen2X` and `ble` blocks are already well documented (descriptions + enums), but the remaining fields are missing `enum`s and descriptions that the MQTT documentation provides.

---

## 1. Missing `enum`s on state fields

The following fields are `type: string` with no `enum` in `openAPISpec.yaml`, but are constrained in the Zebra IoTC MQTT documentation:

| Field | Missing `enum` (per Zebra IoTC MQTT docs) |
|-------|-------------------------------------------|
| `antennas.1` … `antennas.6` | `[connected, disconnected]` |
| `radioActivity` | `[active, inactive]` |
| `radioConnection` | `[connected, disconnected]` |

Please add these `enum`s.

---

## 2. Missing field descriptions

- Most fields have no description in `openAPISpec.yaml` — e.g. `antennas`, `cpu` (`system`/`user`), `flash` (`platform`/`readerConfig`/`readerData`/`rootFileSystem` with `free`/`total`/`used`), `interfaceConnectionStatus`, `ntp` (`offset`/`reach`), `powerNegotiation`, `powerSource`, `ram`, `systemTime`, `temperature`, `uptime`.
- The Zebra IoTC MQTT documentation describes each of these (e.g. `temperature` = "Current reader internal temperature in degrees Celsius", `powerSource` = "Detected power source for the reader"). Please port the descriptions.

---

## Note

The MQTT `get_status` command in the Zebra IoTC documentation is the complete reference. The `impinjGen2X`/`ble` blocks are already aligned; this is a request to add the `enum`s and descriptions to the remaining status fields.
