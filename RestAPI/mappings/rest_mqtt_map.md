# REST ↔ MQTT mapping

Generated from `RestAPI/FXR90.yaml`, `RestAPI/paths/`, and `tag_config.json`.
Regenerate: `python scripts/generate_rest_mqtt_map.py`

## Summary

| Metric | Count |
|--------|------:|
| REST HTTP operations | 68 |
| MQTT operations (total) | 80 |
| Matched (REST has MQTT equivalent) | 67 |
| MQTT-only | 13 (0 commands, 13 events) |

## REST → MQTT (all 68 operations)

| Tag | Method | REST path | MQTT command | operationId |
|-----|--------|-----------|--------------|-------------|
| App-led | GET | `/cloud/app-led` | `get_appled` | getAppLed |
| App-led | PUT | `/cloud/app-led` | `set_appled` | setAppLed |
| userapp | GET | `/cloud/apps` | `get_user_apps` | getUserApps |
| userapp | PUT | `/cloud/apps/install` | `install_user_app` | setInstallUserApp |
| userapp | PUT | `/cloud/apps/{appname}/autostart` | `autostart_user_app` | setAutostartUserApp |
| userapp | PUT | `/cloud/apps/{appname}/pass-through` | `set_req_usr_app` | setReqToUserApp |
| userapp | PUT | `/cloud/apps/{appname}/start` | `start_user_app` | setStartUserApp |
| userapp | PUT | `/cloud/apps/{appname}/stop` | `stop_user_app` | setStopUserApp |
| userapp | PUT | `/cloud/apps/{appname}/uninstall` | `uninstall-user-app` | setUninstallUserApp |
| Ble | GET | `/cloud/ble-config` | `get_bleConfig` | getBleConfig |
| Ble | PUT | `/cloud/ble-config` | `set_bleConfig` | setBleConfig |
| System | GET | `/cloud/cableLossCompensation` | `get_cableLossCompensation` | getCableLossCompensation |
| System | PUT | `/cloud/cableLossCompensation` | `set_cableLossCompensation` | setCableLossCompensation |
| Certificate | GET | `/cloud/certificates` | `get_certs` | getCertificates |
| Certificate | PUT | `/cloud/certificates` | `set_update_cert` | setUpdateCertificate |
| Certificate | DELETE | `/cloud/certificates/{certname}` | `del_certs` | delCertificate |
| Certificate | PUT | `/cloud/certificates/{certname}` | `refresh-cert` | setRefreshCertificate |
| System | PUT | `/cloud/cloudConfig` | `set_importCloudConfig` | setImportCloudConfig |
| System | GET | `/cloud/config` | `get_config` | getConfig |
| System | PUT | `/cloud/config` | `set_config` | setConfig |
| Network | GET | `/cloud/eSimConfig` | `get_eSimConfig` | getEsimConfig |
| Network | PUT | `/cloud/eSimConfig` | `set_eSimConfig` | setEsimConfig |
| Gpio | GET | `/cloud/gpi` | `get_gpi_status` | getGpiStatus |
| Gpio | GET | `/cloud/gpo` | `get_gpostatus` | getGpoStatus |
| Gpio | PUT | `/cloud/gpo` | `set_gpo` | setGpo |
| Network | GET | `/cloud/hostName` | `get_hostname` | getHostName |
| Network | PUT | `/cloud/hostName` | `set_hostname` | setHostName |
| ImpinjGen2X | GET | `/cloud/impinjGen2X` | `get_impinjGen2X` | getImpinjGen2X |
| ImpinjGen2X | PUT | `/cloud/impinjGen2X` | `set_impinjGen2X` | setImpinjGen2X |
| Login | GET | `/cloud/localRestLogin` | `localrest_login` | localRestLogin |
| Logs | GET | `/cloud/logs` | `get_logs` | getLogs |
| Logs | PUT | `/cloud/logs` | `set_logs` | setLogs |
| Logs | GET | `/cloud/logs/RcLog` | `get_rc_log` | getRcLog |
| Logs | GET | `/cloud/logs/RgErrorLog` | `get_rg_error_logs` | getRgErrorLog |
| Logs | GET | `/cloud/logs/RgWarningLog` | `get_rg_warn_logs` | getRgWarningLog |
| Logs | DELETE | `/cloud/logs/radioPacketLog` | `del_radio_pkt_logs` | delRadioPacketLog |
| Logs | GET | `/cloud/logs/radioPacketLog` | `get_radio_pkt_logs` | getRadioPacketLog |
| Logs | DELETE | `/cloud/logs/syslog` | `del_syslogs` | delLogsSyslog |
| Logs | GET | `/cloud/logs/syslog` | `get_logs_syslog` | getLogsSyslog |
| Control | GET | `/cloud/mode` | `get_mode` | getMode |
| Control | PUT | `/cloud/mode` | `set_mode` | setMode |
| Network | GET | `/cloud/network` | `get_network` | getNetwork |
| Network | PUT | `/cloud/network` | `set_network` | updateNetwork |
| Network | GET | `/cloud/networkInterfaces` | `get_networkInterfaces` | getNetworkInterfaces |
| Date&Time | GET | `/cloud/ntpServer` | `get_ntpServer` | getNtpServer |
| Date&Time | PUT | `/cloud/ntpServer` | `set_ntpServer` | updateNtpServer |
| Firmware | PUT | `/cloud/os` | `set_os` | setOS |
| System | PUT | `/cloud/pass-through` | `set_passthru` | status |
| Control | GET | `/cloud/preSelection` | `get_preSelection` | getPreSelection |
| Control | PUT | `/cloud/preSelection` | `set_preSelection` | setPreSelection |
| Network | GET | `/cloud/readPoints` | `get_readPoints` | getReadPoints |
| System | GET | `/cloud/readerCapabilities` | `get_readerCapabilities` | getReaderCapabilities |
| Network | GET | `/cloud/readerLocation` | `get_gpsCoordinates` | getGpsCoordinates |
| System | PUT | `/cloud/reboot` | `reboot` | reboot |
| Region | GET | `/cloud/region` | `get_region` | getRegion |
| Region | PUT | `/cloud/region` | `set_region` | setRegion |
| Firmware | PUT | `/cloud/revertbackOS` | `revertback` | revertBackOS |
| userapp | PUT | `/cloud/setdataToRG` | `set_dataToRG` | setDataToRG |
| Control | PUT | `/cloud/start` | `start` | startInventory |
| System | GET | `/cloud/status` | `get_status` | getStatus |
| Control | PUT | `/cloud/stop` | `stop` | stopInventory |
| Region | GET | `/cloud/supportedRegionList` | `get_SupportedRegionList` | getSupportedRegionList |
| Region | GET | `/cloud/supportedStandardList` | `get_supportedStandardList` | getSupportedStandardList |
| Date&Time | GET | `/cloud/timeZone` | `get_timeZone` | getTimeZone |
| Date&Time | PUT | `/cloud/timeZone` | `set_timeZone` | setTimeZone |
| System | PUT | `/cloud/updatePassword` | `set_password` | updatePassword |
| System | GET | `/cloud/version` | `get_version` | getVersion |
| Network | GET | `/cloud/wifiNetworks` | `get_availableWifiNetworks` | getAvailableWifiNetworks |

