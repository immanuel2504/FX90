## 1. Description

The `GET /cloud/status` REST endpoint retrieves operational statistics and health information from the reader at the moment of the request.

This endpoint returns:

- Uptime and current system time
- Radio connection and activity state
- Reader temperature
- CPU and RAM usage
- Flash storage usage by partition
- Antenna port connection states
- NTP synchronization status
- Cloud interface connection status

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/status` |
| Operation ID | `getStatus` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_status` |
| MQTT Equivalent | `get_status` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/status` to:

- Confirm the reader is powered, healthy, and reachable over REST
- Verify the radio is connected before starting inventory
- Monitor reader temperature, CPU, and RAM usage
- Synchronize against the reader's current system time

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `uptime` | How long has the reader been running? | Long uptimes confirm stability; short uptimes indicate an unexpected restart. |
| `radioConnection` | Is the value `connected`? | Inventory cannot run if the radio is disconnected. |
| `temperature` | Is the value within safe operating range? | Excessive temperature can cause throttling or hardware faults. |
| `antennas` | Are expected ports `connected`? | A `disconnected` antenna port means tags on that port will not be read. |
