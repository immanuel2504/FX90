## 1. Description

The `set_logs` command configures logging on the reader, including per-component log levels and radio packet logging.

Use it to:

- Enable or disable radio packet logging for RF diagnostics
- Set log verbosity per subcomponent (radio_control, reader_gateway)
- Tune logging before collecting log archives

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Log Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_logs](get_logs.md), [get_logs_syslog](get_logs_syslog.md), [get_radio_pkt_logs](get_radio_pkt_logs.md) |
| Supported Operations | Configure logging levels and packet logging |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the command. Raising log verbosity in production can fill storage quickly.

| What You Need | Details |
|---|---|
| Radio packet log | Whether to enable `radioPacketLog` (boolean). |
| Component levels | Per-component name (`radio_control` or `reader_gateway`) and level (`DEBUG`, `INFO`, `WARNING`, `ERROR`). |
