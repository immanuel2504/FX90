The `PUT /cloud/apps/{appname}/stop` REST endpoint is used to stop user application.

Use this endpoint to:

- Stop user application.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `stop_user_app` |
| REST Endpoint | `PUT /cloud/apps/{appname}/stop` |
| Operation ID | `setStopuserapp` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `stop_user_app` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
