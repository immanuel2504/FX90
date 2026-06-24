## 1. Description

The `get_ntpServer` command retrieves the NTP server currently configured for time synchronization on the reader.

This command returns:

- The NTP server hostname or IP address

No additional payload fields are required to retrieve the NTP server setting.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | NTP Server Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/ntpServer` |
| Related Commands | [set_ntpServer](set_ntpServer.md), [get_timeZone](get_timeZone.md), [get_status](get_status.md) |
| Supported Operations | Retrieve the configured NTP server |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_ntpServer` to:

- Confirm the reader is pointed at the correct time source for the deployment
- Verify the result of a prior `set_ntpServer` call
- Troubleshoot clock drift that is affecting event timestamps

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `ntpServer` | Is this the correct NTP server address? | An incorrect or unreachable NTP server causes clock drift, making event timestamps unreliable. |
