The `reboot` command restarts the reader. All in-progress operations stop and the reader briefly disconnects from MQTT.

Use this command to:

- Apply configuration changes that require a restart
- Recover from an unhealthy reader state
- Complete a firmware update cycle (reader may reboot automatically after `set_os`)

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Restart |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/reboot` |
| Related Commands | [get_status](get_status.md), [get_version](get_version.md), [set_os](set_os.md) |
| Supported Operations | Restart the reader |
| Supported API Versions | V1.0 |

## Before You Begin

Plan for downtime — the reader will disconnect until it finishes booting. In-flight inventory and MQTT sessions will be interrupted.

| What You Need | Details |
|---|---|
| Downtime window | Allow 1–3 minutes for reboot and MQTT reconnect. |
