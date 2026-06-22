## 1. Description

The `get_network` command retrieves the reader's complete network configuration across all interfaces.

This command returns:

- The device hostname
- Ethernet (`eth0`) interface configuration and connection status
- Wi-Fi station (`mlan0`) interface configuration and access point details
- Bluetooth PAN (`bnep0`) configuration and status
- Cellular (`wan0`) configuration and status
- Wi-Fi hotspot (`uap0`) configuration, connected clients, and status

No payload fields are required to retrieve the full network configuration.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Network Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/network` |
| Related Commands | [set_network](set_network.md), [get_hostname](get_hostname.md), [get_networkInterfaces](get_networkInterfaces.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve active network configuration for all interfaces |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_network` to:

- Confirm the reader's IP addressing before changing it
- Verify which interfaces are connected or enabled
- Audit network identity and interface status across a fleet
- Review Wi-Fi, Bluetooth, cellular, and hotspot state during connectivity troubleshooting

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `eth0` | Is the Ethernet interface connected and has an IP? | Primary connectivity path; must be up for cloud communication over wired LAN. |
| `mlan0` | Is Wi-Fi associated and which SSID? | Confirms the correct access point is in use for wireless deployments. |
| `wan0` | Is cellular connected and have a carrier? | Required for deployments relying on cellular backhaul. |
| `uap0` | Is the hotspot enabled and are clients connected? | Used to confirm hotspot provisioning mode is active. |
| `hostname` | Does the hostname match expected naming? | Used for device identification on the local network and in management systems. |
