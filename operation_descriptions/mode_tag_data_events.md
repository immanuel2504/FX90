## 1. Description

The `mode_tag_data_events` event carries RFID tag read data reported during SIMPLE, INVENTORY, PORTAL, CONVEYOR, or CUSTOM operating modes.

This event includes:

- Tag identity fields: EPC in `idHex`, format type, and optional memory bank data (TID, USER, XPC, PC, CRC)
- RF telemetry fields: antenna port, peak RSSI, channel, and phase angle
- Read count since the last report interval

Use this event to:

- Process individual tag reads in inventory and portal workflows
- Filter and deduplicate tags using `idHex` and `reads` count
- Build read-quality metrics from RSSI, antenna port, and phase data
- Capture TID or USER memory bank data when access operations are configured

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Mode Tag Data |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published inside `tagDataEvents` when a tag is inventoried or reported during a non-directionality mode |
| Related Events | [tagDataEvents](tagDataEvents.md), [directionality_tag_data_events](directionality_tag_data_events.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes this payload inside the `tagDataEvents` envelope when a tag is read during SIMPLE, INVENTORY, PORTAL, CONVEYOR, or CUSTOM mode. No command is required beyond starting inventory with `start`.

| Condition | State / Behavior | Notes |
|---|---|---|
| Tag inventoried during active inventory | One `mode_tag_data_events` entry per tag per report interval | Report frequency depends on `reportFilter.duration` in the mode configuration |
| `reportFilter.duration` is `0` | Each individual tag read reported separately | `channel` and `phase` are included per-read; RSSI reflects the single read value |
| `reportFilter.duration` is greater than `0` | Tags aggregated and reported at the end of each interval | `peakRssi` reflects the highest RSSI seen since the last report; `reads` reflects the total count; `channel` and `phase` may not be present |
| Memory bank access configured | `TID`, `USER`, `XPC`, `PC`, or `CRC` fields populated | Only present when the mode includes access operations targeting those memory banks |

> **Note:** The `channel` and `phase` fields are only included in the per-read payload when `reportFilter.duration` is `0`. When aggregation is active, `peakRssi` replaces per-read RSSI, and `reads` reflects the count over the report interval rather than a single read event.
