## Description

The `start` command starts RFID inventory, BLE scanning, or both at the same time.

By default, if `payload` is empty or `scanType` is not provided, the reader starts RFID inventory only. Use `scanType` when you need to explicitly start BLE, RFID, or both.

Use this command to:

- Start RFID inventory after configuring the reader mode with `set_mode`
- Start BLE scanning after configuring BLE with `set_bleConfig`
- Start RFID and BLE together for mixed tag/beacon workflows
- Apply a previously saved Impinj Gen2X configuration when starting RFID

## Command Details

| Property | Value |
|---|---|
| Pattern Name | RFID/BLE Scan Control - Start |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [stop](stop.md), [set_bleConfig](set_bleConfig.md), [get_bleConfig](get_bleConfig.md), [set_mode](set_mode.md), [get_mode](get_mode.md), [set_impinjGen2X](set_impinjGen2X.md) |
| Supported Operations | Start RFID inventory, BLE scan, or both |
| Supported API Versions | V1.0 |

## Before You Begin

Configure the scan type you plan to start.

| What You Need | Details |
|---|---|
| RFID inventory | Configure inventory behavior with `set_mode` before starting RFID. |
| BLE scanning | Configure BLE first with `set_bleConfig`. |
| Impinj Gen2X | Configure Gen2X first with `set_impinjGen2X`, then start with `applyImpinjGen2X: true`. |
| Reader status | Use `get_status` to confirm the radio is connected and ready. |

## Start Behavior

| Payload | Result |
|---|---|
| `{}` | Starts RFID inventory only. This is the default behavior. |
| `{ "scanType": ["rfid"] }` | Starts RFID inventory explicitly. |
| `{ "scanType": ["ble"] }` | Starts BLE scanning only. |
| `{ "scanType": ["ble", "rfid"] }` | Starts BLE scanning and RFID inventory together. |
| `{ "applyImpinjGen2X": true }` | Starts RFID inventory and applies the saved Impinj Gen2X configuration. |

## Important Rules

- `scanType` may contain `rfid`, `ble`, or both.
- If `scanType` is omitted, the reader defaults to RFID-only.
- BLE scanning requires BLE configuration from `set_bleConfig`.
- `scanType` containing `ble` cannot be combined with `applyImpinjGen2X`.
- `applyImpinjGen2X` is for RFID Gen2X operations, not BLE scanning.
