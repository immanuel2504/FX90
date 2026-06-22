## 1. Description

The `GET /cloud/stack-led` REST endpoint retrieves the current state of the stack LED on the reader.

This endpoint returns:

- The active stack LED color
- Whether the LED is currently flashing
- How much time remains for a timed LED state (if applicable)

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/stack-led` |
| Operation ID | `getStackled` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_stackled` |
| MQTT Equivalent | `get_stackled` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/stack-led` to:

- Check the active stack LED color and brightness
- Confirm whether the LED is currently in a flashing state
- See how much time remains for a timed LED state before it reverts
- Verify the effect of a prior `PUT /cloud/stack-led` call

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `color` | What color is the LED showing? | Color is used to signal reader operational state to operators on the floor. |
| `flash` | Is the LED flashing? | Flashing indicates a transient or attention state versus a steady operational state. |
| `remainingTime` | Is a timer active? | A remaining time value indicates the LED will revert automatically after the duration expires. |
