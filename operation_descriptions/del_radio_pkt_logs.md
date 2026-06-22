## 1. Description

The `del_radio_pkt_logs` command purges radio packet log files stored on the reader. When you run this command, all accumulated radio packet log data is permanently deleted from the reader's storage.

Use this command to:

- Clear radio packet log archives after downloading them with `get_radio_pkt_logs`
- Free flash storage consumed by high-volume RF packet trace data
- Reset the packet log before starting a new diagnostic capture session

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Radio Packet Log Purge |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `DELETE /cloud/logs/radioPacketLog` |
| Related Commands | [get_radio_pkt_logs](get_radio_pkt_logs.md), [set_logs](set_logs.md), [del_syslogs](del_syslogs.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | None (empty payload) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Download the log files with `get_radio_pkt_logs` before sending this command if you need to retain the data for RF analysis or support cases.

| What You Need | Details |
|---|---|
| Log retrieval | Confirm you have downloaded the radio packet logs using `get_radio_pkt_logs` before purging. Deletion is permanent and cannot be undone. |
| Logging state | If radio packet logging (`radioPacketLog`) is currently enabled, the reader will start writing new log data immediately after purge. Disable logging first (via `set_logs`) if you want to start a clean session with no logging active. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail.

- The payload must be an empty object (`{}`). Providing additional payload fields will cause the command to be rejected.
- Deletion is immediate and permanent. There is no recovery path once the logs are purged.
- If `radioPacketLog` is currently enabled, the reader continues logging after purge; new log data begins accumulating immediately.
