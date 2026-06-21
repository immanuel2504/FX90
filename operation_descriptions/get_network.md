The `get_network` command retrieves the reader network configuration using the same response shape as REST `GET /cloud/network`.

This command returns:

- The device hostname
- Ethernet (`eth0`) interface configuration and status
- Wi-Fi station (`mlan0`) interface configuration and access point details
- Bluetooth PAN (`bnep0`) configuration and status
- Cellular (`wan0`) configuration and status
- Wi-Fi hotspot (`uap0`) configuration, clients, and status

No payload fields are required to retrieve the full network configuration.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Network Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_network, get_hostname, get_networkInterfaces |
| Supported Operations | Retrieve active network configuration |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_network` to:

- Confirm the reader's IP addressing before changing it
- Verify which interfaces are connected or enabled
- Audit network identity and interface status across devices
- Review Wi-Fi, Bluetooth, cellular, and hotspot state during connectivity troubleshooting
