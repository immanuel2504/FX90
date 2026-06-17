The `GET /cloud/ble-config` REST endpoint and the `get_bleConfig` MQTT command retrieve the current BLE scanner configuration from the reader.

This operation returns:
- Whether BLE scanning is enabled
- Scan interval settings
- Protocol-specific filters for iBeacon, AltBeacon, Eddystone, and generic BLE advertisements
- Additional RSSI and service UUID filters

## 1. Operation Details

| Property | Value |
|---|---|
| Pattern Name | BLE Configuration Query |
| Supported Protocols | REST (HTTP/HTTPS), MQTT |
| Applies To | FXR90 |
| Related Operations | `setBleConfig`, `startInventory`, `stopInventory` |
| REST Endpoint | `GET /cloud/ble-config` |
| MQTT Command | `get_bleConfig` |

## 2. When to Use This Endpoint

Use this endpoint before starting BLE scans to verify that the reader is configured with the expected scan interval and filters.

| Field | What to Check |
|---|---|
| `ble.enable` | Confirms whether BLE scanning is enabled. |
| `ble.scanIntervalSec` | Confirms how often BLE scan results are collected. |
| `ble.protocols` | Confirms which beacon protocols and filters are active. |
| `additionalFilters` | Confirms RSSI and service UUID filters. |
