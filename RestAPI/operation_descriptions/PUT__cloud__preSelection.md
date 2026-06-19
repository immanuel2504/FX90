# `PUT /cloud/preSelection` - REST Endpoint Reference

## 1. Description

The `PUT /cloud/preSelection` REST endpoint is used to enables or disables the rxSawFilter.

Use this endpoint to:

- Enables or disables the rxSawFilter.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/preSelection` |
| Description Key | `PUT__cloud__preSelection` |
| MQTT Command | `set_preSelection` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_preSelection` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
