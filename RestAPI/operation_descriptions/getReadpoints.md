# `GET /cloud/readPoints` - REST Endpoint Reference

## 1. Description

The `GET /cloud/readPoints` REST endpoint is used to gets the read points on the reader.

Use this endpoint to:

- Gets the read points on the reader.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/readPoints` |
| Operation ID | `getReadpoints` |
| MQTT Command | `get_readPoints` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_readPoints` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
