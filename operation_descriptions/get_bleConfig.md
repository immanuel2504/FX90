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
