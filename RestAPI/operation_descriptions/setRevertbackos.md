The `PUT /cloud/revertbackOS` REST endpoint is used to revert to previous OS version.

Use this endpoint to:

- Revert to previous OS version.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `revertback` |
| REST Endpoint | `PUT /cloud/revertbackOS` |
| Operation ID | `setRevertbackos` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `revertback` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
