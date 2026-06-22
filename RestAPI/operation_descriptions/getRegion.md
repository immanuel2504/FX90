## 1. Description

The `GET /cloud/region` REST endpoint retrieves the reader's currently configured RF region and the regulatory parameters in effect.

This endpoint returns:

- The active region code and country name
- The regulatory standard currently applied
- Listen Before Talk (LBT) and frequency hopping state
- Enabled channel list for the active region
- Minimum and maximum transmit power supported

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/region` |
| Operation ID | `getRegion` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_region` |
| MQTT Equivalent | `get_region` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/region` to:

- Confirm the reader is set to the correct regulatory region before deployment
- Verify LBT and channel configuration before inventory
- Audit transmit power limits for the active region

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `country` | Is the correct country configured? | The reader must match the regulatory region of its deployment location. |
| `regulatoryStandard` | Which standard is applied? | Determines transmission rules - channels, power limits, and LBT behavior. |
| `lbtEnabled` | Is Listen Before Talk active? | Required in some regions (e.g., ETSI). Affects when the radio may transmit. |
| `FrequencyHopping` | Is frequency hopping enabled? | Mandatory in most regions; confirms compliant radio operation. |
| `maxTxPowerSupported` | What is the allowed power ceiling? | Use to validate transmit power settings before starting inventory. |
