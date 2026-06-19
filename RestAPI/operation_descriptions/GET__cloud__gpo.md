# `GET /cloud/gpo` - REST Endpoint Reference

## 1. Description

The `GET /cloud/gpo` REST endpoint is used to retrieves the GPO status.

Use this endpoint to:

- Retrieves the GPO status.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/gpo` |
| Description Key | `GET__cloud__gpo` |
| MQTT Command | `get_gpoStatus` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_gpoStatus` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
