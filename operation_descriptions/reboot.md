## 1. Description

The `reboot` command restarts the reader. All in-progress operations stop and the reader briefly disconnects from MQTT.

This command requires:

- An empty `payload` object (`{}`) — no additional parameters are needed
- A unique `command_id` that the reader echoes in the response

Use this command to:

- Apply configuration changes that require a restart
- Recover from an unhealthy reader state
- Complete a firmware update cycle (the reader may reboot automatically after `set_os`)

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Restart |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/reboot` |
| Related Commands | [get_status](get_status.md), [get_version](get_version.md), [set_os](set_os.md) |
| Required Payload Fields | None (empty object `{}`) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Plan for downtime — the reader will disconnect until it finishes booting. In-flight inventory and MQTT sessions will be interrupted.

| What You Need | Details |
|---|---|
| Downtime window | Allow 1–3 minutes for reboot and MQTT reconnect |

