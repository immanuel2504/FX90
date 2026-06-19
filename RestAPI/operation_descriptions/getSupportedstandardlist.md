# `GET /cloud/supportedStandardList` - REST Endpoint Reference

## 1. Description

The `GET /cloud/supportedStandardList` REST endpoint is used to retrieves the standard channels of the supported regions.

Use this endpoint to:

- Retrieves the standard channels of the supported regions.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/supportedStandardList` |
| Operation ID | `getSupportedstandardlist` |
| MQTT Command | `get_supportedStandardList` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_supportedStandardList` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
