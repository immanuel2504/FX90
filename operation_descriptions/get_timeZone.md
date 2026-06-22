## 1. Description

The `get_timeZone` command retrieves the time zone currently configured on the reader.

This command returns:

- The configured time zone value (IANA time zone identifier)

No additional payload fields are required to retrieve the time zone.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Time Zone Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/timeZone` |
| Related Commands | [set_timeZone](set_timeZone.md), [get_ntpServer](get_ntpServer.md), [get_status](get_status.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the configured time zone |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_timeZone` to:

- Confirm the reader's time zone before relying on event timestamps
- Verify the result of a prior `set_timeZone` call
- Audit time zone consistency across a fleet of readers

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `timeZone` | Is this the correct IANA time zone for the deployment location? | An incorrect time zone causes local event timestamps to be offset from actual local time. |
