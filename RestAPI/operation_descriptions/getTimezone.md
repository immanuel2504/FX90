## 1. Description

The `GET /cloud/timeZone` REST endpoint retrieves the reader's currently configured time zone.

This endpoint returns:

- The IANA time zone string currently set on the reader

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/timeZone` |
| Operation ID | `getTimeZone` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_timeZone` |
| MQTT Equivalent | `get_timeZone` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/timeZone` to:

- Confirm the reader is using the correct local time zone for timestamp generation
- Verify the effect of a prior `PUT /cloud/timeZone` call
- Audit time zone consistency across a fleet of readers

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `timeZone` | Does it match the deployment location's time zone? | Incorrect time zone causes reader timestamps to differ from local real-world time, which can affect log correlation and event timing. |
