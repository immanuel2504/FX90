# `GET /cloud/preSelection` - REST Endpoint Reference

## 1. Description

The `GET /cloud/preSelection` REST endpoint is used to returns whether the rxSawFilter is enabled or disabled.

Use this endpoint to:

- Returns whether the rxSawFilter is enabled or disabled.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/preSelection` |
| Description Key | `GET__cloud__preSelection` |
| MQTT Command | `get_preSelection` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_preSelection` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
