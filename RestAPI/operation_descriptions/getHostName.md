# `GET /cloud/hostName` - REST Endpoint Reference

## 1. Description

The `GET /cloud/hostName` REST endpoint is used to retrieves reader hostname.

Use this endpoint to:

- Retrieves reader hostname.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/hostName` |
| Operation ID | `getHostName` |
| MQTT Command | `get_hostName` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_hostName` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
