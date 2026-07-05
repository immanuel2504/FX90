## 1. Description

The `GET /cloud/logs/RgWarningLog` REST endpoint retrieves the Reader Gateway warning log file from the reader.

This endpoint returns:

- The log filename
- The full content of the Reader Gateway warning log

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/logs/RgWarningLog` |
| Operation ID | `getRgWarningLog` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. When to Use This Endpoint

Use `GET /cloud/logs/RgWarningLog` to:

- Review Reader Gateway warning events that may indicate non-critical but notable operational issues
- Investigate intermittent connectivity or data delivery problems that did not produce errors
- Capture warning logs as part of routine reader health monitoring

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is the expected log file returned? | Confirms the correct log type was retrieved. |
| `content` | Are there recurring warning patterns? | Repeated warnings often precede errors — early detection prevents escalation to failures. |
