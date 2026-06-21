## 1. Description

The `GET /cloud/logs/radioPacketLog` REST endpoint retrieves the radio packet log file from the reader.

This endpoint returns:

- The log filename
- The full content of the radio packet log

No request body is required. Radio packet logging must be enabled via `PUT /cloud/logs` before this endpoint will return meaningful data.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/logs/radioPacketLog` |
| Operation ID | `GET__cloud__logs__radioPacketLog` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Equivalent | `get_radio_pkt_logs` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/logs/radioPacketLog` to:

- Download RF-level packet data for deep diagnostics of inventory performance
- Analyze raw radio events to investigate tag read anomalies or read rate issues
- Retrieve packet logs after a troubleshooting session before clearing or restarting the reader

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `filename` | Is the expected log file returned? | Confirms the correct log type was retrieved. |
| `content` | Does the log contain RF packet data? | An empty file means radio packet logging was not enabled when the events occurred. |
