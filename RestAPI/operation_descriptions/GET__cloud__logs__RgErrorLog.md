# `GET /cloud/logs/RgErrorLog` - REST Endpoint Reference

## 1. Description

The `GET /cloud/logs/RgErrorLog` REST endpoint is used to retrieve RgErrorLog.

Use this endpoint to:

- Retrieve RgErrorLog.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/logs/RgErrorLog` |
| Description Key | `GET__cloud__logs__RgErrorLog` |
| MQTT Command | `get_logs_rgErrorLog` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_logs_rgErrorLog` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
