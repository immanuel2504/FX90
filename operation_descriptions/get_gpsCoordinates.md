## 1. Description

The `get_gpsCoordinates` command retrieves the reader's last reported GPS coordinates.

This command returns:

- Latitude and longitude values
- The number of satellites used for the last fix
- The time the location was last reported (`lastReportedTime`)

No additional payload fields are required. The returned values represent the most recent location data known to the reader.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | GPS Coordinates Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/readerLocation` |
| Related Commands | [get_network](get_network.md), [get_status](get_status.md) |
| Supported Operations | Retrieve the reader's last known GPS coordinates |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_gpsCoordinates` to:

- Record reader location for asset tracking or fleet management
- Confirm GPS or location availability on a deployed reader
- Feed location data into site, inventory, or logistics systems

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `latitude` | Is a valid latitude value returned? | A null or zero value may indicate the reader does not have a GPS fix yet. |
| `longitude` | Is a valid longitude value returned? | Combined with latitude, this identifies the reader's physical position. |
| `satellitesUsed` | How many satellites produced the fix? | A low satellite count indicates a weak fix and less reliable coordinates. |
| `lastReportedTime` | When was the location last reported? | Indicates how recent the coordinates are; a stale timestamp means the position may be outdated. |
