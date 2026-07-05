## 1. Description

The `GET /cloud/gpo` REST endpoint retrieves the current digital output state of all GPO (General Purpose Output) pins on the reader.

This endpoint returns:

- The current HIGH or LOW state of each GPO pin (pins 1–4)

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/gpo` |
| Operation ID | `getGpoStatus` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. When to Use This Endpoint

Use `GET /cloud/gpo` to:

- Verify the current state of GPO outputs before issuing a GPO control command
- Troubleshoot whether an actuator or signaling device connected to a GPO pin is receiving the correct signal
- Confirm the effect of a prior GPO set command

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Pin 1 state | Is the pin HIGH or LOW? | Confirms whether an actuator or signal connected to GPO pin 1 is currently active. |
| Pin 2–4 states | Are all expected pins in the correct state? | Multi-pin output workflows require all relevant pins to be in the expected state. |
