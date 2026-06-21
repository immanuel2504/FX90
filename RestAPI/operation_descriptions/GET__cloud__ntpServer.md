## 1. Description

The `GET /cloud/ntpServer` REST endpoint retrieves the NTP server address currently configured on the reader.

This endpoint returns:

- The NTP server hostname or IP address the reader is using for time synchronization

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/ntpServer` |
| Operation ID | `GET__cloud__ntpServer` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Equivalent | `get_ntpServer` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/ntpServer` to:

- Confirm the reader is using the correct NTP server for time synchronization
- Troubleshoot timestamp accuracy issues that may be caused by an unreachable or misconfigured NTP server
- Verify the effect of a prior NTP server update

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `ntpServer` | Does it point to the correct NTP server? | An unreachable or wrong NTP server leads to clock drift, which affects log timestamps and time-based trigger logic. |
