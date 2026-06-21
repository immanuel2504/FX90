## 1. Description

The `zoneHistory` payload records the sequence of zones a tag traversed as it moved through the read field before timing out in DIRECTIONALITY operating mode.

This event includes:

- A timestamp for each zone visit
- The zone number for each visited zone

Use this event to:

- Reconstruct the full path a tag took through multiple zones before leaving the read field
- Audit zone transition sequences for compliance or workflow validation
- Debug directionality detection logic by replaying the zone visit history

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Zone History (embedded in directionality_tag_data_events) |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Included in `directionality_tag_data_events` when `state` is `TIMED_OUT` and `report_zone_history` is enabled in directionality mode settings |
| Related Events | [directionality_tag_data_events](directionality_tag_data_events.md), [locationHistory](locationHistory.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

`zoneHistory` is not published as a standalone event. It appears as an array inside a `directionality_tag_data_events` payload when the tag state is `TIMED_OUT` and the `report_zone_history` option is enabled in the directionality mode configuration.

| Condition | State / Behavior | Notes |
|---|---|---|
| Tag times out in DIRECTIONALITY mode with `report_zone_history` enabled | `zoneHistory` array included in `TIMED_OUT` event | Each entry records one zone visit in the order visited, with a UNIX millisecond timestamp. |
| `report_zone_history` is disabled in mode settings | `zoneHistory` array absent from `TIMED_OUT` event | Enable `report_zone_history` in the directionality mode configuration to receive zone history data. |
| Tag state is `NEW`, `UPDATE`, or `TRANSITION` | `zoneHistory` not included | Zone history is only provided on tag timeout. |

> **Note:** Zone numbers in `zoneHistory` correspond to the zone plan configured in directionality mode settings. Zone numbers range from 1 to 6. Use the zone number to look up the zone name and physical meaning in your directionality configuration.
