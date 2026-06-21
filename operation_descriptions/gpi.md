## 1. Description

The `gpi` event reports a state change on a General Purpose Input (GPI) pin of the reader.

This event includes:

- The GPI pin number that changed state
- The new pin state (HIGH or LOW)

Use this event to:

- React to external sensors or triggers wired to GPI pins (motion detectors, beam-break sensors, push buttons)
- Drive inventory start/stop workflows based on GPI pin transitions
- Audit input state transitions over time for compliance or diagnostics

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | GPI State Change |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published when a GPI pin transitions state, if GPI events are enabled in `managementEventConfig.gpiEvents` |
| Related Events | [async-events](async-events.md), [gpo](gpo.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes `gpi` automatically when a GPI pin transitions from HIGH to LOW or LOW to HIGH, provided GPI event reporting is enabled in `managementEventConfig`. No command is required. The event is delivered inside the `async-events` envelope with `type: gpi`.

| Condition | `state` | Notes |
|---|---|---|
| External signal drives GPI pin high | `HIGH` | Indicates the connected sensor or trigger is asserted. |
| External signal releases GPI pin | `LOW` | Indicates the connected sensor or trigger has de-asserted. |
| GPI event reporting disabled in `managementEventConfig` | No event published | Enable `gpiEvents` in the management event configuration to receive GPI state transitions. |

> **Note:** GPI events are only published when `managementEventConfig.gpiEvents` is enabled. Verify this configuration setting is active before relying on GPI events to drive workflows. GPI pin state can always be checked on demand using `get_gpi_status`.
