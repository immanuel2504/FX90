The `PUT /cloud/start` REST endpoint and the `start` MQTT command start RFID inventory, BLE scanning, or both.

By default, an empty request starts RFID inventory only. Use `scanType` to explicitly start BLE, RFID, or both.

## 1. Operation Details

| Property | Value |
|---|---|
| Pattern Name | Scan Control - Start |
| Supported Protocols | REST (HTTP/HTTPS), MQTT |
| Applies To | FXR90 |
| Related Operations | `stopInventory`, `setBleConfig`, `setImpinjGen2X`, `setMode` |
| REST Endpoint | `PUT /cloud/start` |
| MQTT Command | `start` |

## 2. Start Behavior

| Payload | Result |
|---|---|
| `{}` | Starts RFID inventory only. |
| `{ "scanType": ["rfid"] }` | Starts RFID inventory explicitly. |
| `{ "scanType": ["ble"] }` | Starts BLE scanning only. |
| `{ "scanType": ["ble", "rfid"] }` | Starts BLE scanning and RFID inventory together. |
| `{ "applyImpinjGen2X": true }` | Starts RFID inventory and applies the saved Impinj Gen2X configuration. |

## 3. Before You Begin

Configure the scan mode before starting:
- RFID inventory should be configured with mode settings.
- BLE scanning requires BLE configuration from `PUT /cloud/ble-config`.
- Gen2X settings must be saved before using `applyImpinjGen2X`.
