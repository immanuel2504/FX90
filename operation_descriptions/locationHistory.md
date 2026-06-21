## 1. Description

The `locationHistory` payload records estimated x/y location points for a tag as it moved through the read field before timing out in DIRECTIONALITY operating mode.

This event includes:

- A timestamp for each location estimate
- X and Y coordinates (in feet) for each estimated position

Use this event to:

- Plot a tag's movement path on a physical floor plan or site map
- Validate directionality zone placement by reviewing actual tag trajectories
- Build location-based analytics for portal, dock, and zone-based deployments

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Location History (embedded in directionality_tag_data_events) |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Included in `directionality_tag_data_events` when `state` is `TIMED_OUT` and `report_location_history` is enabled in directionality mode settings |
| Related Events | [directionality_tag_data_events](directionality_tag_data_events.md), [zoneHistory](zoneHistory.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

`locationHistory` is not published as a standalone event. It appears as an array inside a `directionality_tag_data_events` payload when the tag state is `TIMED_OUT` and the `report_location_history` option is enabled in the directionality mode configuration.

| Condition | State / Behavior | Notes |
|---|---|---|
| Tag times out in DIRECTIONALITY mode with `report_location_history` enabled | `locationHistory` array included in `TIMED_OUT` event | Each entry represents one location estimate during the tag's time in the read field. |
| `report_location_history` is disabled in mode settings | `locationHistory` array absent from `TIMED_OUT` event | Enable `report_location_history` in the directionality mode configuration to receive location data. |
| Tag state is `NEW`, `UPDATE`, or `TRANSITION` | `locationHistory` not included | Location history is only provided on tag timeout. |

> **Note:** Location estimates are computed from multi-antenna RF measurements and represent probabilistic positions, not GPS-level accuracy. The quality of location estimates depends on antenna placement, zone plan calibration, and the physical RF environment at the deployment site.
