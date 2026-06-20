The `set_bleConfig` MQTT command configures the Bluetooth Low Energy (BLE) scanner on the FXR90 reader, covering scanner enable/disable, scan interval, RSSI and service UUID filtering, and protocol-specific filters for iBeacon, AltBeacon, Eddystone, and generic BLE devices.

**This command allows you to configure:**

- BLE scanner enable/disable and scan interval
- Cross-protocol filters for RSSI and 16-bit / 128-bit service UUIDs
- iBeacon filters (UUID, major, minor, txPower)
- AltBeacon filters (manufacturer ID, beacon ID, major, minor, reference RSSI)
- Eddystone filters (URL, UID, EID, TLM frame types)
- Generic BLE filters by address, address type, name, or alias

**Use this command to:**

- Activate the BLE scanner before starting a BLE inventory
- Reduce noise by filtering weak or irrelevant BLE advertisements
- Capture only specific beacon types or specific devices
- Combine BLE scanning with RFID scanning in a single inventory session

### Command Details

| Property | Value |
|---|---|
| Pattern Name | BLE Configuration Update |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 Series |
| MQTT Command | `set_bleConfig` |
| Related Commands | `get_bleConfig`, `start`, `stop` |
| Required Request Fields | `command`, `command_id`, `payload.ble.enable` |
| Supported Protocols | iBeacon, AltBeacon, Eddystone, Generic BLE |
| Supported Eddystone Frame Types | `URL`, `UID`, `EID`, `TLM` |
| Supported Address Types (Generic) | `public`, `random` |
| Service UUID Filters | 16-bit (`serviceUuids16`), 128-bit (`serviceUuids128`) |
| RSSI Filter Range | `-127` to `0` (dBm) |
| Scan Interval Range | Minimum `1` second |
| Protocol Coexistence | All four protocols may be configured together (not mutually exclusive) |

---

## 2. Before You Begin

Decide which BLE behavior you need to configure before publishing this command. You can send a minimal payload that only enables BLE (`ble.enable: true`), or a full payload with scan interval, additional filters, and protocol-specific filters.

| What You Need | Details |
|---|---|
| MQTT connectivity | The reader must be connected to the MQTT broker and subscribed to its command topic. Verify connection status before publishing. |
| Enable decision | `ble.enable` is **required**. Set to `true` to activate scanning, or `false` to disable it. |
| Scan interval | Decide how often the reader should collect BLE scan results (`scanIntervalSec`, minimum 1 second). Shorter intervals increase responsiveness; longer intervals reduce data volume. |
| RSSI threshold | If you only want strong-signal beacons, set `additionalFilters.rssi` (range `-127` to `0`). Closer-to-zero values are stronger signals. |
| Service UUID filters | If filtering by advertised services, prepare 16-bit (`serviceUuids16`) and/or 128-bit (`serviceUuids128`) UUID lists. |
| iBeacon details | If filtering iBeacons, prepare `uuid`, `major`, `minor`, and `txPower` values. |
| AltBeacon details | If filtering AltBeacons, prepare `mfgId`, `beaconId`, `major`, `minor`, and `refRssi`. |
| Eddystone details | Decide on frame type (`URL`, `UID`, `EID`, `TLM`) and prepare the corresponding fields (`url`, `namespace` + `instance`, `ephemeralId`, etc.). |
| Generic BLE details | If filtering specific BLE devices, prepare `address`, `addressType` (`public` / `random`), `name`, and/or `alias`. |
| Activation | Saving the configuration does not start scanning. Publish `start` with `scanType: ["ble"]` (or `["ble", "rfid"]`) to begin BLE scanning. |
| Command tracking | Generate a unique `command_id` (UUID recommended) for each request to correlate the response on the reply topic. |

---

## 3. Choosing the Core BLE Settings

The two top-level fields control the scanner itself, independent of protocol filtering.

| Field | What It Controls |
|---|---|
| `ble.enable: true` | Activates the BLE scanner. Required for any other field to take effect. |
| `ble.enable: false` | Disables the BLE scanner. All other fields are ignored. |
| `ble.scanIntervalSec` | Interval in seconds between BLE scan collections. Minimum value is `1`. |

> Important: If `ble.enable` is `false`, all filter and protocol settings are saved but inactive. They will resume only when scanning is re-enabled.

