The `PUT /cloud/timeZone` REST endpoint is used to sets the timezone.

Use this endpoint to:

- Sets the timezone.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `set_timeZone` |
| REST Endpoint | `PUT /cloud/timeZone` |
| Operation ID | `setTimezone` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_timeZone` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
