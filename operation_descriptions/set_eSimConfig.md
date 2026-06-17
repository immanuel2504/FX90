## Description

The `set_eSimConfig` command updates the eSIM profile state on the reader.

Use this command to:

- Enable a specific eSIM profile
- Change cellular provisioning behavior
- Apply a profile nickname returned by `get_eSimConfig`

## Command Details

| Property | Value |
|---|---|
| Pattern Name | eSIM Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_eSimConfig](get_eSimConfig.md), [get_network](get_network.md), [set_network](set_network.md) |
| Supported Operations | Set eSIM configuration |
| Supported API Versions | V1.0 |

## Before You Begin

Run `get_eSimConfig` first if you need the exact profile nickname. The nickname in the request must match a profile known to the reader.
