# FXR90 REST Endpoint Summary

Reference for **32 PUT** endpoints, **1 parameterized GET**, and **1 parameterized DELETE** (from `FXR90-rest-api.yaml`).

Swagger UI: https://immanuel2504.github.io/FX90/RestAPI/swagger.html

---

## Verification order (matches Swagger sidebar)

Work top to bottom — same tag order and operation order as the HTML sidebar.

| # | Done | Tag | Method | Path | Operation ID | Param | Sidebar label |
| -: | :--: | --- | ------ | ---- | ------------ | ----- | ------------- |
| 1 | [ ] | Control | PUT | `/cloud/mode` | `setMode` | — | Set Operating Mode |
| 2 | [ ] | Control | PUT | `/cloud/start` | `startInventory` | — | Start Tag Reads |
| 3 | [ ] | Control | PUT | `/cloud/stop` | `stopInventory` | — | Stop Tag Reads |
| 4 | [ ] | Control | PUT | `/cloud/preSelection` | `setPreSelection` | — | Set Pre-Selection |
| 5 | [ ] | ImpinjGen2X | PUT | `/cloud/impinjGen2X` | `setImpinjGen2X` | — | Set Impinj Gen2X Configuration |
| 6 | [ ] | System | PUT | `/cloud/config` | `setConfig` | — | Set Reader Configuration |
| 7 | [ ] | System | PUT | `/cloud/pass-through` | `status` | — | Pass-Through Command |
| 8 | [ ] | System | PUT | `/cloud/cloudConfig` | `setImportCloudConfig` | — | Import Cloud Configuration |
| 9 | [ ] | System | PUT | `/cloud/cableLossCompensation` | `setCableLossCompensation` | — | Set Cable Loss Compensation |
| 10 | [ ] | System | PUT | `/cloud/reboot` | `reboot` | — | Reboot the Reader |
| 11 | [ ] | System | PUT | `/cloud/updatePassword` | `updatePassword` | — | Change Password |
| 12 | [ ] | App-led | PUT | `/cloud/app-led` | `setAppLed` | — | Control LED |
| 13 | [ ] | Gpio | PUT | `/cloud/gpo` | `setGpo` | — | Control GPO |
| 14 | [ ] | Region | PUT | `/cloud/region` | `setRegion` | — | Set Reader Region Configuration |
| 15 | [ ] | Region | GET | `/cloud/supportedStandardList` | `getSupportedStandardList` | query: `region` | Get the Supported Regions standard list |
| 16 | [ ] | Logs | PUT | `/cloud/logs` | `setLogs` | — | Change Log Configuration |
| 17 | [ ] | Date&Time | PUT | `/cloud/timeZone` | `setTimeZone` | — | Set Reader Time Zone |
| 18 | [ ] | Date&Time | PUT | `/cloud/ntpServer` | `updateNtpServer` | — | Set Reader NTP Server |
| 19 | [ ] | Certificate | PUT | `/cloud/certificates` | `setUpdateCertificate` | — | Install Certificate |
| 20 | [ ] | Certificate | PUT | `/cloud/certificates/{certname}` | `setRefreshCertificate` | path: `certname` | Refresh Certificate |
| 21 | [ ] | Network | PUT | `/cloud/network` | `updateNetwork` | — | Set Network Configuration |
| 22 | [ ] | Network | PUT | `/cloud/eSimConfig` | `setEsimConfig` | — | Set eSIM Configuration |
| 23 | [ ] | Network | PUT | `/cloud/hostName` | `setHostName` | — | Set Reader Host Name |
| 24 | [ ] | Firmware | PUT | `/cloud/os` | `setOS` | — | Update Firmware |
| 25 | [ ] | Firmware | PUT | `/cloud/revertbackOS` | `revertBackOS` | — | Revert Back Firmware Update |
| 26 | [ ] | userapp | PUT | `/cloud/apps/install` | `setInstallUserApp` | — | Install User App |
| 27 | [ ] | userapp | PUT | `/cloud/apps/{appname}/start` | `setStartUserApp` | path: `appname` | Start User App |
| 28 | [ ] | userapp | PUT | `/cloud/apps/{appname}/stop` | `setStopUserApp` | path: `appname` | Stop User App |
| 29 | [ ] | userapp | PUT | `/cloud/apps/{appname}/autostart` | `setAutostartUserApp` | path: `appname` | Auto Start User App |
| 30 | [ ] | userapp | PUT | `/cloud/setdataToRG` | `setDataToRG` | — | Set Data to RG |
| 31 | [ ] | userapp | PUT | `/cloud/apps/{appname}/pass-through` | `setReqToUserApp` | path: `appname` | Send Commands to User App |
| 32 | [ ] | userapp | PUT | `/cloud/apps/{appname}/uninstall` | `setUninstallUserApp` | path: `appname` | Uninstall User App |
| 33 | [ ] | Ble | PUT | `/cloud/ble-config` | `setBleConfig` | — | Set BLE Configuration |

**Bonus (parameterized DELETE — verify after Certificate PUTs):**

| # | Done | Tag | Method | Path | Operation ID | Param |
| -: | :--: | --- | ------ | ---- | ------------ | ----- |
| — | [ ] | Certificate | DELETE | `/cloud/certificates/{certname}` | `delCertificate` | path: `certname`, query: `type` |

