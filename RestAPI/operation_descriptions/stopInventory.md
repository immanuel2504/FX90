The `PUT /cloud/stop` REST endpoint and the `stop` MQTT command stop RFID inventory, BLE scanning, or both.

By default, an empty request stops RFID inventory only. Use `scanType` to explicitly stop BLE, RFID, or both.

## 1. Operation Details

| Property | Value |
|---|---|
| Pattern Name | Scan Control - Stop |
| Supported Protocols | REST (HTTP/HTTPS), MQTT |
| Applies To | FXR90 |
| Related Operations | `startInventory`, `getStatus` |
| REST Endpoint | `PUT /cloud/stop` |
| MQTT Command | `stop` |

## 2. Stop Behavior

| Payload | Result |
|---|---|
| `{}` | Stops RFID inventory only. |
| `{ "scanType": ["rfid"] }` | Stops RFID inventory explicitly. |
| `{ "scanType": ["ble"] }` | Stops BLE scanning only. RFID inventory continues. |
| `{ "scanType": ["ble", "rfid"] }` | Stops BLE scanning and RFID inventory together. |

## 3. When to Use This Endpoint

Use this endpoint when changing operating modes, applying configuration updates, or stopping scans before maintenance. Use `GET /cloud/status` to confirm the resulting radio and BLE activity state.
