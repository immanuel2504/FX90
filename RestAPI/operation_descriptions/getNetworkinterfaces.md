## 1. Description

The `GET /cloud/networkInterfaces` REST endpoint retrieves the list of network interfaces available on the reader.

This endpoint returns:

- The list of network interface names available on this reader (e.g., `eth0`, `mlan0`, `wan0`, `bnep0`, `uap0`)

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/networkInterfaces` |
| Operation ID | `getNetworkInterfaces` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |

## 3. When to Use This Endpoint

Use `GET /cloud/networkInterfaces` to:

- Identify which network interfaces are present before configuring them via `PUT /cloud/network`
- Confirm Ethernet, Wi-Fi, Bluetooth, or cellular interface availability on this reader model
- Use returned interface names as valid keys in subsequent network configuration calls

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Interface list | Are all expected interfaces present? | Only interfaces listed here can be configured in `PUT /cloud/network`. |
| `wan0` presence | Is the cellular interface listed? | Confirms whether the reader hardware supports cellular connectivity. |
