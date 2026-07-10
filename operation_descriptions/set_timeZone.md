## 1. Description

The `set_timeZone` command sets the time zone on the reader.

This command allows you to configure:

- The reader's local time zone through `timeZone`

Use this command to:

- Align the reader's clock with the deployment site's local time zone
- Correct event timestamps and log timestamps for local time reporting
- Standardize time zone configuration across a fleet of readers
- Update the time zone after a reader is relocated to a different region

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Time Zone Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/timeZone` |
| Related Commands | [get_timeZone](get_timeZone.md), [set_ntpServer](set_ntpServer.md), [get_status](get_status.md) |
| Required Payload Fields | `timeZone` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Have the exact time zone string ready before sending this command. An unrecognized time zone string will be rejected.

| What You Need | Details |
|---|---|
| Time zone string | A reader-supported time zone name (e.g., `"International Date Line West"`, `"Pacific Time (US & Canada)"`). Use `get_timeZone` to check the currently configured value. |
| Site location | Confirm the physical deployment location of the reader to select the correct time zone. |

