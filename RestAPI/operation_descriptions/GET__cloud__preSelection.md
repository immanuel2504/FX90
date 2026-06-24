## 1. Description

The `GET /cloud/preSelection` REST endpoint retrieves the current rxSawFilter pre-selection state from the reader.

This endpoint returns:

- Whether the rxSawFilter (receive SAW filter pre-selection) is enabled or disabled

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/preSelection` |
| Operation ID | `GET__cloud__preSelection` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Equivalent | `get_preSelection` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/preSelection` to:

- Check whether rxSawFilter is enabled or disabled before starting inventory
- Verify RF pre-selection state in deployments where receiver filtering is important
- Confirm the effect of a prior `PUT /cloud/preSelection` call

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `rxSawFilter` | Is the filter enabled or disabled? | Enabling the SAW filter improves receiver selectivity in noisy RF environments but may reduce sensitivity in clean environments. |
