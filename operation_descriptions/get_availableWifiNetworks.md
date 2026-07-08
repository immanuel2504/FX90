## 1. Description

The `get_availableWifiNetworks` command triggers a Wi-Fi scan and retrieves the list of all visible Wi-Fi networks in the reader's vicinity.

This command returns:

- The ESSID (network name) of each visible access point
- The current signal strength of each network as a percentage
- The security protocols and capabilities supported by each access point (e.g., WPA2, WPA3, 802.1X)
- Any existing saved configuration profiles on the reader for these networks, including auto-connect behavior and enterprise security details

No additional payload fields are required to initiate the scan.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Wi-Fi Site Survey |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/wifiNetworks` |
| Related Commands | [get_networkInterfaces](get_networkInterfaces.md), [get_network](get_network.md), [set_network](set_network.md) |
| Supported Operations | Retrieve visible Wi-Fi networks and saved connection profiles |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_availableWifiNetworks` to:

- Perform a remote site survey to evaluate Wi-Fi coverage in the reader's physical location
- Troubleshoot wireless connectivity by verifying the target network is broadcasting with adequate signal strength
- Identify the security protocols required by local access points before pushing a new network configuration
- Audit which networks have saved profiles configured to `autoConnect`

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `essid` | Is the target network visible? | If the network is not listed, the reader cannot connect to it regardless of configuration. |
| `signalStrength` | What is the signal strength percentage? | Low signal causes unstable connectivity and increased retransmissions. |
| `security.type` | What security type is required (WPA2, WPA3, 802.1X)? | The network configuration in `set_network` must match the access point's security requirements. |
| `autoConnect` | Is a saved profile configured for auto-connect? | Confirms whether the reader will reconnect to this network automatically after a restart. |
