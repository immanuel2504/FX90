## 1. Description

The `GET /cloud/wifiNetworks` REST endpoint triggers a Wi-Fi scan and returns all visible Wi-Fi networks in the reader's vicinity.

This endpoint returns:

- The ESSID (network name) of each visible access point
- Signal strength of each network as a percentage
- Supported security protocols and capabilities (WPA2, WPA3, 802.1X)
- Any existing saved Wi-Fi profiles on the reader, including auto-connect settings

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/wifiNetworks` |
| Operation ID | `getAvailablewifinetworks` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_availableWifiNetworks` |
| MQTT Equivalent | `get_availableWifiNetworks` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/wifiNetworks` to:

- Perform a remote site survey to evaluate Wi-Fi coverage at the reader's location
- Confirm the target network is broadcasting before pushing a new Wi-Fi configuration
- Identify the security type required by local access points
- Check which saved profiles are configured for auto-connect

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `essid` | Is the target network visible? | If the network is not listed, the reader cannot connect regardless of configuration. |
| `signal` | What is the signal strength percentage? | Low signal causes unstable connectivity and increased retransmissions. |
| `secProtocol` | What security type is required? | The network configuration must match the access point's security requirements. |
| `autoConnect` | Is a saved profile set to auto-connect? | Confirms whether the reader will reconnect to this network automatically after a restart. |
