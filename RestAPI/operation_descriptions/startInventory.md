The `PUT /cloud/start` REST endpoint starts RFID inventory, BLE scanning, or both on the FXR90 reader.

By default, an empty request body starts RFID inventory only. Use the `scanType` field to explicitly start BLE, RFID, or both together. Optional flags allow you to apply a previously saved Impinj Gen2X configuration or control whether the start state persists across reboots.

### Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | Scan Control - Start |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 Series |
| Related Endpoints | `PUT /cloud/stop`, `PUT /cloud/ble-config`, `PUT /cloud/impinjGen2X`, `PUT /cloud/mode` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |
| Supported Scan Types | `rfid`, `ble`, or both combined |

---

## 2. Before You Begin

Make sure the relevant scanners are configured before sending this request.

| What You Need | Details |
|---|---|
| Authentication | Obtain a valid bearer token and include it in the `Authorization` header of every request. |
| Network reachability | The reader's HTTPS endpoint must be reachable from your client. |
| RFID configuration | Operating mode must be configured via `PUT /cloud/mode` (or default) before starting RFID inventory. |
| BLE configuration | If starting BLE, the BLE scanner must be configured via `PUT /cloud/ble-config` with `ble.enable: true`. |
| Gen2X configuration | If using `applyImpinjGen2X: true`, the Gen2X configuration must be saved via `PUT /cloud/impinjGen2X` beforehand. |

---

## 3. What Happens After Start

Once the `PUT /cloud/start` request succeeds, the reader transitions from **Idle** to **Running**. Two important behaviors govern the running session.

### Scan Type

The `scanType` field determines which scanners run and where the data is published.

| Scan Type | Behavior |
|---|---|
| `rfid` (default) | Starts RFID inventory only. Tag read events stream on the reader's RFID data topic. |
| `ble` | Starts BLE scanning only. BLE advertisement events stream on the reader's BLE data topic. |
| `["ble", "rfid"]` | Starts both scanners in a single session. RFID and BLE events stream independently on their respective data topics. |

### Persistence Across Reboots

The `doNotPersistState` field controls whether the reader resumes scanning automatically after a reboot or reconnect.

| `doNotPersistState` | Behavior on Reboot or Reconnect |
|---|---|
| `false` (default) | The reader **remembers the running state** and automatically resumes scanning. |
| `true` | The running state is **not saved**. The reader stays Idle until `PUT /cloud/start` is called again. |

> Tip: Use `doNotPersistState: true` for one-time or debugging sessions where automatic resume after reboot is not desired.

---
