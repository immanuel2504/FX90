The `PUT /cloud/apps/{appname}/autostart` REST endpoint is used to autostart user application.

Use this endpoint to:

- Autostart user application.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `autostart_user_app` |
| REST Endpoint | `PUT /cloud/apps/{appname}/autostart` |
| Operation ID | `setAutostartuserapp` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `autostart_user_app` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
