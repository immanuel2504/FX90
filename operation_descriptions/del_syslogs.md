## 1. Description

The `del_syslogs` command purges system log files stored on the reader. When you run this command, all accumulated syslog data is permanently deleted from the reader's storage.

Use this command to:

- Clear syslog archives after downloading them with `get_logs_syslog`
- Free flash storage consumed by accumulated system log data
- Reset the syslog before a diagnostic test run to ensure a clean capture

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Syslog Purge |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `DELETE /cloud/logs/syslog` |
| Related Commands | [get_logs_syslog](get_logs_syslog.md), [get_logs](get_logs.md), [del_radio_pkt_logs](del_radio_pkt_logs.md) |
| Required Payload Fields | None (empty payload) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Archive the syslog files with `get_logs_syslog` before sending this command if you need to retain them for support cases or post-incident analysis.

| What You Need | Details |
|---|---|
| Log retrieval | Confirm you have downloaded the syslog using `get_logs_syslog` before purging. Deletion is permanent and cannot be undone. |
| Diagnostic baseline | If you plan to run a diagnostic session after purging, ensure all relevant services are in a known state before the purge so the new logs capture only the events of interest. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail.

- The payload must be an empty object (`{}`). Providing additional payload fields will cause the command to be rejected.
- Deletion is immediate and permanent. Purged syslog data cannot be recovered.
- The OS continues writing new syslog entries immediately after purge; a clean initial state is only guaranteed at the moment the purge completes.
