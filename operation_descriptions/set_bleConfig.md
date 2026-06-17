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
| Supported Operations | Configure BLE scanner behavior |
| Supported API Versions | V1.0 |

## Before You Begin

Configure BLE before starting a BLE scan. After applying this command, use `start` with `scanType: ["ble"]` or `scanType: ["ble", "rfid"]`.
