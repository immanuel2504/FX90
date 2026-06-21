## 1. Description

The `GET /cloud/mode` REST endpoint retrieves the reader's current operating mode and all associated configuration settings.

This endpoint returns:

- Operating mode type (`SIMPLE`, `INVENTORY`, `PORTAL`, `CONVEYOR`, `CUSTOM`, or `DIRECTIONALITY`)
- Configured antennas or beams and their transmit power values
- Environment profile setting
- Mode-specific settings (portal, conveyor, directionality, etc.)
- Gen2 query, select, and access settings
- Report filtering, RSSI filtering, metadata fields, and radio start/stop conditions

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/mode` |
| Operation ID | `getMode` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Equivalent | `get_mode` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/mode` to:

- Review the full current mode configuration before calling `PUT /cloud/mode`
- Confirm antenna transmit power settings before starting inventory
- Audit the environment profile and mode type across a fleet
- Check tag reporting and RSSI filter settings before a site validation

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `modeType` | Is the mode type correct for this application? | Controls fundamental read behavior — portal, conveyor, or inventory logic. |
| `antennas` | Are the right ports enabled with expected transmit power? | Misconfigured antennas will result in missed reads or coverage gaps. |
| `txPower` | Is the power level within regulatory limits? | Transmit power must stay below the regional maximum set in `GET /cloud/region`. |
| `environmentProfile` | Is the profile matched to the deployment environment? | Profile influences sensitivity and false-read filtering in dense environments. |
