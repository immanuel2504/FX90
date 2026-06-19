# `GET /cloud/eSimConfig` - REST Endpoint Reference

## 1. Description

The `GET /cloud/eSimConfig` REST endpoint is used to gets the eSIM configuration.

Use this endpoint to:

- Gets the eSIM configuration.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/eSimConfig` |
| Description Key | `GET__cloud__eSimConfig` |
| MQTT Command | `get_eSimConfig` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_eSimConfig` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
