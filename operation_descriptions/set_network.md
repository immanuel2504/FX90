## 1. Description

The `set_network` command configures the reader's network identity and IP settings (DHCP or static).

Use it to:

- Set the reader hostname and MAC-referenced network parameters
- Enable DHCP or configure static IPv4 addressing
- Update gateway, subnet mask, and DNS for static deployments

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Network Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_network](get_network.md), [set_hostname](set_hostname.md), [get_hostname](get_hostname.md) |
| Supported Operations | Configure network addressing |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the command. A wrong static IP or gateway can disconnect the reader from your network.

| What You Need | Details |
|---|---|
| Hostname | Desired reader hostname. |
| MAC address | Reader MAC address (as reported by `get_network`). |
| DHCP vs static | `dhcp: true` for automatic addressing, or `false` with full static details. |
| Static IP details | If DHCP disabled: `ipAddress`, `gatewayAddress`, `subnetMask`, `dnsAddress`. |
