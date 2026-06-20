The `DELETE /cloud/certificates/{certname}` REST endpoint is used to delete certificate.

Use this endpoint to:

- Delete certificate.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `DELETE /cloud/certificates/{certname}` |
| Operation ID | `delCertificate` |
| MQTT Command | `del_certificate` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `del_certificate` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
