The `locationHistory` payload records estimated x/y location points for a tag before it timed out in directionality mode.

This event includes:

- A timestamp and x/y coordinates for each location estimate

Use this event to:

- Plot a tag's movement path on a floor plan
- Validate directionality zone placement
- Build location-based analytics for portal/dock deployments

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Location History (embedded) |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Included in `directionality_tag_data_events` on `TIMED_OUT` when `report_location_history` is enabled |
| Related Events | directionality_tag_data_events, zoneHistory |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

`locationHistory` is not published as a standalone event. It appears as an array inside `directionality_tag_data_events` when `state` is `TIMED_OUT` and `report_location_history` is enabled in directionality mode settings.

| Field | Type | Description |
|---|---|---|
| `timestamp` | string | Timestamp in ISO 8601 format. |
| `x` | number | X coordinate of location estimate (feet). |
| `y` | number | Y coordinate of location estimate (feet). |
