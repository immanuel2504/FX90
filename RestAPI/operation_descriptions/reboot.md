## 1. Description

The `PUT /cloud/reboot` REST endpoint restarts the reader.

All in-progress operations stop and the reader briefly disconnects until boot completes. No request body is required.

Use this endpoint to:

- Apply configuration changes that require a restart
- Recover from an unhealthy reader state
- Complete a firmware update cycle (the reader may also reboot automatically after `PUT /cloud/os`)

## 2. Before You Begin

Plan for downtime — the reader will disconnect until it finishes booting. In-flight inventory and active connections will be interrupted.

| What You Need | Details |
|---|---|
| Downtime window | Allow 1–3 minutes for reboot and reconnect |
| Authentication | Bearer token in the `Authorization` header |

## 3. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/reboot` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Request body | None |
