## 1. Description

The `set_ntpServer` command sets one or more NTP servers used by the reader for time synchronization.

This command allows you to configure:

- The primary NTP server through `server`
- Optional secondary NTP servers through `server1` and `server2`

Use this command to:

- Point the reader to your organization's NTP server for accurate timekeeping
- Configure fallback NTP servers for resilience when the primary is unreachable
- Correct clock drift that is affecting event timestamps and log correlation
- Standardize NTP configuration across a fleet of readers

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | NTP Server Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/ntpServer` |
| Related Commands | [get_ntpServer](get_ntpServer.md), [set_timeZone](set_timeZone.md), [get_status](get_status.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | `server` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm that the NTP server is reachable from the reader's network before sending this command. An unreachable NTP server will leave the reader clock unsynchronized.

| What You Need | Details |
|---|---|
| Primary NTP server | Hostname or IP address of the primary NTP server (payload key: `server`). The reader must be able to reach this address on UDP port 123. |
| Fallback servers | Optional - provide `server1` and `server2` for resilience. If the primary is unreachable, the reader will attempt fallback servers in order. |
| Network access | NTP uses UDP port 123. Ensure this port is open between the reader and the NTP server on all network paths. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or time synchronization to be unavailable.

### Required Fields

- `server` is required in the payload. Omitting it will cause the command to be rejected.

### Server Values

- `server`, `server1`, and `server2` must be valid hostnames or IP addresses. Empty strings or malformed addresses will be rejected.
- The reader will use `server1` and `server2` only if the primary `server` is unreachable. Both are optional.

### Apply Timing

- The NTP server configuration takes effect immediately after the command is acknowledged.
- The reader attempts synchronization shortly after the command is applied. Verify the sync status using `get_status` (check the `ntp.offset` field).

### Security Note

- No credentials or secrets are required in the `set_ntpServer` payload. Do not include authentication data in NTP configuration requests.
