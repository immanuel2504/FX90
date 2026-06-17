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
| Related Commands | set_ntpServer, get_timeZone, get_status |
| Supported Operations | Retrieve the configured NTP server |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_ntpServer` to:

- Confirm the reader points to the correct time source
- Verify the result of a prior `set_ntpServer` call
- Troubleshoot clock drift affecting event timestamps
