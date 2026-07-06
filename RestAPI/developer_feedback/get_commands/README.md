# Developer feedback — GET (read) endpoints

Each file in this folder documents schema/documentation gaps found while reviewing the **GET (read) commands** in `openAPISpec.yaml`. Every GET endpoint's `200` response was compared against the corresponding MQTT command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal (the Zebra IoTC MQTT documentation) — following the response payload definitions and their `$ref`s to confirm the real fields, enums, and descriptions. The API contract itself is consistent; these notes are about schema metadata (missing `enum`, missing descriptions, under-typed responses, item-type mismatches).

These are the read-side companions to the write/`PUT` feedback in the [parent folder](../README.md) and [`mqtt_verified/`](../mqtt_verified/README.md).

## Commands with gaps (one file each)

| Command | Endpoint | Main gap(s) |
|---------|----------|-------------|
| `get_appled` | `GET /cloud/app-led` | `status` no `enum` (`DEFAULT`, `NOT_DEFAULT`); no description |
| `get_gpiStatus` | `GET /cloud/gpi` | per-port descriptions missing; `required` ports (enums already present) |
| `get_region` | `GET /cloud/region` | `channelData` items `integer` vs MQTT `string`; descriptions; `required` |
| `get_SupportedRegionList` | `GET /cloud/supportedRegionList` | `SupportedRegions` no description; `required` |
| `get_version` | `GET /cloud/version` | `model` no `enum`; descriptions |
| `get_status` | `GET /cloud/status` | `antennas`/`radioActivity`/`radioConnection` no `enum`; descriptions |
| `get_readerCapabilities` | `GET /cloud/readerCapabilities` | under-typed arrays (`antennas`, `externalSerialPort`, `supportedPowerSource`, `networkInterfaces`); enums/descriptions; unrealistic example |
| `get_cableLossCompensation` | `GET /cloud/cableLossCompensation` | numbered keys unexplained; no `minimum`/descriptions; `required` |
| `get_logs` | `GET /cloud/logs` | `componentName`/`level` no `enum`; descriptions |
| `get_timeZone` | `GET /cloud/timeZone` | `timeZone` no `enum`; example `UTC` not in allowed list; description |
| `get_certificates` | `GET /cloud/certificates` | `type` no `enum` (`server`, `client`, `app`); descriptions; `required` |
| `get_availableWifiNetworks` | `GET /cloud/wifiNetworks` | field descriptions missing; `required` |
| `get_networkInterfaces` | `GET /cloud/networkInterfaces` | `availableNetworkInterfaces` no description; `required` |
| `get_userapps` | `GET /cloud/apps` | descriptions; item `required`; `minItems`/`uniqueItems`/`default` |
| `get_hostname` | `GET /cloud/hostName` | `hostName` no description; `required` |
| `get_impinjGen2X` | `GET /cloud/impinjGen2X` | `fastID.tidSelector` missing from schema (present in example + MQTT, enum `TID[0]`–`TID[3]`) |

Concrete request/response walkthroughs for each of the above live in [`scenarios/`](scenarios/README.md).

## Commands reviewed — no gaps found

These GET endpoints were reviewed and already match the Zebra IoTC MQTT documentation (proper typed schema, enums, descriptions, examples), so no feedback file was created:

- `get_config` (`GET /cloud/config`) — richly typed reader configuration; already documented.
- `get_network` (`GET /cloud/network`) — per-interface objects with descriptions and enums (e.g. `securityType`).
- `get_readPoints` (`GET /cloud/readPoints`) — array of strings; matches the MQTT response (which is also a plain string array).
- `get_gpsCoordinates` (`GET /cloud/readerLocation`) — `latitude`/`longitude`/`lastReportedTime` as strings and `satellitesUsed` as integer, matching the MQTT response.
- `get_bleConfig` (`GET /cloud/ble-config`) — full BLE scanner config with descriptions and enums; matches the MQTT response.

## Already covered elsewhere (not duplicated here)

- `get_mode` (`GET /cloud/mode`) — the `get_mode` response reuses the `operatingMode.v1` schema; its gaps are already documented alongside `set_mode` in [`mqtt_verified/set_mode_schema_feedback.md`](../mqtt_verified/set_mode_schema_feedback.md) (that file explicitly covers both `GET /cloud/mode` and `PUT /cloud/mode`).
- `get_preSelection` (`GET /cloud/preSelection`) — see [`../scenarios/get_preSelection_set_preSelection_scenario.md`](../scenarios/get_preSelection_set_preSelection_scenario.md).
- `get_SupportedStandardList` (`GET /cloud/supportedStandardList`) — see [`../get_supportedStandardList_schema_feedback.md`](../get_supportedStandardList_schema_feedback.md).

## Not applicable to FXR90

- `get_stackled` (`GET /cloud/stack-led`) — FXR60-only; not supported on FXR90, so it was skipped.
