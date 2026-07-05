The `PUT /cloud/mode` REST endpoint configures the reader's operating mode using the same `operatingMode.v1` payload shape supported by the MQTT `set_mode` command.

## 2. Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Configuration |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 Series |
| REST Endpoint | `PUT /cloud/mode` |
| Request Schema | `operatingMode.v1` |
| Related Endpoints | `GET /cloud/mode`, `PUT /cloud/start`, `PUT /cloud/stop`, `GET /cloud/config` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |

## 3. Before You Begin

Changing mode while inventory is active can disrupt reads. Stop inventory first with `PUT /cloud/stop` if the reader is currently running.

| What You Need | Details |
|---|---|
| Mode type | One of `SIMPLE`, `INVENTORY`, `PORTAL`, `CONVEYOR`, `CUSTOM`, or `DIRECTIONALITY`. |
| Antennas or beams | Antenna ports or ATR beam settings used for inventory. |
| RF settings | Transmit power, environment profile, query settings, select operations, and optional access operations. |
| Mode-specific settings | Inventory interval, portal trigger settings, or directionality zone/beam configuration, depending on `type`. |
| Reporting settings | Metadata, report filter, RSSI filter, and optional radio start/stop conditions. |

## 4. Schema Alignment

The request schema is aligned with MQTT `set_mode`. Any mode configuration supported by MQTT should be accepted by REST with the same field name, nested object shape, enum values, and description.
