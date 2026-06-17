## Description

The `get_bleConfig` command retrieves the current Bluetooth Low Energy scanner configuration.

Use this command to:

- Verify whether BLE scanning is enabled
- Review scan interval and RSSI filtering
- Check iBeacon, AltBeacon, Eddystone, and generic BLE filter settings
- Confirm BLE configuration before sending `start` with `scanType: ["ble"]`

## Command Details

| Property | Value |
|---|---|
| Pattern Name | BLE Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_bleConfig](set_bleConfig.md), [start](start.md), [stop](stop.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Retrieve BLE scanner configuration |
| Supported API Versions | V1.0 |

## Before You Begin

No command payload fields are required. Use the response to confirm BLE settings before starting a BLE scan.

## Response Payload Summary

| Field | Type | Description |
|---|---|---|
| `payload.ble.enable` | boolean | Whether BLE scanning is enabled. |
| `payload.ble.scanIntervalSec` | integer | BLE scan interval in seconds. |
| `payload.ble.additionalFilters.rssi` | integer | Minimum RSSI filter. |
| `payload.ble.additionalFilters.serviceUuids16` | array of strings | 16-bit service UUID filters. |
| `payload.ble.additionalFilters.serviceUuids128` | array of strings | 128-bit service UUID filters. |
| `payload.ble.protocols.iBeacon` | object | iBeacon scanner settings and filters. |
| `payload.ble.protocols.altBeacon` | object | AltBeacon scanner settings and filters. |
| `payload.ble.protocols.eddystone` | object | Eddystone scanner settings and filters. |
| `payload.ble.protocols.generic` | object | Generic BLE advertisement settings and filters. |
