## 1. Description

The `GET /cloud/hostName` REST endpoint retrieves the reader's current network hostname.

This endpoint returns:

- The hostname string currently assigned to the reader

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/hostName` |
| Operation ID | `getHostName` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Equivalent | `get_hostname` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/hostName` to:

- Verify the hostname assigned to a reader during provisioning
- Confirm the hostname matches the expected naming convention for the deployment
- Retrieve the hostname before updating it with `PUT /cloud/hostName`

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `hostname` | Does it match the expected value? | The hostname identifies the reader on the network and in management systems; a mismatch may indicate the wrong reader was configured. |
