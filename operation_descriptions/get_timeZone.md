The `get_timeZone` command retrieves the time zone currently configured on the reader.

This command returns:

- The configured time zone value

No additional payload fields are required to retrieve the time zone.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Time Zone Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_timeZone, get_ntpServer, get_status |
| Supported Operations | Retrieve the configured time zone |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_timeZone` to:

- Confirm the reader's time zone before relying on event timestamps
- Verify the result of a prior `set_timeZone` call
- Audit time zone consistency across a fleet
