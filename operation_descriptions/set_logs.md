## 1. Description

The `set_logs` command configures logging behavior on the reader, including per-component log verbosity and radio packet log capture.

This command allows you to configure:

- Whether radio packet logging is enabled through `radioPacketLog`
- The log level for each reader software component through `logLevels`

Use this command to:

- Enable radio packet logging before collecting RF diagnostic data
- Increase log verbosity for a specific component during troubleshooting
- Reduce log verbosity in production to limit storage consumption
- Reset component log levels to a known state before a support capture

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Log Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/logs` |
| Related Commands | [get_logs](get_logs.md), [get_logs_syslog](get_logs_syslog.md), [get_radio_pkt_logs](get_radio_pkt_logs.md), [get_rg_error_logs](get_rg_error_logs.md) |
| Supported Log Levels | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| Supported Components | `radio_control`, `reader_gateway` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Decide which logging areas you need to change before sending this command. Verbose log levels can fill storage quickly in production deployments.

| What You Need | Details |
|---|---|
| Radio packet log | Whether to enable or disable `radioPacketLog` (boolean). Enabling this is required before `get_radio_pkt_logs` will return useful data. |
| Component name | The component whose level to change: `radio_control` or `reader_gateway`. |
| Log level | The verbosity level to apply: `DEBUG` (most verbose), `INFO`, `WARNING`, or `ERROR` (least verbose). |
| Storage impact | `DEBUG` level generates the most data. Confirm available flash storage before enabling debug logging for extended periods. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or log data to be unavailable.

### Radio Packet Logging

- `radioPacketLog` must be set to `true` before RF-level diagnostic data will be written. Downloading `get_radio_pkt_logs` while this is `false` returns an empty or stale file.
- Radio packet logging consumes flash storage over time. Disable it (`radioPacketLog: false`) after completing diagnostic collection.

### Component Log Levels

- Component names in `logLevels` must exactly match the supported values (`radio_control`, `reader_gateway`). Unrecognized component names will be ignored or rejected.
- Log level values must be one of `DEBUG`, `INFO`, `WARNING`, or `ERROR`. Invalid strings will cause the command to be rejected.

### Apply Timing

- Log configuration changes take effect immediately after the command is acknowledged. Previously written log data is not affected.

### Security Note

- No credentials or secrets are required in the `set_logs` payload. Do not include authentication data in log configuration requests.
