# Developer feedback — scenario clarifications (GET endpoints)

Each file here explains a GET-endpoint schema gap using a **concrete scenario** (a real request/response example) so the developer can quickly see the ambiguity and confirm the intended behavior. These are the scenario-style companions to the concise `*_schema_feedback.md` files in the [parent `get_commands/` folder](../README.md).

Every scenario compares the `openAPISpec.yaml` GET response against the corresponding MQTT command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal.

## Scenario files (one per command)

| Command | Endpoint | Scenario focus |
|---------|----------|----------------|
| `get_appled` | `GET /cloud/app-led` | `status` no `enum` (`DEFAULT`, `NOT_DEFAULT`) |
| `get_gpiStatus` | `GET /cloud/gpi` | per-port descriptions; `required` ports |
| `get_region` | `GET /cloud/region` | `channelData` items `integer` vs `string` |
| `get_SupportedRegionList` | `GET /cloud/supportedRegionList` | `SupportedRegions` no description |
| `get_version` | `GET /cloud/version` | `model` no `enum`; descriptions |
| `get_status` | `GET /cloud/status` | state fields no `enum`; descriptions |
| `get_readerCapabilities` | `GET /cloud/readerCapabilities` | under-typed arrays; unrealistic example |
| `get_cableLossCompensation` | `GET /cloud/cableLossCompensation` | numbered keys; `minimum`/descriptions |
| `get_logs` | `GET /cloud/logs` | `componentName`/`level` no `enum` |
| `get_timeZone` | `GET /cloud/timeZone` | `timeZone` no `enum`; example not in list |
| `get_certificates` | `GET /cloud/certificates` | `type` no `enum`; descriptions |
| `get_availableWifiNetworks` | `GET /cloud/wifiNetworks` | field descriptions |
| `get_networkInterfaces` | `GET /cloud/networkInterfaces` | field description; `required` |
| `get_userapps` | `GET /cloud/apps` | descriptions; item `required`; constraints |
| `get_hostname` | `GET /cloud/hostName` | `hostName` no description |
| `get_impinjGen2X` | `GET /cloud/impinjGen2X` | `fastID.tidSelector` missing from schema |

## Commands reviewed — no scenario needed

Already match the Zebra IoTC MQTT documentation (typed schema, enums, descriptions, examples):
`get_config`, `get_network`, `get_readPoints`, `get_gpsCoordinates`, `get_bleConfig`.