---

## 4. Choosing Cross-Protocol Filters

`additionalFilters` apply **across all protocols** (iBeacon, AltBeacon, Eddystone, Generic). Use them to drop low-signal noise and to pre-filter by advertised services.

| Field | What It Controls | Constraints |
|---|---|---|
| `rssi` | Minimum signal strength (in dBm) for an advertisement to be forwarded. | Integer in range `-127` to `0`. Closer to 0 = stronger signal. |
| `serviceUuids16` | Array of 16-bit service UUIDs the reader should match (e.g., `FEAA`, `FE9B`). | Hex strings, 4 characters each. |
| `serviceUuids128` | Array of 128-bit service UUIDs the reader should match. | Full UUID format (8-4-4-4-12 hex digits). |

> Important: Cross-protocol filters apply on top of any protocol-specific filters. An advertisement must satisfy **both** `additionalFilters` and at least one protocol filter (if protocols are enabled) to be reported.

---

## 5. Choosing Protocol-Specific Filters

Each entry in `ble.protocols` is independent and can be enabled or disabled on its own. All four protocols may coexist; they are **not mutually exclusive**.

### 5.1 iBeacon

| Field | What It Controls |
|---|---|
| `enabled` | Activates iBeacon filtering. |
| `filters[].uuid` | Proximity UUID to match. |
| `filters[].major` | Major value (integer). |
| `filters[].minor` | Minor value (integer). |
| `filters[].txPower` | Calibrated RSSI at 1 meter (dBm), used for distance estimation. |

**Use when:** You deploy Apple iBeacon-compatible beacons for proximity, retail, or asset tracking.

---

### 5.2 AltBeacon

| Field | What It Controls |
|---|---|
| `enabled` | Activates AltBeacon filtering. |
| `filters[].mfgId` | Manufacturer ID as a hex string. |
| `filters[].beaconId` | Beacon ID UUID string. |
| `filters[].major` | Major value (integer). |
| `filters[].minor` | Minor value (integer). |
| `filters[].refRssi` | Reference RSSI at 1 meter (dBm). |

**Use when:** You deploy AltBeacon-compatible beacons (open-source alternative to iBeacon).

---

### 5.3 Eddystone

Eddystone supports four frame types; each carries different payload fields.

| `frameType` | Required Extra Fields | Purpose |
|---|---|---|
| `URL` | `url`, `txPower` | Broadcast a short URL. |
| `UID` | `namespace` (10-byte hex), `instance` (6-byte hex), `txPower` | Broadcast a fixed identifier. |
| `EID` | `ephemeralId` (8-byte hex), `txPower` | Broadcast a rotating ephemeral ID for security. |
| `TLM` | Telemetry frame | Broadcast sensor/battery telemetry. |

| Common Field | What It Controls |
|---|---|
| `enabled` | Activates Eddystone filtering. |
| `filters[].frameType` | Frame type to match: `URL`, `UID`, `EID`, or `TLM`. |
| `filters[].txPower` | TX power at 0 meters (dBm). |

**Use when:** You deploy Google Eddystone-compatible beacons for URL broadcasting, asset ID, or secure ephemeral identifiers.

---

### 5.4 Generic BLE

| Field | What It Controls |
|---|---|
| `enabled` | Activates generic BLE filtering. |
| `filters[].address` | Bluetooth device MAC address to match. |
| `filters[].addressType` | `public` or `random` Bluetooth address type. |
| `filters[].name` | Device advertised name to match. |
| `filters[].alias` | Device alias to match. |

**Use when:** You need to capture non-standard BLE devices (custom peripherals, sensors, wearables) that do not implement iBeacon, AltBeacon, or Eddystone.

> Important: Multiple filters within a protocol act as **OR** conditions (any match passes). Fields within a single filter act as **AND** conditions (all must match).

---

## 6. Applying the Configuration

Publishing this command only **saves** the configuration on the reader; BLE scanning does not begin until `start` is published with the BLE scan type.

### MQTT Workflow

```text
set_bleConfig                  -> save the BLE configuration
get_bleConfig                  -> verify the saved configuration
start                          -> payload: { "scanType": ["ble"] }
                                  or:      { "scanType": ["ble", "rfid"] }
stop                           -> stop active scanning
```

### Command Envelope

