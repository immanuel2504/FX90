## Description

The `get_gpsCoordinates` command retrieves the reader's last reported GPS coordinates.

Use this command to:

- Record reader location for asset tracking
- Confirm GPS/location availability on a deployed reader
- Feed location data into fleet, site, or inventory systems

## Command Details

| Property | Value |
|---|---|
| Pattern Name | GPS Coordinates Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_network](get_network.md), [get_status](get_status.md) |
| Supported Operations | Retrieve GPS coordinates |
| Supported API Versions | V1.0 |

## Before You Begin

No command payload fields are required. The returned values represent the latest location data known to the reader.
