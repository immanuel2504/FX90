## 1. Description

The `get_logs` command retrieves the reader's current log configuration, including per-component log levels.

This command returns:

- The radio packet log enable flag
- Per-component logging levels

No additional payload fields are required to retrieve the log configuration.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Log Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_logs, get_logs_syslog, get_radio_pkt_logs |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve current logging configuration |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_logs` to:

- Review active log levels before changing them with `set_logs`
- Confirm whether radio packet logging is enabled
- Audit per-component verbosity during troubleshooting

> **Note:** Use `get_logs` before `set_logs` to review existing levels and avoid unintentionally raising verbosity in production.
