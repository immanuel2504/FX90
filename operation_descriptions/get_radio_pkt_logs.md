## 1. Description

The `get_radio_pkt_logs` command retrieves the radio packet log as a downloadable archive.

This command returns:

- The archive filename
- The Base64-encoded `.tar.gz` log content

No additional payload fields are required to retrieve the radio packet log archive.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Radio Packet Log Retrieval |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | del_radio_pkt_logs, get_logs, get_logs_syslog |
| Supported Operations | Retrieve the radio packet log archive |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_radio_pkt_logs` to:

- Collect low-level radio packet traces for RF diagnostics
- Capture evidence when investigating read-performance issues
- Archive packet logs before purging with `del_radio_pkt_logs`
