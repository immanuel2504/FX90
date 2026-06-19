# `GET /cloud/readerLocation` - REST Endpoint Reference

## 1. Description

The `GET /cloud/readerLocation` REST endpoint is used to gets the GPS coordinates (lat/long).

Use this endpoint to:

- Gets the GPS coordinates (lat/long).
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/readerLocation` |
| Operation ID | `getGpsCoordinates` |
| MQTT Command | `get_gpsCoordinates` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_gpsCoordinates` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
