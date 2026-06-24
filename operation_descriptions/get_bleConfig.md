## 1. Description

The `get_bleConfig` command retrieves the current Bluetooth Low Energy (BLE) scanner configuration from the reader.

This command returns:

- Whether BLE scanning is enabled
- Scan interval and window settings
- RSSI filtering threshold
- iBeacon, AltBeacon, Eddystone, and generic BLE filter settings

No additional payload fields are required to retrieve the BLE configuration.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | BLE Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/ble-config` |
| Related Commands | [set_bleConfig](set_bleConfig.md), [start](start.md), [stop](stop.md) |
| Supported Operations | Retrieve the current BLE scanner configuration |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_bleConfig` to:

- Verify whether BLE scanning is enabled before issuing a `start` with `scanType: ["ble"]`
- Review scan interval and RSSI filtering settings before changing them
- Confirm iBeacon, AltBeacon, Eddystone, or generic BLE filter configuration
- Verify the effect of a prior `set_bleConfig` call

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `enabled` | Is BLE scanning enabled? | BLE inventory will not start if scanning is disabled. |
| `scanInterval` | What is the configured scan interval? | Determines how frequently the reader actively listens for BLE advertisements. |
| `rssiFilter` | What is the RSSI threshold? | Tags or beacons below the RSSI threshold will be filtered out of the scan results. |
| Beacon type filters | Which beacon types are included in the scan? | Only beacon types that are enabled will appear in BLE tag data events. |
