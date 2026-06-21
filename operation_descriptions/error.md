## 1. Description

The `error` event reports an error-level diagnostic message from the reader's Reader Gateway (RG) or Radio Control (RC) subsystems.

This event includes:

- A human-readable `message` string describing the error condition

Use this event to:

- Detect and respond to critical conditions such as antenna disconnects, radio failures, and temperature faults
- Monitor resource exhaustion events including CPU, RAM, flash, and database capacity limits
- Feed alerting pipelines and on-call triggers for operational issues requiring immediate attention

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Error |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published when a monitored error condition is detected, per `managementEventConfig.errors` |
| Related Events | [async-events](async-events.md), [warning](warning.md), [heartbeat](heartbeat.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes `error` automatically when an error-level condition is detected. No command is required. The event is delivered inside the `async-events` envelope with `type: error`.

| Condition | State / Behavior | Notes |
|---|---|---|
| Reader Gateway resource threshold exceeded | Error event published with RG message | Covers CPU, RAM, and flash utilization above the error threshold; NTP sync failure; data endpoint disconnected; retention queue full. |
| Antenna disconnected or reconnected | Error event published with antenna port message | Indicates a physical cable or antenna issue on the reported port. Reads from that port stop until reconnection is confirmed. |
| Reader temperature critical | Error event published with temperature message | Ambient or PA temperature has exceeded the critical threshold. Inventory may be throttled or stopped. |
| Radio transmitter failure | Error event published with TX failure message | A PA failure on a specific port prevents RF transmission from that port. |
| Database full or reset | Error event published with database message | The on-device tag database has reached capacity and was reset, or repeated NGE reset failures occurred. |

> **Note:** Error events indicate conditions that are actively affecting reader operation or data delivery. Pair error event monitoring with `heartbeat` monitoring to distinguish between a reader that is healthy but encountered a transient error, and a reader that has stopped reporting entirely.
