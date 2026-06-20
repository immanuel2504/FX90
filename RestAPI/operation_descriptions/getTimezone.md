The `GET /cloud/timeZone` REST endpoint is used to retrieves the reader timezone.

Use this endpoint to:

- Retrieves the reader timezone.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/timeZone` |
| Operation ID | `getTimezone` |
| MQTT Command | `get_timeZone` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_timeZone` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