## MQTT-only (no REST endpoint in FXR90 paths)

### Commands (0)

| MQTT command | Category |
|--------------|----------|

### Events (13)

| MQTT event | Category |
|------------|----------|
| `async-events` | management-events |
| `error` | management-events |
| `firmwareUpdateProgress` | management-events |
| `gpi` | management-events |
| `gpo` | management-events |
| `heartbeat` | management-events |
| `userapp_event` | management-events |
| `warning` | management-events |
| `directionality_tag_data_events` | tag-data-events |
| `locationHistory` | tag-data-events |
| `mode_tag_data_events` | tag-data-events |
| `tagDataEvents` | tag-data-events |
| `zoneHistory` | tag-data-events |

## REST label aliases

REST path `description` fields use alternate names; normalized to canonical MQTT commands:

| REST label in YAML | Canonical MQTT command |
|--------------------|------------------------|
| `del_certificate` | `del_certs` |
| `del_logs_radioPacketLog` | `del_radio_pkt_logs` |
| `del_logs_syslog` | `del_syslogs` |
| `get_SupportedStandardList` | `get_SupportedStandardlist` |
| `get_certificates` | `get_certs` |
| `get_gpiStatus` | `get_gpi_status` |
| `get_gpoStatus` | `get_gpostatus` |
| `get_hostName` | `get_hostname` |
| `get_logs_radioPacketLog` | `get_radio_pkt_logs` |
| `get_logs_rcLog` | `get_rc_log` |
| `get_logs_rgErrorLog` | `get_rg_error_logs` |
| `get_logs_rgWarningLog` | `get_rg_warn_logs` |
| `get_userapps` | `get_user_apps` |
| `localrestlogin` | `localrest_login` |
| `set_autostartUserapp` | `autostart_user_app` |
| `set_hostName` | `set_hostname` |
| `set_installUserapp` | `install_user_app` |
| `set_refreshCertificate` | `refresh-cert` |
| `set_reqToUserapp` | `set_req_usr_app` |
| `set_revertbackOS` | `revertback` |
| `set_startUserapp` | `start_user_app` |
| `set_stopUserapp` | `stop_user_app` |
| `set_uninstallUserapp` | `uninstall-user-app` |
| `set_updateCertificate` | `set_update_cert` |
