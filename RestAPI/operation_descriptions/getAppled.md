## 1. Description

The `GET /cloud/app-led` REST endpoint retrieves the current state of the application LED on the reader.

This endpoint returns:

- The application LED status (`DEFAULT` or `NOT_DEFAULT`)

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/app-led` |
| Operation ID | `getAppLed` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_appled` |
| MQTT Equivalent | `get_appled` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/app-led` to:

- Confirm whether the application LED is showing default reader state or has been overridden
- Verify the effect of a prior `PUT /cloud/app-led` call
- Audit LED state as part of a device health or provisioning check

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `status` | Is it `DEFAULT` or `NOT_DEFAULT`? | `NOT_DEFAULT` indicates the LED has been overridden by the application; `DEFAULT` means it reflects normal reader status. |
