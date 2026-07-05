# FXR90 REST Endpoint Checklist (33 commands)

Quick reference for **32 PUT** endpoints plus **1 GET with a parameter**.
Generated from `FXR90-rest-api.yaml`.

**Auth:** all endpoints below require **Bearer token** unless noted otherwise.

## Legend

| Column | Meaning |
|---|---|
| **Tier** | `simple` = small/trivial body · `moderate` = few fields or path param · `complex` = large/nested schema or long workflow docs |
| **Read schema first** | Open the Swagger request schema and examples before calling |
| **Required fields** | Top-level JSON fields marked required in OpenAPI (nested objects may contain additional required fields) |

## Summary

| Tier | Count |
|---|---:|
| Simple | 11 |
| Moderate | 10 |
| Complex | 12 |
| **Total** | **33** |

## Full checklist

| # | Method | Path | Operation ID | Tier | Read schema first | Params | Body | Required fields (top-level) | Optional fields (top-level) | Nested objects |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | PUT | `/cloud/app-led` | `setAppLed` | moderate | No | — | Optional JSON (`setAppledRequest`) | *(none at top level)* | `color`, `flash`, `seconds` | — |
| 2 | PUT | `/cloud/apps/install` | `setInstallUserApp` | moderate | No | — | Optional JSON (`setInstalluserappRequest`) | *(none at top level)* | `authenticationOptions`, `authenticationType`, `filename`, `url` | `authenticationOptions` |
| 3 | PUT | `/cloud/apps/{appname}/autostart` | `setAutostartUserApp` | moderate | No | `appname` (path, required) | Optional JSON (`setAutostartuserappRequest`) | `autostart` | `appname` | — |
| 4 | PUT | `/cloud/apps/{appname}/pass-through` | `setReqToUserApp` | complex | Yes | `appname` (path, required) | Optional JSON (`setReqtouserappRequest`) | `userapp` | `command` | `command` |
| 5 | PUT | `/cloud/apps/{appname}/start` | `setStartUserApp` | moderate | No | `appname` (path, required) | Optional JSON (`setStartuserappRequest`) | *(none at top level)* | `appname` | — |
| 6 | PUT | `/cloud/apps/{appname}/stop` | `setStopUserApp` | moderate | No | `appname` (path, required) | Optional JSON (`setStopuserappRequest`) | *(none at top level)* | `appname` | — |
| 7 | PUT | `/cloud/apps/{appname}/uninstall` | `setUninstallUserApp` | moderate | No | `appname` (path, required) | Optional JSON (`setUninstalluserappRequest`) | *(none at top level)* | `appname` | — |
| 8 | PUT | `/cloud/ble-config` | `setBleConfig` | complex | Yes | — | Required JSON (`setBleConfigRequest`) | `ble` | *(none at top level)* | `ble` |
| 9 | PUT | `/cloud/cableLossCompensation` | `setCableLossCompensation` | complex | Yes | — | Optional JSON (`setCablelosscompensationRequest`) | *(none at top level)* | `1`, `2`, `3`, `4` | `1`, `2`, `3`, `4` |
| 10 | PUT | `/cloud/certificates` | `setUpdateCertificate` | complex | Yes | — | Optional JSON (`setUpdatecertificateRequest`) | `name`, `type`, `url` | `authenticationOptions`, `authenticationType`, `pfxPassword` | `authenticationOptions` |
| 11 | PUT | `/cloud/certificates/{certname}` | `setRefreshCertificate` | moderate | No | `certname` (path, required) | Optional JSON (`setRefreshcertificateRequest`) | *(none at top level)* | `name`, `type` | — |
| 12 | PUT | `/cloud/cloudConfig` | `setImportCloudConfig` | complex | Yes | — | Required JSON (`setImportcloudconfigRequest`) | `endpointConfig` | *(none at top level)* | `endpointConfig` |
| 13 | PUT | `/cloud/config` | `setConfig` | complex | Yes | — | Optional JSON (`setConfigMqttRequest`) | *(none at top level)* | `xml`, `GPIO-LED`, `READER-GATEWAY` | `GPIO-LED`, `READER-GATEWAY` |
| 14 | PUT | `/cloud/eSimConfig` | `setEsimConfig` | simple | No | — | Optional JSON (`setEsimConfigRequest`) | *(none at top level)* | `operation`, `profileNickName` | — |
| 15 | PUT | `/cloud/gpo` | `setGpo` | simple | No | — | Optional JSON (`setGpoRequest`) | `port`, `state` | *(none at top level)* | — |
| 16 | PUT | `/cloud/hostName` | `setHostName` | simple | No | — | Optional JSON (`setHostNameRequest`) | *(none at top level)* | `hostname` | — |
| 17 | PUT | `/cloud/impinjGen2X` | `setImpinjGen2X` | complex | Yes | — | Required JSON (`setImpinjGen2XRequest`) | *(none at top level)* | `fastID`, `tagProtect`, `tagFocus`, `tagQuieting` | `fastID`, `tagFocus`, `tagQuieting` |
| 18 | PUT | `/cloud/logs` | `setLogs` | moderate | No | — | Optional JSON (`setLogsRequest`) | *(none at top level)* | `components`, `radioPacketLog` | `components` |
| 19 | PUT | `/cloud/mode` | `setMode` | complex | Yes | — | Optional JSON (`operatingMode.v1`) | `type` | `modeSpecificSettings`, `environment`, `antennas`, `filter`, `transmitPower`, `antennaStopCondition`, `query`, `selects`, `delayAfterSelects`, `accesses`, `delayBetweenAntennaCycles`, `tagMetaData`, `radioStartConditions`, `radioStopConditions`, `reportFilter`, `rssiFilter`, `beams` | `antennas`, `filter`, `delayBetweenAntennaCycles`, `tagMetaData`, `radioStartConditions`, `radioStopConditions`, `reportFilter`, `rssiFilter`, `beams` |
| 20 | PUT | `/cloud/network` | `updateNetwork` | complex | Yes | — | Optional JSON (`updateNetworkRequest`) | *(none at top level)* | `eth0`, `mlan0`, `bnep0`, `wan0`, `uap0` | `eth0`, `mlan0`, `bnep0`, `wan0`, `uap0` |
| 21 | PUT | `/cloud/ntpServer` | `updateNtpServer` | simple | No | — | Optional JSON (`updateNtpServerRequest`) | *(none at top level)* | *(none at top level)* | — |
| 22 | PUT | `/cloud/os` | `setOS` | moderate | No | — | Optional JSON (`setOsRequest`) | *(none at top level)* | `authenticationType`, `options`, `url` | `options` |
| 23 | PUT | `/cloud/pass-through` | `status` | simple | No | — | Optional JSON (`statusRequest`) | *(none at top level)* | `component`, `payload` | — |
| 24 | PUT | `/cloud/preSelection` | `setPreSelection` | simple | No | — | Optional JSON (`put_preSelectionRequest`) | *(none at top level)* | `preSelection` | — |
| 25 | PUT | `/cloud/reboot` | `reboot` | simple | No | — | No body | — | — | — |
| 26 | PUT | `/cloud/region` | `setRegion` | simple | No | — | Optional JSON (`setRegionRequest`) | `country`, `standardname` | *(none at top level)* | — |
| 27 | PUT | `/cloud/revertbackOS` | `revertBackOS` | simple | No | — | Optional JSON (`setRevertbackosRequest`) | *(none at top level)* | *(none at top level)* | — |
| 28 | PUT | `/cloud/setdataToRG` | `setDataToRG` | simple | No | — | No body | — | — | — |
| 29 | PUT | `/cloud/start` | `startInventory` | complex | Yes | — | Optional JSON (`startInventoryRequest`) | *(none at top level)* | `scanType`, `doNotPersistState`, `applyImpinjGen2X` | `scanType` |
| 30 | PUT | `/cloud/stop` | `stopInventory` | complex | Yes | — | Optional JSON (`stopInventoryRequest`) | *(none at top level)* | `scanType` | `scanType` |
| 31 | GET | `/cloud/supportedStandardList` | `getSupportedStandardList` | complex | Yes | `region` (query, optional) | No body | — | — | — |
| 32 | PUT | `/cloud/timeZone` | `setTimeZone` | simple | No | — | Optional JSON (`setTimezoneRequest`) | *(none at top level)* | `timeZone` | — |
| 33 | PUT | `/cloud/updatePassword` | `updatePassword` | moderate | No | — | Optional JSON (`put_updatePasswordRequest`) | *(none at top level)* | `currentPassword`, `newPassword`, `userName` | — |

