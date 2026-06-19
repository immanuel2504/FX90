# `GET /cloud/localRestLogin` - REST Endpoint Reference

## 1. Description

The `GET /cloud/localRestLogin` REST endpoint is used to reader Login.

Use this endpoint to:

- Reader Login.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/localRestLogin` |
| Operation ID | `localrestlogin` |
| MQTT Command | `localrest_login` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `localrest_login` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
