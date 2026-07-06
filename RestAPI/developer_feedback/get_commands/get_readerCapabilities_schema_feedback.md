# `get_readerCapabilities` — OpenAPI schema feedback

**Command:** `get_readerCapabilities`  
**REST endpoint:** `GET /cloud/readerCapabilities`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_readerCapabilities` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_readerCapabilities` command and compared the `GET /cloud/readerCapabilities` response in `openAPISpec.yaml` with the MQTT `get_readerCapabilities` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. Several nested fields are under-specified compared with the MQTT documentation.

---

## 1. Under-typed array items (declared `object`/empty, but have a real shape)

| Field | REST (`openAPISpec.yaml`) | Zebra IoTC MQTT docs |
|-------|---------------------------|----------------------|
| `capabilities.antennas` | `items: type: object` (no properties) | array of `{ port: integer, type: enum[external, internal] }` |
| `capabilities.externalSerialPort` | `items: type: object` | array of `string` (e.g. `NONE`) |
| `capabilities.supportedPowerSource` | `items: type: object` | array of `string` (`POWERBRICK`, `POE`, `POE+`) |
| `capabilities.networkInterfaces` | `type: object` with `properties: {}` | array of `{ type, ipAssignment[], ipStack[], "802.1x", internal }` |

Please define these with their real item shapes so the response is not treated as free-form.

---

## 2. Missing `enum`s

- `capabilities.antennas[].type` — `[external, internal]`.
- Fields like `supportedPowerSource`, `ipAssignment` (`[STATIC, DHCP]`), and `ipStack` (`[IPv4, IPv6]`) are enumerated in the Zebra IoTC MQTT documentation. Please add the corresponding `enum`s.

---

## 3. Missing field descriptions

- The `capabilities.*` fields have no descriptions in `openAPISpec.yaml`. The Zebra IoTC MQTT documentation documents each capability. Please port the descriptions.

---

## 4. Example values look unrealistic

- The `openAPISpec.yaml` example contains values such as `numGPIs: 491980688`, `numGPOs: 43691`, `networkInterfaces: null`, and empty `antennas: []` / `supportedPowerSource: []`.
- The Zebra IoTC MQTT documentation shows realistic values (e.g. `numGPIs: 4`, `numGPOs: 4`, populated `antennas` and `networkInterfaces`). Please update the example to match a real reader response.

---

## Note

The MQTT `get_readerCapabilities` command in the Zebra IoTC documentation is the complete reference. This is a request to type the nested arrays (`antennas`, `externalSerialPort`, `supportedPowerSource`, `networkInterfaces`), add the enums/descriptions, and fix the example.
