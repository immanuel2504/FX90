## 1. Description

The `gpo` event reports a state change on a General Purpose Output (GPO) pin of the reader.

This event includes:

- The GPO pin number that changed state
- The new pin state (HIGH or LOW)

Use this event to:

- Confirm that a `set_gpo` command successfully drove an external device (light stack, horn, gate)
- Audit GPO output transitions across your management channel
- Synchronize your application's internal state model with the reader's actual output state

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | GPO State Change |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published when a GPO pin changes state |
| Related Events | [async-events](async-events.md), [gpi](gpi.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes `gpo` automatically when a GPO pin transitions state. No command is required. The event is delivered inside the `async-events` envelope with `type: gpo`.

| Condition | `state` | Notes |
|---|---|---|
| GPO pin driven HIGH | `HIGH` | Published after the output is asserted, including via `set_gpo` or a mode-triggered output. |
| GPO pin driven LOW | `LOW` | Published after the output is de-asserted. |

> **Note:** GPO events provide asynchronous confirmation that the output state changed. For immediate state verification, use `get_gpostatus` to poll the current GPO pin state directly.
