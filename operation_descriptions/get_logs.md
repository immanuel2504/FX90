## 1. Description

The `get_logs` command retrieves the reader's current log configuration, including the radio packet log enable flag and per-component log levels.

This command returns:

- The radio packet log enable flag
- Per-component logging levels (e.g., DEBUG, INFO, WARNING, ERROR)

No additional payload fields are required to retrieve the log configuration.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Log Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/logs` |
| Related Commands | [set_logs](set_logs.md), [get_logs_syslog](get_logs_syslog.md), [get_radio_pkt_logs](get_radio_pkt_logs.md) |
| Supported Operations | Retrieve current logging configuration |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_logs` to:

- Review active log levels before changing them with `set_logs`
- Confirm whether radio packet logging is enabled before collecting packet logs
- Audit per-component verbosity during troubleshooting or before a support handoff

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `radioPacketLog` | Is radio packet logging enabled? | Must be enabled before `get_radio_pkt_logs` will return meaningful data. |
| Component log levels | Are levels set to DEBUG or higher? | Higher verbosity produces more diagnostic data but increases log size and I/O. |
