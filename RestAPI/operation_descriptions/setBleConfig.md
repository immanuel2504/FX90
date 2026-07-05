The `PUT /cloud/ble-config` REST endpoint and the `set_bleConfig` MQTT command configure BLE scanning on the reader.

Use this operation to:
- Enable or disable BLE scanning
- Set the scan interval
- Filter beacons by RSSI, service UUID, address, or beacon protocol fields
- Configure iBeacon, AltBeacon, Eddystone, and generic BLE filters

## 1. Operation Details

| Property | Value |
|---|---|
| Pattern Name | BLE Configuration Update |
| Supported Protocols | REST (HTTP/HTTPS), MQTT |
| Applies To | FXR90 |
| Related Operations | `getBleConfig`, `startInventory`, `stopInventory` |
| REST Endpoint | `PUT /cloud/ble-config` |

## 2. Before You Begin

BLE configuration must be applied before starting a BLE scan. After saving configuration, use `PUT /cloud/start` with `scanType: ["ble"]` or `scanType: ["ble", "rfid"]`.

| Field | Notes |
|---|---|
| `ble.enable` | Required. Set to `true` to enable BLE scanning or `false` to disable it. |
| `ble.scanIntervalSec` | Optional scan interval in seconds. |
| `ble.additionalFilters.rssi` | Optional minimum RSSI filter. |
| `ble.protocols` | Optional protocol-specific filters for iBeacon, AltBeacon, Eddystone, or generic BLE advertisements. |
