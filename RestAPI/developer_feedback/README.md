# Developer feedback — OpenAPI schema gaps

Each file in this folder documents schema/documentation gaps found while reviewing a command (or group of related commands) in `openAPISpec.yaml`. The API contract itself is consistent in all cases; these notes are about schema metadata (missing `enum`, missing descriptions, undocumented responses, naming inconsistencies).

## Commands with gaps (one file each)

| Command(s) | Endpoint | Main gap(s) |
|------------|----------|-------------|
| `get_preSelection` / `set_preSelection` | `/cloud/preSelection` | GET value no `enum`; missing descriptions; PUT response no description |
| `get_mode` / `set_mode` | `/cloud/mode` | `type` no `enum`; `environment` missing; nested enums/descriptions (vs `Command Schemas.json`) |
| `get_appled` / `set_appled` | `/cloud/app-led` | `color` no `enum` (differs from `set_stackled`); `status` no `enum`; descriptions |
| `set_gpo` | `/cloud/gpo` | `port` range; descriptions; response description |
| `set_region` | `/cloud/region` | `country`/`standardname` no `enum`/reference; descriptions |
| `get_SupportedStandardList` | `/cloud/supportedStandardList` | `channeldata` vs `channelData`; boolean-as-string; descriptions |
| `set_passthru` | `/cloud/pass-through` | `operationId` is `status`; `component` no `enum`; descriptions |
| `set_cableLossCompensation` | `/cloud/cableLossCompensation` | units/ranges; numbered keys unexplained; response description |
| `reboot` | `/cloud/reboot` | description mentions device ID not in schema; response description |
| `set_password` | `/cloud/updatePassword` | descriptions; no `required`; password rules |
| `set_logs` | `/cloud/logs` | `level`/`componentName` no `enum`; descriptions |
| `set_timeZone` | `/cloud/timeZone` | response has no schema; `timeZone` format |
| `set_updateCertificate` | `/cloud/certificates` | `type` no `enum` (should be client/server/app); no `required` [name,type,url]; response no schema — per `Command Schemas.json` |
| `set_refreshCertificate` | `/cloud/certificates/{certname}` | `type` no `enum`/description; response no schema |
| `del_certificate` | `/cloud/certificates/{certname}` | `type` body vs query; `type` no `enum`; response no schema |
| `set_eSimConfig` | `/cloud/eSimConfig` | `operation` no `enum`; boolean-as-string; response no schema |
| `set_hostName` | `/cloud/hostName` | `hostname` vs `hostName`; descriptions/constraints |
| `set_os` | `/cloud/os` | example `authenticationOptions` but correct is `options` (per `Command Schemas.json`); missing optional fields; response no schema |
| `set_revertbackOS` | `/cloud/revertbackOS` | response no schema |
| `set_installUserapp` | `/cloud/apps/install` | `authenticationOptions` vs `options` mismatch (per `Command Schemas.json`); missing optional fields; no `required` |
| `set_dataToRG` | `/cloud/setdataToRG` | no request body defined despite "sets data" |
| `set_reqToUserapp` | `/cloud/apps/{appname}/pass-through` | descriptions; response object untyped |
| `set_startUserapp` / `set_stopUserapp` / `set_autostartUserapp` / `set_uninstallUserapp` | `/cloud/apps/{appname}/...` | responses have no schema; `autostart` no description |

## Commands reviewed — no gaps found

These were reviewed and are already well documented (descriptions, `enum`s, examples, response schemas), so no feedback file was created:

- `set_impinjGen2X` / `get_impinjGen2X` (`/cloud/impinjGen2X`)
- `set_config` / `get_config` (`/cloud/config`)
- `set_importCloudConfig` (`/cloud/cloudConfig`)
- `updateNetwork` / `get_network` (`/cloud/network`)
- `set_bleConfig` (`/cloud/ble-config`)
- `set_ntpServer` / `get_ntpServer` (`/cloud/ntpServer`) — minor only (GET `server` lacks a description)
