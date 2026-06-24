## 1. Description

The `GET /cloud/supportedRegionList` REST endpoint retrieves the list of RF regulatory regions supported by this reader.

This endpoint returns:

- The list of supported region codes for this reader model

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/supportedRegionList` |
| Operation ID | `getSupportedregionlist` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_SupportedRegionList` |
| MQTT Equivalent | `get_SupportedRegionList` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/supportedRegionList` to:

- Validate that the target deployment region is supported before calling `PUT /cloud/region`
- Populate a region selection UI with only region codes valid for this reader model
- Audit region support across different reader hardware variants in the same fleet

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Region list | Is the deployment region in the list? | Attempting to configure an unsupported region will result in an error or non-compliant behavior. |
