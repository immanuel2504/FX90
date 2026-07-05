## 1. Description

The `GET /cloud/gpi` REST endpoint retrieves the current digital input state of all GPI (General Purpose Input) pins on the reader.

This endpoint returns:

- The current HIGH or LOW state of each GPI pin (pins 1-4)

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/gpi` |
| Operation ID | `getGpiStatus` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_gpi_status` |
| MQTT Equivalent | `get_gpi_status` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/gpi` to:

- Check the current digital state of trigger or sensor inputs connected to GPI pins
- Verify GPI pin state before applying a GPI-triggered workflow
- Troubleshoot whether an external trigger signal is being received at the reader

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Pin 1 state | Is the pin HIGH or LOW? | Confirms whether an external trigger or sensor is actively signaling the reader. |
| Pin 2-4 states | Are all expected pins reporting the correct state? | Multi-pin triggers require all relevant pins to be in the expected state before initiating action. |
