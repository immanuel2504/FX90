The `GET /cloud/supportedRegionList` REST endpoint is used to retrieves the supported region list based on the reader type.

Use this endpoint to:

- Retrieves the supported region list based on the reader type.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/supportedRegionList` |
| Operation ID | `getSupportedregionlist` |
| MQTT Command | `get_SupportedRegionList` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_SupportedRegionList` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
