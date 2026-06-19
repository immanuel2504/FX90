# `GET /cloud/status` - REST Endpoint Reference

## 1. Description

The `GET /cloud/status` REST endpoint is used to retrieves reader operational statistics.

Use this endpoint to:

- Retrieves reader operational statistics.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/status` |
| Operation ID | `getStatus` |
| MQTT Command | `get_status` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_status` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
