# `GET /cloud/mode` - REST Endpoint Reference

## 1. Description

The `GET /cloud/mode` REST endpoint retrieves the reader's current operating mode using the same `operatingMode.v1` schema used by the MQTT `get_mode` response payload.

This endpoint returns:

- Operating mode type (`SIMPLE`, `INVENTORY`, `PORTAL`, `CONVEYOR`, `CUSTOM`, or `DIRECTIONALITY`)
- Antennas or beams and transmit power
- Environment profile
- Mode-specific settings
- Gen2 query/select/access settings
- Report filtering, RSSI filtering, metadata, and radio start/stop conditions

## 2. Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Query |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 Series |
| REST Endpoint | `GET /cloud/mode` |
| MQTT Command | `get_mode` |
| Response Schema | `operatingMode.v1` |
| Related Endpoints | `PUT /cloud/mode`, `PUT /cloud/start`, `PUT /cloud/stop` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. Schema Alignment

The response schema is aligned with MQTT `get_mode`. Any mode field supported in the MQTT `get_mode` response should be represented in the REST response using the same field name, nested object shape, enum values, and description.
