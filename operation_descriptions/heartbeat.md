## 1. Description

The `heartbeat` event provides a periodic health and operational snapshot of the reader.

This event includes:

- Radio activity state, connection status, and tag-read count
- Reader gateway event-delivery statistics
- System temperature, uptime, CPU, RAM, and flash usage
- Status of installed user applications

Use this event to:

- Confirm the reader is alive, connected, and actively reporting to the cloud
- Track radio activity state and tag read throughput over time
- Monitor system temperature and uptime for health dashboards and alerting
- Detect user application status changes without polling

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Heartbeat |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published periodically per `managementEventConfig.heartbeat` interval configuration |
| Related Events | [async-events](async-events.md), [error](error.md), [warning](warning.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes `heartbeat` automatically on a periodic interval configured in `managementEventConfig`. No command is required. The event is delivered inside the `async-events` envelope with `type: heartbeat`.

| Condition | State / Behavior | Notes |
|---|---|---|
| Reader connected and healthy | Heartbeat published at the configured interval | Interval is set in `managementEventConfig.heartbeat`. A missing heartbeat beyond the expected interval indicates a connectivity or health issue. |
| Radio is actively reading tags | `radio_control.radioActivity` is `active` | Transitions to `inactive` when inventory is stopped. |
| Radio connection established | `radio_control.radioConnection` is `connected` | Transitions to `disconnected` if the radio module loses contact. |
| Tags being read | `radio_control.numTagReads` incrementing | Use as a throughput indicator. Resets between heartbeat events. |
| User application running | `userapps[].status` is `running` | A `stopped` status may indicate an unexpected application crash. |

> **Note:** Temperature values reflect the reader's ambient and power amplifier sensors at the time of the heartbeat. Sustained high temperatures should trigger investigation as they may indicate cooling or placement issues.
