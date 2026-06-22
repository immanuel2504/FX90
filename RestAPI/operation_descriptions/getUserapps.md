## 1. Description

The `GET /cloud/apps` REST endpoint retrieves the list of user applications installed on the reader.

This endpoint returns:

- An array of installed user apps, each with name, autostart flag, running status, and metadata

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/apps` |
| Operation ID | `getUserapps` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_user_apps` |
| MQTT Equivalent | `get_user_apps` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/apps` to:

- Confirm which user apps are installed before issuing start, stop, or uninstall requests
- Check whether a user app is currently running
- Verify autostart configuration per installed app
- Audit deployed applications across a fleet of readers

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `name` | Is the expected app present? | Confirms successful installation before attempting to start or configure the app. |
| `running` | Is the app currently running? | Required before sending a stop request; also confirms a successful start. |
| `autostart` | Is autostart enabled? | Determines whether the app will resume automatically after a reboot. |
