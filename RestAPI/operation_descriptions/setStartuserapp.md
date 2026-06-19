# `PUT /cloud/apps/{appname}/start` - REST Endpoint Reference

## 1. Description

The `PUT /cloud/apps/{appname}/start` REST endpoint is used to start user application.

Use this endpoint to:

- Start user application.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/apps/{appname}/start` |
| Operation ID | `setStartuserapp` |
| MQTT Command | `start_user_app` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `start_user_app` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
