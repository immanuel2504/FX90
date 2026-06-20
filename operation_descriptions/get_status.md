The `get_status` command retrieves operational statistics and health information from the reader at the moment of the request.

This command returns:

- Uptime and current system time
- Radio connection and activity state
- Reader temperature

No additional payload fields are required to retrieve the full status snapshot.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | get_version, get_readerCapabilites, get_config |
| Supported Operations | Retrieve live operational statistics and health |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_status` to:

- Confirm the reader is powered, healthy, and reachable
- Verify the radio is connected before starting inventory
- Monitor reader temperature for thermal issues
- Synchronize against the reader's current system time
