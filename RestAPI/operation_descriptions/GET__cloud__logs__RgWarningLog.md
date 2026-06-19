# `GET /cloud/logs/RgWarningLog` - REST Endpoint Reference

## 1. Description

The `GET /cloud/logs/RgWarningLog` REST endpoint is used to retrieve RgWarningLog.

Use this endpoint to:

- Retrieve RgWarningLog.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/logs/RgWarningLog` |
| Description Key | `GET__cloud__logs__RgWarningLog` |
| MQTT Command | `get_logs_rgWarningLog` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_logs_rgWarningLog` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