## Complex endpoints — read schema first

These 12 endpoints have the largest schemas or multi-step behavior. Always expand the request model in Swagger UI before calling:

- **PUT `/cloud/apps/{appname}/pass-through`** (`setReqToUserApp`) — Send Request to Userapp
- **PUT `/cloud/ble-config`** (`setBleConfig`) — Set BLE configuration
- **PUT `/cloud/cableLossCompensation`** (`setCableLossCompensation`) — Sets the cableLossCompensation
- **PUT `/cloud/certificates`** (`setUpdateCertificate`) — Install certificate
- **PUT `/cloud/cloudConfig`** (`setImportCloudConfig`) — Import cloud endpoint configuration
- **PUT `/cloud/config`** (`setConfig`) — Updates reader configuration
- **PUT `/cloud/impinjGen2X`** (`setImpinjGen2X`) — Set Impinj Gen2X configuration
- **PUT `/cloud/mode`** (`setMode`) — Updates the reader's operating mode
- **PUT `/cloud/network`** (`updateNetwork`) — Updates reader network configuration
- **PUT `/cloud/start`** (`startInventory`) — Start RFID Inventory or BLE scan
- **PUT `/cloud/stop`** (`stopInventory`) — Stop RFID Inventory or BLE scan
- **GET `/cloud/supportedStandardList`** (`getSupportedStandardList`) — Retrieves the standard channels of the supported regions

## Simple endpoints — quick calls

Safe starting points for integration testing (still send valid JSON where a body exists):

- **PUT `/cloud/eSimConfig`** (`setEsimConfig`) — Sets the eSIM configuration
- **PUT `/cloud/gpo`** (`setGpo`) — Updates GPO port state
- **PUT `/cloud/hostName`** (`setHostName`) — Sets reader hostname
- **PUT `/cloud/ntpServer`** (`updateNtpServer`) — Set NTP server
- **PUT `/cloud/pass-through`** (`status`) — Pass-through command
- **PUT `/cloud/preSelection`** (`setPreSelection`) — Enables or disables the rxSawFilter
- **PUT `/cloud/reboot`** (`reboot`) — Restarts reader
- **PUT `/cloud/region`** (`setRegion`) — Update region information
- **PUT `/cloud/revertbackOS`** (`revertBackOS`) — Revert to previous OS version
- **PUT `/cloud/setdataToRG`** (`setDataToRG`) — Trigger reader gateway data delivery
- **PUT `/cloud/timeZone`** (`setTimeZone`) — Sets the timezone
