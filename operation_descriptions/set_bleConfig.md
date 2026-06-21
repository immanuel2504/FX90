## 1. Description

The `set_bleConfig` command configures the Bluetooth Low Energy (BLE) scanner on the reader.

This command allows you to configure:

- BLE scanner enable or disable through `ble.enable`
- Scan interval through `ble.scanIntervalSec`
- Cross-protocol RSSI and service UUID filters through `ble.additionalFilters`
- iBeacon filters through `ble.protocols.iBeacon`
- AltBeacon filters through `ble.protocols.altBeacon`
- Eddystone filters through `ble.protocols.eddystone`
- Generic BLE device filters through `ble.protocols.generic`

Use this command to:

- Activate or deactivate BLE scanning
- Tune how frequently the reader collects BLE scan results
- Filter out weak or irrelevant BLE advertisements using RSSI or service UUID
- Capture only specific beacon types or devices from the BLE environment
- Prepare BLE configuration before starting a combined RFID and BLE inventory

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | BLE Configuration Update |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_bleConfig](get_bleConfig.md), [start](start.md), [stop](stop.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | `ble.enable` |
| Supported BLE Protocols | iBeacon, AltBeacon, Eddystone (`URL`, `UID`, `EID`, `TLM`), Generic |
| Supported Address Types | `public`, `random` |
| RSSI Filter Range | `-127` to `0` dBm |
| Scan Interval Minimum | 1 second |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Decide which BLE behavior you need to configure before sending this command. A minimal payload only needs `ble.enable`; additional fields refine which beacons are captured.

| What You Need | Details |
|---|---|
| Enable decision | `ble.enable` is required in every request. Set to `true` to activate scanning, or `false` to disable it. |
| Scan interval | How often the reader collects BLE scan results (`scanIntervalSec`). Minimum value is `1` second. Shorter intervals increase responsiveness; longer intervals reduce data volume. |
| RSSI threshold | Set `additionalFilters.rssi` to drop weak advertisements. Range is `-127` to `0` dBm; values closer to zero indicate stronger signals. |
| Service UUID filters | Prepare 16-bit (`serviceUuids16`) or 128-bit (`serviceUuids128`) UUID lists to filter by advertised services. |
| iBeacon details | UUID, major, minor, and txPower values for each iBeacon filter entry. |
| AltBeacon details | Manufacturer ID, beacon ID, major, minor, and refRssi for each AltBeacon filter entry. |
| Eddystone frame type | Choose `URL`, `UID`, `EID`, or `TLM` and supply the corresponding fields (`url`, `namespace`/`instance`, `ephemeralId`). |
| Generic BLE device | Bluetooth MAC address, address type (`public`/`random`), device name, or alias for each generic filter entry. |
| Activation | Saving this configuration does not start BLE scanning. Send `start` with `scanType: ["ble"]` to begin scanning. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or BLE data to be absent from inventory results.

### Required Fields

- `ble.enable` is required in every request. Omitting it will cause the command to be rejected.
- Even when only updating filters, the current `ble.enable` value must be included in the payload.

### Scan Interval

- `scanIntervalSec` must be an integer with a minimum value of `1`. Values below `1` will be rejected.

### RSSI Filter

- `additionalFilters.rssi` must be an integer in the range `-127` to `0`. Values outside this range will be rejected.

### Eddystone Filters

- `frameType` must be one of `URL`, `UID`, `EID`, or `TLM`. Unrecognized frame type strings will be rejected.
- For `URL` frames: `url` and `txPower` are required.
- For `UID` frames: `namespace` (10-byte hex), `instance` (6-byte hex), and `txPower` are required.
- For `EID` frames: `ephemeralId` (8-byte hex) and `txPower` are required.

### Protocol Coexistence

- All four BLE protocols (iBeacon, AltBeacon, Eddystone, Generic) may be configured simultaneously; they are not mutually exclusive.
- Multiple filter entries within a single protocol act as OR conditions. All fields within a single filter entry act as AND conditions.

### Activation

- This command saves the BLE configuration. BLE scanning does not begin until `start` is published with `scanType: ["ble"]` or `["ble", "rfid"]`.
- The saved configuration persists across reboots and MQTT reconnects.

### Security Note

- No credentials or secrets are required in the `set_bleConfig` payload. Do not include authentication data in BLE configuration requests.
