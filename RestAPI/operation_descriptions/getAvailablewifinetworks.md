The `GET /cloud/wifiNetworks` REST endpoint is used to retrieves available Wi-Fi networks.

Use this endpoint to:

- Retrieves available Wi-Fi networks.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/wifiNetworks` |
| Operation ID | `getAvailablewifinetworks` |
| MQTT Command | `get_availableWifiNetworks` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `get_availableWifiNetworks` MQTT command where applicable.

Review the request and response schemas in the REST API reference for required fields, optional fields, enum values, and examples before calling this endpoint.
