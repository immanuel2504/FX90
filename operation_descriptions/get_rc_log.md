## 1. Description

The `get_rc_log` command retrieves the radio-control information log as a downloadable archive.

This command returns:

- The archive filename
- The Base64-encoded `.tar.gz` radio-control log content

No additional payload fields are required to retrieve the radio-control log archive.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Radio-Control Log Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/logs/RcLog` |
| Related Commands | [get_rg_error_logs](get_rg_error_logs.md), [get_rg_warn_logs](get_rg_warn_logs.md), [get_logs](get_logs.md) |
| Supported Operations | Retrieve the radio-control information log archive |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_rc_log` to:

- Investigate radio-control behavior and RF issues
- Collect radio-control logs for a support escalation
- Correlate radio events with inventory anomalies

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is a filename returned? | Confirms the archive was successfully generated on the reader. |
| `content` | Is the Base64 string non-empty? | An empty value indicates the radio-control log has no recorded data. |
