## 1. Description

The `GET /cloud/logs/RcLog` REST endpoint retrieves the Radio Control (RC) information log file from the reader.

This endpoint returns:

- The log filename
- The full content of the RC info log

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/logs/RcLog` |
| Operation ID | `getRcLog` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. When to Use This Endpoint

Use `GET /cloud/logs/RcLog` to:

- Retrieve radio control events and diagnostic messages for troubleshooting inventory issues
- Capture RC log data before a reader restart wipes in-memory logs
- Investigate radio connection failures or inventory start/stop events

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is the expected log file returned? | Confirms the correct log type was retrieved. |
| `content` | Does the log contain relevant events or error messages? | The log content reveals radio control state changes, errors, and diagnostics during reader operation. |
