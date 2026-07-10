## 1. Description

The `PUT /cloud/stop` REST endpoint stops RFID inventory, BLE scanning, or both.

By default, if the request body is empty or `scanType` is not provided, the reader stops RFID inventory only. Use `scanType` when you need to stop BLE separately or stop both scan types together.

Use this endpoint to:

- Stop an active RFID inventory cycle
- Stop BLE scanning without stopping RFID
- Stop both BLE and RFID before changing configuration
- Return the reader to an idle state before changing mode or BLE settings

## 2. Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | Scan Control - Stop |
| REST Endpoint | `PUT /cloud/stop` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |
| Related Endpoints | [startInventory](startInventory.md), [setBleConfig](setBleConfig.md), [getBleConfig](getBleConfig.md), [getMode](getMode.md), [getStatus](getStatus.md) |
| Supported Operations | Stop RFID inventory, BLE scan, or both |
| Supported API Versions | V1.0 |

## 3. Stop Behavior

| Request Body | Result |
|---|---|
| `{}` | Stops RFID inventory only. This is the default behavior. |
| `{ "scanType": ["rfid"] }` | Stops RFID inventory explicitly. BLE scanning continues if active. |
| `{ "scanType": ["ble"] }` | Stops BLE scanning only. RFID inventory continues if active. |
| `{ "scanType": ["ble", "rfid"] }` | Stops both BLE scanning and RFID inventory. |

## 4. Before You Begin

Stopping a scan type that is already idle may still succeed or may return failure depending on the reader state. If you need to know the current state first, check `GET /cloud/status`.

| What You Need | Details |
|---|---|
| Current activity | Optional. Check `GET /cloud/status` if you need to confirm RFID or BLE activity before stopping. |
| Target scan type | Choose `rfid`, `ble`, or both in `scanType`. Omit `scanType` only when you want the default RFID stop behavior. |
