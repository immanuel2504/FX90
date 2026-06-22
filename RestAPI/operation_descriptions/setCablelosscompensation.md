The `PUT /cloud/cableLossCompensation` REST endpoint is used to sets the cableLossCompensation.

Use this endpoint to:

- Sets the cableLossCompensation.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `set_cableLossCompensation` |
| REST Endpoint | `PUT /cloud/cableLossCompensation` |
| Operation ID | `setCablelosscompensation` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_cableLossCompensation` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
