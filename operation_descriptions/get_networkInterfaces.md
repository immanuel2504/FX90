## 1. Description

The `get_networkInterfaces` command retrieves network interface information from the reader.

Use this command to:

- List available Ethernet and Wi-Fi interfaces
- Troubleshoot interface-level connectivity

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Network Interface Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_network](get_network.md), [set_network](set_network.md) |
| Required Request Fields | `command`, `command_id` |
| Supported Operations | Retrieve network interface details |
| Supported Response Sections | payload |
| Supported API Versions | V1.0 |
