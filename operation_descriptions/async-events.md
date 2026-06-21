## 1. Description

The `async-events` event is the common envelope for all asynchronous management events the reader publishes to configured management endpoints.

This event includes:

- An event `type` discriminator that identifies the event category
- A `timestamp` for the event
- The source `component` (`RG`, `RC`, or a user-app name) and an `eventNum` sequence counter
- A `data` payload whose shape depends on the `type` field

Use this event to:

- Receive all device health, GPIO, firmware, diagnostic, and user-app events through a single management channel
- Route events to the correct handler in your backend based on the `type` field
- Correlate related events using `component` and `eventNum` across the event stream

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Management Event Envelope |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Wraps every asynchronous management event published by the reader to `managementEventConfig` endpoints |
| Related Events | [heartbeat](heartbeat.md), [firmwareUpdateProgress](firmwareUpdateProgress.md), [gpi](gpi.md), [gpo](gpo.md), [error](error.md), [warning](warning.md), [userapp_event](userapp_event.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes management events automatically to the endpoints configured in `managementEventConfig`. No command is required. The `type` field selects which payload shape appears in `data`.

| `type` | `data` Payload | Condition |
|---|---|---|
| `heartbeat` | [heartbeat](heartbeat.md) | Published on a periodic interval per `managementEventConfig.heartbeat` |
| `firmwareUpdateProgress` | [firmwareUpdateProgress](firmwareUpdateProgress.md) | Published during an active firmware update started by `set_os` |
| `gpi` | [gpi](gpi.md) | Published when a GPI pin changes state, if enabled in `managementEventConfig.gpiEvents` |
| `gpo` | [gpo](gpo.md) | Published when a GPO pin changes state |
| `error` | [error](error.md) | Published when an error-level condition occurs, per `managementEventConfig.errors` |
| `warning` | [warning](warning.md) | Published when a warning-level condition occurs, per `managementEventConfig.warnings` |
| `userapp` | [userapp_event](userapp_event.md) | Published when an installed user application emits a custom event |

> **Note:** Always check the `type` field before parsing `data`. The `data` shape is different for each event type. Consumers should handle unknown `type` values gracefully to remain forward-compatible with new event types added in future firmware versions.
