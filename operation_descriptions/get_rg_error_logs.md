## 1. Description

The `get_rg_error_logs` command retrieves the reader-gateway error log as a downloadable archive.

This command returns:

- The archive filename
- The Base64-encoded `.tar.gz` reader-gateway error log content

No additional payload fields are required to retrieve the error log archive.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader-Gateway Error Log Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/logs/RgErrorLog` |
| Related Commands | [get_rg_warn_logs](get_rg_warn_logs.md), [get_rc_log](get_rc_log.md), [get_logs](get_logs.md) |
| Supported Operations | Retrieve the reader-gateway error log archive |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_rg_error_logs` to:

- Investigate reader-gateway errors affecting tag data delivery
- Collect error logs for a support escalation
- Correlate gateway errors with `error` management events

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is a filename returned? | Confirms the archive was generated and is ready for download. |
| `content` | Is the Base64 string non-empty? | An empty value means no errors have been logged since the last purge. |