Every MQTT command published to the reader follows this envelope:

```json
{
  "command": "set_bleConfig",
  "command_id": "ble-set-001",
  "payload": {
    "ble": {
      "enable": true,
      "scanIntervalSec": 5,
      "additionalFilters": {
        "rssi": -80,
        "serviceUuids16": ["FEAA", "FE9B"],
        "serviceUuids128": ["FDA50693-A4E2-4FB1-AFCF-C6EB07647825"]
      },
      "protocols": {
        "iBeacon": {
          "enabled": true,
          "filters": [
            {
              "uuid": "FDA50693-A4E2-4FB1-AFCF-C6EB07647825",
              "major": 10001,
              "minor": 20002,
              "txPower": -59
            }
          ]
        }
      }
    }
  }
}
```

### Success Response Envelope

The reader publishes the response on the reply topic with the same `command_id`:

```json
{
  "command": "set_bleConfig",
  "command_id": "ble-set-001",
  "response": "success",
  "payload": {}
}
```

### Failure Response Envelope

```json
{
  "command": "set_bleConfig",
  "command_id": "ble-set-001",
  "response": "failure",
  "payload": {
    "code": 2,
    "message": "Invalid scan interval value"
  }
}
```

> Persistence: The reader stores the last saved configuration and restores it across reboots and MQTT reconnects. The configuration is only applied during scanning when `scanType: ["ble"]` is included in the `start` command payload.

---

## 7. Rules and Constraints

### Command Envelope

- `command` must be exactly `set_bleConfig`.
- `command_id` must be a unique identifier (UUID recommended) for response correlation.
- `payload` must contain a `ble` object with `ble.enable` set. An empty or malformed payload returns a failure response.

### Required Fields

- `ble.enable` is **required** in every request; even when only changing filters, you must include the current enable state.

### Core BLE Settings

- `ble.scanIntervalSec` - integer, **minimum value 1** (seconds).
- If `ble.enable: false`, all other fields are accepted and saved but ignored until scanning is re-enabled.

### Cross-Protocol Filters

- `additionalFilters.rssi` - integer, range **`-127` to `0`** (dBm).
- `additionalFilters.serviceUuids16` - array of 4-character hex strings.
- `additionalFilters.serviceUuids128` - array of 128-bit UUID strings in standard `8-4-4-4-12` hex format.

### iBeacon

- `uuid` - proximity UUID hex string.
- `major`, `minor` - integers.
- `txPower` - integer (dBm).

### AltBeacon

- `mfgId` - hex string (e.g., `"0118"`).
- `beaconId` - UUID string.
- `major`, `minor` - integers.
- `refRssi` - integer (dBm).

### Eddystone

- `frameType` - must be one of `URL`, `UID`, `EID`, `TLM`.
- `URL` frame requires `url` and `txPower`.
- `UID` frame requires `namespace` (10-byte hex), `instance` (6-byte hex), and `txPower`.
- `EID` frame requires `ephemeralId` (8-byte hex) and `txPower`.
- `TLM` frame carries telemetry; no identifier fields required.

### Generic BLE

- `address` - Bluetooth MAC address string (e.g., `"7E:41:25:1E:D5:16"`).
- `addressType` - must be `public` or `random`.
- `name`, `alias` - strings.

### Protocol Coexistence

- All four protocols (`iBeacon`, `altBeacon`, `eddystone`, `generic`) may be enabled simultaneously. They are **not mutually exclusive**.
- Multiple filters within the same protocol act as **OR** conditions. Fields within a single filter act as **AND** conditions.

### Activation

- Saving configuration does not start scanning. BLE scanning begins only when `start` is published with `scanType: ["ble"]` (or `["ble", "rfid"]` for combined inventory).
- Configuration persists across reboots and MQTT reconnects.

### Response Handling

- A `"response": "success"` indicates the configuration was saved successfully on the reader.
- A `"response": "failure"` indicates the command was rejected. The `payload.code` and `payload.message` fields identify the specific error.
- Always match the response by `command_id` to your original request.

### Failure Error Codes

| Code | Meaning |
|---|---|
| `1` | Generic command failure. |
| `2` | Invalid or out-of-range parameter value. |
| `3` | Required field missing. |
| `6` | Operation not permitted in current state. |
| `7` | Internal reader error. |
