The `PUT /cloud/updatePassword` REST endpoint is used to changes the password on the reader.

Use this endpoint to:

- Changes the password on the reader.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/updatePassword` |
| Description Key | `PUT__cloud__updatePassword` |
| MQTT Command | `set_password` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_password` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
