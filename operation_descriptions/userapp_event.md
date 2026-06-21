## 1. Description

The `userapp_event` event delivers a custom asynchronous event emitted by a user application running on the reader.

This event includes:

- A raw event string defined and formatted by the user application

Use this event to:

- Receive custom signals from on-reader user applications without polling
- Integrate application-specific logic into your backend processing pipeline
- Forward user application state changes or output to external systems

## 2. Event Details

| Property | Value |
|---|---|
| Event Type | User Application Event |
| Communication Type | Device to Cloud |
| Applies To | FXR90 |
| Trigger Condition | Published when an installed user application emits a custom event, if user app events are enabled in `managementEventConfig` |
| Related Events | [async-events](async-events.md), [heartbeat](heartbeat.md) |
| Supported API Versions | V1.0 |

## 3. When This Event Is Published

The reader publishes `userapp_event` when an installed user application emits a custom event. No reader-level command is required. The event is delivered inside the `async-events` envelope with `type: userapp`. The `component` field in the envelope carries the name of the application that emitted the event.

| Condition | State / Behavior | Notes |
|---|---|---|
| User application emits a custom event | `userapp_event` published with `event` string | The application must be running. A stopped application cannot emit events. |
| User application is stopped | No event published | Check `heartbeat` `userapps[].status` to confirm the application is running if events are not being received. |

> **Note:** The format and content of the `event` string are defined entirely by the user application, not by the reader firmware. Parse `event` according to your application's documented output format. The `component` field in the `async-events` envelope identifies which application produced the event when multiple user applications are installed.
