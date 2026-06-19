# `PUT /cloud/gpo` - REST Endpoint Reference

## 1. Description

The `PUT /cloud/gpo` REST endpoint is used to updates GPO port state.

Use this endpoint to:

- Updates GPO port state.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/gpo` |
| Operation ID | `setGpo` |
| MQTT Command | `set_gpo` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_gpo` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