---

## API Endpoint Summary

| Category                           |  Count | Details                                                          |
| ---------------------------------- | -----: | ---------------------------------------------------------------- |
| **PUT endpoints (total)**          | **32** | Includes all configuration and control operations                |
| PUT endpoints with path parameters |      6 | Require a path variable (`appname` or `certname`)                |
| **GET endpoints with parameters**  |  **1** | `GET /cloud/supportedStandardList`                               |
| GET endpoints without parameters   |     32 | No query or path parameters defined in the OpenAPI specification |

---

## GET Endpoint with Parameters

| Method | Path                           | Operation ID               | Parameter | In    | Required | Description                                                                       |
| ------ | ------------------------------ | -------------------------- | --------- | ----- | -------- | --------------------------------------------------------------------------------- |
| GET    | `/cloud/supportedStandardList` | `getSupportedStandardList` | `region`  | Query | No       | Returns supported standard channels. If provided, filters the response by region. |

---

## PUT Endpoints

|  # | Path                                 | Operation ID               | Path Parameter |
| -: | ------------------------------------ | -------------------------- | -------------- |
|  1 | `/cloud/app-led`                     | `setAppLed`                | —              |
|  2 | `/cloud/apps/install`                | `setInstallUserApp`        | —              |
|  3 | `/cloud/apps/{appname}/autostart`    | `setAutostartUserApp`      | `appname`      |
|  4 | `/cloud/apps/{appname}/pass-through` | `setReqToUserApp`          | `appname`      |
|  5 | `/cloud/apps/{appname}/start`        | `setStartUserApp`          | `appname`      |
|  6 | `/cloud/apps/{appname}/stop`         | `setStopUserApp`           | `appname`      |
|  7 | `/cloud/apps/{appname}/uninstall`    | `setUninstallUserApp`      | `appname`      |
|  8 | `/cloud/ble-config`                  | `setBleConfig`             | —              |
|  9 | `/cloud/cableLossCompensation`       | `setCableLossCompensation` | —              |
| 10 | `/cloud/certificates`                | `setUpdateCertificate`     | —              |
| 11 | `/cloud/certificates/{certname}`     | `setRefreshCertificate`    | `certname`     |
| 12 | `/cloud/cloudConfig`                 | `setImportCloudConfig`     | —              |
| 13 | `/cloud/config`                      | `setConfig`                | —              |
| 14 | `/cloud/eSimConfig`                  | `setEsimConfig`            | —              |
| 15 | `/cloud/gpo`                         | `setGpo`                   | —              |
| 16 | `/cloud/hostName`                    | `setHostName`              | —              |
| 17 | `/cloud/impinjGen2X`                 | `setImpinjGen2X`           | —              |
| 18 | `/cloud/logs`                        | `setLogs`                  | —              |
| 19 | `/cloud/mode`                        | `setMode`                  | —              |
| 20 | `/cloud/network`                     | `updateNetwork`            | —              |
| 21 | `/cloud/ntpServer`                   | `updateNtpServer`          | —              |
| 22 | `/cloud/os`                          | `setOS`                    | —              |
| 23 | `/cloud/pass-through`                | `status`                   | —              |
| 24 | `/cloud/preSelection`                | `setPreSelection`          | —              |
| 25 | `/cloud/reboot`                      | `reboot`                   | —              |
| 26 | `/cloud/region`                      | `setRegion`                | —              |
| 27 | `/cloud/revertbackOS`                | `revertBackOS`             | —              |
| 28 | `/cloud/setdataToRG`                 | `setDataToRG`              | —              |
| 29 | `/cloud/start`                       | `startInventory`           | —              |
| 30 | `/cloud/stop`                        | `stopInventory`            | —              |
| 31 | `/cloud/timeZone`                    | `setTimeZone`              | —              |
| 32 | `/cloud/updatePassword`              | `updatePassword`           | —              |

---

## PUT Endpoints with Path Parameters

| Method | Path                                 | Operation ID            | Path Parameter |
| ------ | ------------------------------------ | ----------------------- | -------------- |
| PUT    | `/cloud/apps/{appname}/autostart`    | `setAutostartUserApp`   | `appname`      |
| PUT    | `/cloud/apps/{appname}/pass-through` | `setReqToUserApp`       | `appname`      |
| PUT    | `/cloud/apps/{appname}/start`        | `setStartUserApp`       | `appname`      |
| PUT    | `/cloud/apps/{appname}/stop`         | `setStopUserApp`        | `appname`      |
| PUT    | `/cloud/apps/{appname}/uninstall`    | `setUninstallUserApp`   | `appname`      |
| PUT    | `/cloud/certificates/{certname}`     | `setRefreshCertificate` | `certname`     |

---

## DELETE Endpoint with Parameters

| Method | Path                             | Operation ID      | Parameter  | In    | Required |
| ------ | -------------------------------- | ----------------- | ---------- | ----- | -------- |
| DELETE | `/cloud/certificates/{certname}` | `delCertificate`  | `certname` | Path  | Yes      |
|        |                                  |                   | `type`     | Query | Yes      |
