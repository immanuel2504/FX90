## 1. Description

The `GET /cloud/cableLossCompensation` REST endpoint retrieves the cable loss compensation values currently configured for each read point on the reader.

This endpoint returns:

- The cable length and the attenuation value (in dBm) configured per read point

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/cableLossCompensation` |
| Operation ID | `getCablelosscompensation` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_cableLossCompensation` |
| MQTT Equivalent | `get_cableLossCompensation` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/cableLossCompensation` to:

- Review cable loss settings before tuning transmit power for a deployment
- Confirm compensation values match physical cable lengths at each antenna port
- Verify the effect of a prior `PUT /cloud/cableLossCompensation` call

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `cableLength` | Does the configured length match the physical cable run? | An incorrect cable length will produce inaccurate loss compensation and reduce read range. |
| `cableLoss` (per read point) | Is the attenuation value consistent with the cable spec? | Mismatched values result in too little or too much transmit power after compensation is applied. |
