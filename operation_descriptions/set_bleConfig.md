## Description

The `set_bleConfig` command configures the Bluetooth Low Energy scanner on the reader.

Use this command to:

- Enable or disable BLE scanning
- Set the BLE scan interval
- Filter BLE advertisements by RSSI or service UUID
- Configure protocol-specific filters for iBeacon, AltBeacon, Eddystone, and generic BLE devices

## Command Details

| Property | Value |
|---|---|
| Pattern Name | BLE Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_bleConfig](get_bleConfig.md), [start](start.md), [stop](stop.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Configure BLE scanner behavior |
| Supported API Versions | V1.0 |

## Before You Begin

Configure BLE before starting a BLE scan. After applying this command, use `start` with `scanType: ["ble"]` or `scanType: ["ble", "rfid"]`.

## Request Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `payload.ble` | object | Yes | BLE scanner configuration object. |
| `payload.ble.enable` | boolean | Yes | Enables or disables BLE scanning. |
| `payload.ble.scanIntervalSec` | integer | No | BLE scan interval in seconds. |
| `payload.ble.additionalFilters.rssi` | integer | No | Minimum RSSI threshold. |
| `payload.ble.additionalFilters.serviceUuids16` | array of strings | No | 16-bit service UUID filters. |
| `payload.ble.additionalFilters.serviceUuids128` | array of strings | No | 128-bit service UUID filters. |
| `payload.ble.protocols.iBeacon` | object | No | iBeacon scanner settings and filters. |
| `payload.ble.protocols.altBeacon` | object | No | AltBeacon scanner settings and filters. |
| `payload.ble.protocols.eddystone` | object | No | Eddystone scanner settings and filters. |
| `payload.ble.protocols.generic` | object | No | Generic BLE advertisement settings and filters. |
