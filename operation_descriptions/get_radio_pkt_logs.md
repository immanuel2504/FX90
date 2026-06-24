## 1. Description

The `get_radio_pkt_logs` command retrieves the radio packet log as a downloadable archive.

This command returns:

- The archive filename
- The Base64-encoded `.tar.gz` radio packet log content

No additional payload fields are required to retrieve the radio packet log archive. Radio packet logging must be enabled via `set_logs` before meaningful data is available.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Radio Packet Log Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/logs/radioPacketLog` |
| Related Commands | [del_radio_pkt_logs](del_radio_pkt_logs.md), [get_logs](get_logs.md), [get_logs_syslog](get_logs_syslog.md), [set_logs](set_logs.md) |
| Supported Operations | Retrieve the radio packet log archive |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_radio_pkt_logs` to:

- Collect low-level radio packet traces for RF diagnostics
- Capture evidence when investigating read-performance issues
- Archive packet logs before purging with `del_radio_pkt_logs`

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is a filename returned? | Confirms the archive was generated and ready for download. |
| `content` | Is the Base64 string non-empty? | An empty value means no packet log data exists - verify logging is enabled with `get_logs`. |
