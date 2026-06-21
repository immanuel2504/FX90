## 1. Description

The `tagDataEvents` event is the common envelope for all RFID tag read payloads the reader publishes to configured data endpoints.

This event includes:

- The operating mode `type` that generated the tag data
- A `timestamp` for the read event
- A `data` payload whose shape depends on the active operating mode

Use this event to:

- Receive tag reads from inventory, portal, conveyor, and directionality modes through a single data channel
- Route tag data to the correct handler in your backend based on the `type` field
- Correlate reads across sessions using `timestamp` and `eventNum` in the inner payload

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | Tag Data Event Envelope |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published when the reader reports tag reads during an active operating mode |
| Related Events | [mode_tag_data_events](mode_tag_data_events.md), [directionality_tag_data_events](directionality_tag_data_events.md), [async-events](async-events.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes `tagDataEvents` automatically to configured data endpoints while an inventory or directionality operation is active. No command is required beyond starting inventory with `start`.

| `type` | `data` Payload Shape | Description |
|---|---|---|
| `SIMPLE` | [mode_tag_data_events](mode_tag_data_events.md) | Basic continuous inventory read |
| `INVENTORY` | [mode_tag_data_events](mode_tag_data_events.md) | Timed or triggered inventory read |
| `PORTAL` | [mode_tag_data_events](mode_tag_data_events.md) | Portal or dock read with GPI triggers |
| `CONVEYOR` | [mode_tag_data_events](mode_tag_data_events.md) | Conveyor-style read |
| `CUSTOM` | [mode_tag_data_events](mode_tag_data_events.md) | Custom mode read |
| `DIRECTIONALITY` | [directionality_tag_data_events](directionality_tag_data_events.md) | Zone-based tag state and direction |

> **Note:** The `data` payload shape changes based on `type`. Always check the `type` field before parsing `data`. For DIRECTIONALITY mode, the inner payload carries zone state and direction rather than per-read RF telemetry.
