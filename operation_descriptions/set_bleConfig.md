## 1. Description

The `set_bleConfig` command sets the BLE (Bluetooth Low Energy) configuration on the reader.

Use it to:

- Enable or configure BLE scanning alongside RFID
- Tune BLE parameters for beacon or tag detection
- Integrate BLE-based workflows with reader operations

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | BLE Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_bleConfig](get_bleConfig.md), [start](start.md), [stop](stop.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Set BLE configuration |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Review current BLE settings with `get_bleConfig` once schemas are available.
