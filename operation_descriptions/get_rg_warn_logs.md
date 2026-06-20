The `get_rg_warn_logs` command retrieves the reader-gateway warning log as a downloadable archive.

This command returns:

- The archive filename
- The Base64-encoded `.tar.gz` log content

No additional payload fields are required to retrieve the warning log archive.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader-Gateway Warning Log Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | get_rg_error_logs, get_rc_log, get_logs |
| Supported Operations | Retrieve the reader-gateway warning log archive |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_rg_warn_logs` to:

- Review non-fatal reader-gateway warnings
- Spot early signs of degradation before errors occur
- Collect warning logs for support escalation
