# `PUT /cloud/hostName` - REST Endpoint Reference

## 1. Description

The `PUT /cloud/hostName` REST endpoint is used to sets reader hostname.

Use this endpoint to:

- Sets reader hostname.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/hostName` |
| Operation ID | `setHostName` |
| MQTT Command | `set_hostName` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_hostName` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
