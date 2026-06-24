## 1. Description

The `get_networkInterfaces` command retrieves the network interfaces available on the reader.

This command returns:

- The list of network interface names available on this reader (e.g., `eth0`, `mlan0`, `wan0`, `bnep0`, `uap0`)

No additional payload fields are required to retrieve the interface list.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Network Interface Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/networkInterfaces` |
| Related Commands | [get_network](get_network.md), [set_network](set_network.md), [get_eSimConfig](get_eSimConfig.md) |
| Supported Operations | Retrieve available network interface names |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_networkInterfaces` to:

- Identify which network interfaces are present before configuring them via `set_network`
- Confirm Ethernet, Wi-Fi, Bluetooth, or cellular interface availability on this reader model
- Use returned interface names as valid keys in subsequent network configuration calls

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Interface list | Are all expected interfaces present (`eth0`, `mlan0`, `wan0`)? | Only interfaces returned here can be configured in `set_network`. |
| `wan0` presence | Is the cellular interface listed? | Confirms whether the reader hardware supports cellular connectivity. |
