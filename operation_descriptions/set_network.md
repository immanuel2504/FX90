The `set_network` command updates reader network configuration using the same per-interface request shape as REST `PUT /cloud/network`.

Use it to:

- Configure Ethernet (`eth0`) DHCP, static IPv4/IPv6, and 802.1X security
- Configure Wi-Fi station (`mlan0`) DHCP, static addressing, and access point security
- Configure Bluetooth PAN (`bnep0`)
- Configure cellular WAN (`wan0`)
- Configure Wi-Fi hotspot (`uap0`)

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Network Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_network](get_network.md), [set_hostname](set_hostname.md), [get_hostname](get_hostname.md), [get_networkInterfaces](get_networkInterfaces.md) |
| Supported Operations | Configure one network interface per request |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the command. A wrong static IP, gateway, Wi-Fi credential, or cellular setting can disconnect the reader from your network.

| What You Need | Details |
|---|---|
| Interface key | Provide exactly one of `eth0`, `mlan0`, `bnep0`, `wan0`, or `uap0`. |
| IP settings | Use `IPV4` / `IPV6` with `dhcp: true`, or provide static address fields when DHCP is false. |
| Interface enablement | Use `enable: true` or `enable: false` on the selected interface. |
| Security details | For Ethernet/Wi-Fi security, include the interface-specific `security` or `accesspoint.security` object. |

## 4. Payload Shape

The payload is an object with one interface name as the top-level key. The value contains the configuration for that interface.
