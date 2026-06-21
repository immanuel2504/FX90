The `GET /cloud/readerCapabilities` REST endpoint is used to retrieves the Reader Capabilities.

Use this endpoint to:

- Retrieves the Reader Capabilities.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/readerCapabilities` |
| Operation ID | `getReaderCapabilities` |
| MQTT Command | `get_readerCapabilities` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_readerCapabilities` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
