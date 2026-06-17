## 1. Description

The `get_network` command retrieves the reader's network configuration across its interfaces.

This command returns:

- The device hostname
- Ethernet (`eth0`) interface configuration and status
- Wi-Fi (`mlan0`) interface configuration

No additional payload fields are required to retrieve the full network configuration.

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
- Verify which interface (Ethernet/Wi-Fi) is connected
- Audit network identity (hostname) across devices
- Review interface status during connectivity troubleshooting
