The `start` MQTT command starts RFID inventory, BLE scanning, or both on the FXR90 reader.

By default, an empty payload starts RFID inventory only. Use the `scanType` field to explicitly start BLE, RFID, or both together. Optional flags allow you to apply a previously saved Impinj Gen2X configuration or control whether the start state persists across reboots.

**Use this command to:**

- Start RFID inventory using the currently configured operating mode
- Start BLE scanning using the currently configured BLE settings
- Start RFID and BLE scanning together in a single inventory session
- Apply a previously saved Impinj Gen2X configuration when starting RFID inventory
- Control whether the reader automatically resumes scanning after reboot

### Command Details

| Property | Value |
|---|---|
| Pattern Name | Scan Control - Start |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 Series |
| MQTT Command | `start` |
| REST Endpoint | `PUT /cloud/start` |
| Related Commands | `stop`, `set_bleConfig`, `set_impinjGen2X`, `set_mode` |
| Supported Scan Types | `rfid`, `ble`, or both combined |

---

## 2. Before You Begin

Make sure the relevant scanners are configured before publishing this command.

| What You Need | Details |
|---|---|
| MQTT connectivity | The reader must be connected to the MQTT broker and subscribed to its command topic. |
| RFID configuration | Operating mode must be configured via `set_mode` (or default) before starting RFID inventory. |
| BLE configuration | If starting BLE, the BLE scanner must be configured via `set_bleConfig` with `ble.enable: true`. |
| Gen2X configuration | If using `applyImpinjGen2X: true`, the Gen2X configuration must be saved via `set_impinjGen2X` beforehand. |

---

## 3. What Happens After Start

Once the `start` command succeeds, the reader transitions from **Idle** to **Running**. Two important behaviors govern the running session.

### Scan Type

The `scanType` field determines which scanners run and where the data is published.

| Scan Type | Behavior |
|---|---|
| `rfid` (default) | Starts RFID inventory only. Tag read events stream on the reader's RFID data topic. |
| `ble` | Starts BLE scanning only. BLE advertisement events stream on the reader's BLE data topic. |
| `["ble", "rfid"]` | Starts both scanners in a single session. RFID and BLE events stream independently on their respective data topics. |

### Persistence Across Reboots

The `doNotPersistState` field controls whether the reader resumes scanning automatically after a reboot or MQTT reconnect.

| `doNotPersistState` | Behavior on Reboot or Reconnect |
|---|---|
| `false` (default) | The reader **remembers the running state** and automatically resumes scanning. |
| `true` | The running state is **not saved**. The reader stays Idle until `start` is published again. |

> Tip: Use `doNotPersistState: true` for one-time or debugging sessions where automatic resume after reboot is not desired.

---

## 4. Rules and Constraints

### Command Envelope

- `command` must be exactly `start`.
- `command_id` must be a unique, non-empty string.
- `payload` must be present; it may be empty (`{}`).

### Field-Level Rules

- `scanType` - array of strings. Allowed values: `"rfid"`, `"ble"`.
- `applyImpinjGen2X` - boolean.
- `doNotPersistState` - boolean.

### Inventory State

- Only one inventory session may be active at a time.
