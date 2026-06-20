The `set_timeZone` command sets the time zone on the reader.

Use it to:

- Align the reader clock with the deployment site's local time zone
- Correct event timestamps for local reporting
- Standardize time zone across a fleet of readers

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Time Zone Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_timeZone](get_timeZone.md), [set_ntpServer](set_ntpServer.md), [get_status](get_status.md) |
| Supported Operations | Set the reader time zone |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the command. An unrecognized time zone string will be rejected.

| What You Need | Details |
|---|---|
| Time zone | A supported time zone name or GMT-offset string (e.g. `"Pacific Time (US & Canada)"` or `"(GMT-08:00) Pacific Time (US & Canada)"`). See `get_timeZone` for allowed values. |
