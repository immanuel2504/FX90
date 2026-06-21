## 1. Description

The `warning` event reports a warning-level diagnostic message from the reader's Reader Gateway (RG) or Radio Control (RC) subsystems.

This event includes:

- A human-readable `message` string describing the warning condition

Use this event to:

- Detect early signs of degradation before they escalate to errors
- Monitor elevated resource utilization and rising temperature trends
- Track database and storage capacity approaching their limits
- Feed monitoring dashboards to provide early visibility of reader health trends

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Warning |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published when a monitored warning condition is detected, per `managementEventConfig.warnings` |
| Related Events | [async-events](async-events.md), [error](error.md), [heartbeat](heartbeat.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes `warning` automatically when a warning-level condition is detected. No command is required. The event is delivered inside the `async-events` envelope with `type: warning`.

| Condition | State / Behavior | Notes |
|---|---|---|
| Reader Gateway resource utilization elevated | Warning event published with RG message | Covers CPU, RAM, or flash usage above warning threshold but below error threshold; NTP sync degraded. |
| Reader temperature elevated | Warning event published with temperature message | Ambient or PA temperature is high but has not yet reached the critical threshold. Investigate cooling or reader placement. |
| Database nearing capacity | Warning event published with database message | The on-device tag database is approaching its limit and will be reset if it reaches full capacity. |
| NGE API error | Warning event published with API error code | A non-critical API error was reported by the NGE layer. |

> **Note:** Warning events precede error events for most monitored conditions. Responding to warnings (e.g., reducing log verbosity to free flash, improving airflow) can prevent escalation to error-level conditions that affect reader operation.
