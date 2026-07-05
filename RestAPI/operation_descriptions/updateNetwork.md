The `PUT /cloud/network` REST endpoint updates network configuration, including Wi-Fi hotspot (uap0) settings.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `set_network` |
| REST Endpoint | `PUT /cloud/network` |
| Operation ID | `updateNetwork` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
