## 1. Description

The `GET /cloud/logs/RgErrorLog` REST endpoint retrieves the Reader Gateway error log file from the reader.

This endpoint returns:

- The log filename
- The full content of the Reader Gateway error log

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/logs/RgErrorLog` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. When to Use This Endpoint

Use `GET /cloud/logs/RgErrorLog` to:

- Retrieve Reader Gateway error events for troubleshooting connectivity or data delivery failures
- Investigate errors that occurred during tag data forwarding or cloud endpoint communication
- Capture error logs before a reader restart clears in-memory data

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is the expected log file returned? | Confirms the correct log type was retrieved. |
| `content` | Are there error messages or stack traces? | Error log content reveals the specific failures affecting Reader Gateway operation. |
