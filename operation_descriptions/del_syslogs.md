## Description

The `del_syslogs` command purges system logs stored on the reader, allowing a fresh log collection cycle.

Use this command to:

- Clear syslog archives after collecting them with `get_logs_syslog`
- Free storage consumed by accumulated system logs
- Reset logging before a diagnostic test run

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Syslog Purge |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_logs_syslog](get_logs_syslog.md), [get_logs](get_logs.md) |
| Supported API Versions | V1.0 |

## Before You Begin

Archive logs with `get_logs_syslog` before purging if you need to retain them for support.

MQTT command key: `del_logs_syslog`.
