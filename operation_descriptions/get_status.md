## 1. Description

The `get_status` command retrieves operational statistics and health information from the reader at the moment of the request.

This command returns:

- Uptime and current system time
- Radio connection and activity state
- Reader temperature
- CPU and RAM usage
- Flash storage usage by partition
- Antenna port connection states
- NTP synchronization status
- Cloud interface connection status

No additional payload fields are required to retrieve the full status snapshot.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/status` |
| Related Commands | [get_version](get_version.md), [get_readerCapabilities](get_readerCapabilities.md), [get_config](get_config.md) |
| Supported Operations | Retrieve live operational statistics and health |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_status` to:

- Confirm the reader is powered, healthy, and reachable
- Verify the radio is connected before starting inventory
- Monitor reader temperature for thermal issues
- Synchronize against the reader's current system time
- Check CPU, RAM, and flash usage during high-load scenarios

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `uptime` | How long has the reader been running? | Long uptimes confirm stability; short uptimes indicate an unexpected restart. |
| `radioConnection` | Is the value `connected`? | Inventory cannot run if the radio is disconnected. |
| `radioActivity` | Is it `active` or `inactive`? | Confirms whether an inventory session is currently in progress. |
| `temperature` | Is the value within safe operating range? | Excessive temperature can cause throttling or hardware faults. |
| `antennas` | Are expected ports `connected`? | A `disconnected` antenna port means tags on that port will not be read. |
| `ntp.offset` | Is the offset near zero? | A large NTP offset means event timestamps may be inaccurate. |
