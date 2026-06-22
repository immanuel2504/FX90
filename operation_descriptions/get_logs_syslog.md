## 1. Description

The `get_logs_syslog` command retrieves the reader's system log as a downloadable archive.

This command returns:

- The archive filename
- The Base64-encoded `.tar.gz` syslog content

No additional payload fields are required to retrieve the syslog archive.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Syslog Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/logs/syslog` |
| Related Commands | [del_syslogs](del_syslogs.md), [get_logs](get_logs.md), [get_radio_pkt_logs](get_radio_pkt_logs.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the system log archive |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_logs_syslog` to:

- Collect system logs for support escalation or diagnostics
- Capture a log snapshot before rebooting or applying an OS update
- Archive syslog content before purging with `del_syslogs`

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is a filename returned? | Confirms the archive was generated and identifies the log file for record keeping. |
| `content` | Is the Base64 string non-empty? | An empty value indicates no syslog data was available on the reader. |
