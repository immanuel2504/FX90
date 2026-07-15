## 1. Description

The `set_network` command updates reader network configuration for a single interface per request.

This command allows you to configure:

- Ethernet (`eth0`) - DHCP, static IPv4/IPv6 addressing, and 802.1X security
- Wi-Fi station (`mlan0`) - DHCP, static addressing, access point connection, and WPA2/WPA3/Enterprise security
- Bluetooth PAN (`bnep0`) - discoverability, pairing, and DHCP address pool
- Cellular WAN (`wan0`) - SIM selection, APN, network type preference, and IPv6
- Wi-Fi hotspot (`uap0`) - SSID, password, country code, and security type

Use this command to:

- Connect the reader to a new Wi-Fi access point
- Switch from DHCP to static IP addressing on Ethernet
- Enable or disable a network interface
- Configure cellular APN and SIM settings
- Provision a Wi-Fi hotspot on the reader

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Network Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/network` |
| Related Commands | [get_network](get_network.md), [get_networkInterfaces](get_networkInterfaces.md), [set_hostname](set_hostname.md) |
| Supported Interface Keys | `eth0`, `mlan0`, `bnep0`, `wan0`, `uap0` |
| Supported Wi-Fi Security Types | `WPA2Personal`, `WPA2Enterprise`, `WPA3Personal`, `WPA3Enterprise` |
| Supported 802.1X Authentication | `TLS`, `TTLS`, `PEAP` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather all interface-specific settings before sending this command. A wrong static IP, gateway, Wi-Fi credential, or cellular setting can disconnect the reader from your network.

| What You Need | Details |
|---|---|
| Interface key | Include exactly one top-level interface key: `eth0`, `mlan0`, `bnep0`, `wan0`, or `uap0`. Only one interface can be configured per request. |
| Hotspot vs Wi-Fi client | `uap0` (hotspot) and `mlan0` (Wi-Fi client) share the same Wi-Fi radio and **cannot be active at the same time**. Enabling one disables the other. |
| IP addressing | Use `IPV4.dhcp: true` for dynamic addressing, or supply `ipAddress`, `subnetMask`, `gatewayAddress`, and `dnsAddress` for static. |
| Wi-Fi access point | For `mlan0`, include the `accesspoint` object with `essid`, `connect`, `autoConn`, and the `security` sub-object. |
| Wi-Fi security | For WPA2 Personal, provide the `password`. For WPA2 Enterprise, provide `authentication` type and either a certificate name (TLS) or credentials (TTLS/PEAP). |
| Cellular settings | For `wan0`, set `activeSim` (`psim` or `esim`) and supply the `apn` and `preferredNetworkType` for the chosen SIM. |
| Hotspot settings | For `uap0`, provide `ssid`, `ssidPassword`, `countryCode`, `securityType` (`WPA2Personal` or `WPA3Personal` only), and `isHidden`. |
| Interface enablement | Always include `enable: true` or `enable: false` on the interface object to control whether the interface is active after configuration. |

> Important: `uap0` and `mlan0` are mutually exclusive. The reader has one Wi-Fi radio, which operates either as a client joining an access point (`mlan0`) or as an access point of its own (`uap0`) — never both. Publishing `uap0` with `enable: true` while `mlan0` is connected drops the Wi-Fi client connection, and vice versa. Configure them in separate commands and enable only the one you intend to run. If the reader's only route to your network is `mlan0`, enabling the hotspot will disconnect it.

