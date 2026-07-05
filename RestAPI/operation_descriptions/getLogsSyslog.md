## 1. Description

The `GET /cloud/logs/syslog` REST endpoint retrieves the system log file from the reader's operating system.

This endpoint returns:

- The syslog filename
- The full content of the OS-level system log

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/logs/syslog` |
| Operation ID | `getLogsSyslog` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. When to Use This Endpoint

Use `GET /cloud/logs/syslog` to:

- Retrieve OS-level events for troubleshooting system startup, network changes, or service crashes
- Investigate unexpected reboots or hardware-related events
- Capture system logs before a reader restart resets the log buffer

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is the expected log file returned? | Confirms the correct log type was retrieved. |
| `content` | Are there kernel, network, or service failure messages? | Syslog captures low-level OS events that application logs may not surface, making it essential for diagnosing platform-level issues. |
