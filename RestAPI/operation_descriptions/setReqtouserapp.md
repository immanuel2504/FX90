The `PUT /cloud/apps/{appname}/pass-through` REST endpoint is used to send Request to Userapp.

Use this endpoint to:

- Send Request to Userapp.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/apps/{appname}/pass-through` |
| Operation ID | `setReqtouserapp` |
| MQTT Command | `set_req_usr_app` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_req_usr_app` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
