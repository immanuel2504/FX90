## Description

The `get_networkInterfaces` command retrieves the network interfaces available on the reader.

Use this command to:

- See which network interfaces the reader exposes
- Confirm Ethernet, Wi-Fi, Bluetooth network, or cellular interface availability
- Troubleshoot network configuration before using `get_network` or `set_network`

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Network Interface Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_network](get_network.md), [set_network](set_network.md), [get_eSimConfig](get_eSimConfig.md) |
| Supported Operations | Retrieve available network interfaces |
| Supported API Versions | V1.0 |

## Before You Begin

No network configuration payload is required. Send an empty `payload` object and use the response to decide which interface names can be used in later network commands.
