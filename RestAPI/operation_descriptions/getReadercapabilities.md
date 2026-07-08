## 1. Description

The `GET /cloud/readerCapabilities` REST endpoint retrieves the hardware and protocol capabilities of the reader.

This endpoint returns:

- The number of GPI and GPO pins available
- Supported RFID protocols
- Supported endpoint types for tag data delivery
- Supported API versions

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/readerCapabilities` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. When to Use This Endpoint

Use `GET /cloud/readerCapabilities` to:

- Determine how many GPI and GPO pins are available before designing a trigger-based workflow
- Confirm which RFID protocols the reader supports before configuring inventory
- Verify API version support before using newer API features
- Audit hardware capabilities across a mixed fleet

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `numGPIs` | How many GPI pins are available? | Sets the upper limit for GPI-based trigger inputs. |
| `numGPOs` | How many GPO pins are available? | Sets the upper limit for GPO-driven outputs in workflows. |
| `protocols` | Which RFID protocols are supported? | Determines which tag types can be read - e.g., GS1 Gen2, ISO 18000-63. |
| `apiSupported.versions` | Which API versions are supported? | Ensures compatibility between management software and the reader firmware. |
