The `PUT /cloud/apps/{appname}/uninstall` REST endpoint is used to uninstall User Application.

Use this endpoint to:

- Uninstall User Application.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `uninstall-user-app` |
| REST Endpoint | `PUT /cloud/apps/{appname}/uninstall` |
| Operation ID | `setUninstalluserapp` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `uninstall-user-app` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
