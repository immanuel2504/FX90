# `PUT /cloud/ntpServer` - REST Endpoint Reference

## 1. Description

The `PUT /cloud/ntpServer` REST endpoint is used to set NTP server.

Use this endpoint to:

- Set NTP server.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/ntpServer` |
| Operation ID | `updateNtpServer` |
| MQTT Command | `set_ntpServer` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_ntpServer` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
