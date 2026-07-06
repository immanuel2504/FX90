# Developer feedback — scenario clarifications

Each file here explains a schema gap using a **concrete scenario** (a real request/response example) so the developer can quickly see the ambiguity and confirm the intended behavior. These are the scenario-style companions to the concise `*_schema_feedback.md` files in the parent folder.

> Note: the scenarios for `setUpdateCertificate`, `setOS`, `setInstallUserApp`, and `setMode` were moved to [`../mqtt_verified/scenarios/`](../mqtt_verified/README.md) (verified against the Zebra IoTC MQTT documentation).

## Scenario files (one per command / group)

| Command(s) | Endpoint | Scenario focus |
|------------|----------|----------------|
| `get_preSelection` / `set_preSelection` | `/cloud/preSelection` | GET value no `enum`; response descriptions |
| `get_appled` / `set_appled` | `/cloud/app-led` | `color`/`status` no `enum` (differs from `set_stackled`) |
| `set_gpo` | `/cloud/gpo` | `port` no range |
| `set_region` | `/cloud/region` | `country`/`standardname` no `enum`/reference |
| `get_SupportedStandardList` | `/cloud/supportedStandardList` | `channeldata` vs `channelData`; boolean-as-string |
| `set_passthru` | `/cloud/pass-through` | `component`/`payload` no `enum`; `operationId` is `status` |
| `set_cableLossCompensation` | `/cloud/cableLossCompensation` | units/ranges; numbered keys |
| `reboot` | `/cloud/reboot` | device ID mentioned but not in schema |
| `set_password` | `/cloud/updatePassword` | `required`; password rules |
| `set_logs` | `/cloud/logs` | `level`/`componentName` no `enum` |
| `set_timeZone` | `/cloud/timeZone` | response has no schema; `timeZone` format |
| `set_refreshCertificate` | `/cloud/certificates/{certname}` | `type` no `enum`; response no schema |
| `del_certificate` | `/cloud/certificates/{certname}` | `type` body vs query; response no schema |
| `set_eSimConfig` | `/cloud/eSimConfig` | `operation` no `enum`; boolean-as-string |
| `set_hostName` | `/cloud/hostName` | `hostname` vs `hostName` |
| `set_revertbackOS` | `/cloud/revertbackOS` | response has no schema |
| `set_dataToRG` | `/cloud/setdataToRG` | no request body defined |
| `set_reqToUserapp` | `/cloud/apps/{appname}/pass-through` | response object untyped |
| `set_startUserapp` / `set_stopUserapp` / `set_autostartUserapp` / `set_uninstallUserapp` | `/cloud/apps/{appname}/...` | responses have no schema; `autostart` no description |

## Commands reviewed — no scenario needed

Already well documented (descriptions, `enum`s, examples, response schemas):
`set_impinjGen2X`, `set_config`, `set_importCloudConfig`, `updateNetwork`, `set_bleConfig`, `set_ntpServer`.
