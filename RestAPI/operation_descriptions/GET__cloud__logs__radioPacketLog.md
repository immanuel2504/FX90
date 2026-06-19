# `GET /cloud/logs/radioPacketLog` - REST Endpoint Reference

## 1. Description

The `GET /cloud/logs/radioPacketLog` REST endpoint is used to retrieve radioPacketLog.

Use this endpoint to:

- Retrieve radioPacketLog.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/logs/radioPacketLog` |
| Description Key | `GET__cloud__logs__radioPacketLog` |
| MQTT Command | `get_logs_radioPacketLog` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_logs_radioPacketLog` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
