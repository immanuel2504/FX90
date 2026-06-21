## 1. Description

The `directionality_tag_data_events` event carries zone-based tag state and direction information during DIRECTIONALITY operating mode.

This event includes:

- Tag identity (`tagId`) and current zone state (`NEW`, `UPDATE`, `TRANSITION`, `TIMED_OUT`)
- Current and previous zone number and zone name
- Travel direction on tag timeout (`IN`, `OUT`, `NONE`, `UNKNOWN`, `ERROR`)
- Optional zone history and location history arrays when enabled in mode settings

Use this event to:

- Detect tag entry and exit at zone boundaries (portals, docks, doorways)
- Determine the travel direction of a tag as it leaves the read field
- Build zone-transition analytics, flow monitoring, and alerting
- Reconstruct tag movement paths using zone history and location history

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Directionality Tag Data |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published inside `tagDataEvents` when a tag's zone state changes during DIRECTIONALITY mode |
| Related Events | [tagDataEvents](tagDataEvents.md), [zoneHistory](zoneHistory.md), [locationHistory](locationHistory.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes this payload inside the `tagDataEvents` envelope (`type: DIRECTIONALITY`) when a tag's zone state changes. No command is required beyond starting directionality mode with `start`.

| `state` | Condition | Notes |
|---|---|---|
| `NEW` | Tag first appears in a zone | Includes `zone` and `zoneName`. No previous zone. |
| `UPDATE` | Tag remains in the same zone and is read again | Includes `zone` and `zoneName`. Confirms continued presence. |
| `TRANSITION` | Tag moves from one zone to another | Includes `zone`, `zoneName`, `prevZone`, and `prevZoneName`. |
| `TIMED_OUT` | Tag is no longer detected in the read field | Includes `direction`. Optionally includes `zoneHistory` and `locationHistory` if enabled in mode settings. |

> **Note:** `zoneHistory` is included in `TIMED_OUT` events only when `report_zone_history` is enabled in the directionality mode configuration. `locationHistory` is included only when `report_location_history` is enabled. Both are absent otherwise and must not be assumed to be present.
