## 1. Description

The `GET /cloud/network` REST endpoint retrieves the reader's complete network configuration across all interfaces.

This endpoint returns:

- The device hostname
- Ethernet (`eth0`) interface configuration and connection status
- Wi-Fi station (`mlan0`) interface configuration and access point details
- Bluetooth PAN (`bnep0`) configuration and status
- Cellular (`wan0`) configuration and status
- Wi-Fi hotspot (`uap0`) configuration, connected clients, and status

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/network` |
| Operation ID | `getNetwork` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_network` |
| MQTT Equivalent | `get_network` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/network` to:

- Confirm the reader's IP addressing before changing network settings
- Verify which interfaces are connected or enabled
- Audit network identity and interface status across a fleet
- Troubleshoot Wi-Fi, Bluetooth, cellular, or hotspot connectivity

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `eth0` | Is Ethernet connected and does it have an IP? | Primary connectivity path; must be up for cloud communication over wired LAN. |
| `mlan0` | Is Wi-Fi associated and which SSID? | Confirms the correct access point is in use for wireless deployments. |
| `wan0` | Is cellular connected and has a carrier? | Required for deployments relying on cellular backhaul. |
| `hostname` | Does the hostname match expected naming? | Used for device identification on the network and in management systems. |
