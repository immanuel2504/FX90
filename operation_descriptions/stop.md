## 1. Description

The `stop` command stops RFID inventory, BLE scanning, or both.

By default, if `payload` is empty or `scanType` is not provided, the reader stops RFID inventory only. Use `scanType` when you need to stop BLE separately or stop both scan types together.

Use this command to:

- Stop an active RFID inventory cycle
- Stop BLE scanning without stopping RFID
- Stop both BLE and RFID before changing configuration
- Return the reader to an idle state before changing mode or BLE settings

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Scan Control - Stop |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/stop` |
| Related Commands | [start](start.md), [set_bleConfig](set_bleConfig.md), [get_bleConfig](get_bleConfig.md), [get_mode](get_mode.md), [get_status](get_status.md) |
| Supported Operations | Stop RFID inventory, BLE scan, or both |
| Supported API Versions | V1.0 |

## 3. Stop Behavior

| Payload | Result |
|---|---|
| `{}` | Stops RFID inventory only. This is the default behavior. |
| `{ "scanType": ["rfid"] }` | Stops RFID inventory explicitly. BLE scanning continues if active. |
| `{ "scanType": ["ble"] }` | Stops BLE scanning only. RFID inventory continues if active. |
| `{ "scanType": ["ble", "rfid"] }` | Stops both BLE scanning and RFID inventory. |

## 4. Before You Begin

Stopping a scan type that is already idle may still succeed or may return failure depending on the reader state. If you need to know the current state first, check `get_status` or the heartbeat/radio activity data.

| What You Need | Details |
|---|---|
| Current activity | Optional. Check `get_status` if you need to confirm RFID or BLE activity before stopping. |
| Target scan type | Choose `rfid`, `ble`, or both in `scanType`. Omit `scanType` only when you want the default RFID stop behavior. |
