## 1. Description

The `GET /cloud/supportedStandardList` REST endpoint retrieves the list of regulatory standards and their associated channel data supported by this reader.

This endpoint returns:

- The list of regulatory standard names supported for each region
- Channel data for each standard, including whether LBT is configurable

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/supportedStandardList` |
| Operation ID | `getSupportedstandardlist` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_SupportedStandardlist` |
| MQTT Equivalent | `get_supportedStandardList` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/supportedStandardList` to:

- Determine which regulatory standards are available before configuring a region
- Check whether LBT is configurable for a given standard
- Populate standard selection options in provisioning tools

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Standard names | Is the required standard listed? | Only listed standards can be applied when configuring the reader's RF region. |
| `lbtConfigurable` | Can LBT be toggled for this standard? | Some standards mandate LBT always-on; knowing this prevents invalid configuration attempts. |
| `channelData` | What channels are available for this standard? | Determines valid frequency channels for inventory operations under this standard. |
