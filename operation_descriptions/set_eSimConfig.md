## 1. Description

The `set_eSimConfig` command updates the eSIM profile state on the reader.

This command allows you to configure:

- The eSIM operation to perform through `operation`
- The target profile nickname through `profileNickName`

Use this command to:

- Enable a specific eSIM carrier profile on the reader
- Switch between installed eSIM profiles for different cellular network providers
- Apply eSIM provisioning changes from your carrier management system

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | eSIM Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/eSimConfig` |
| Related Commands | [get_eSimConfig](get_eSimConfig.md), [get_network](get_network.md), [set_network](set_network.md) |
| Supported Operations | `enable`, `disable` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Use `get_eSimConfig` first to retrieve the exact profile nickname available on the reader before sending this command.

| What You Need | Details |
|---|---|
| Operation | The eSIM operation to perform: `enable` to activate the selected profile, or `disable` to deactivate it. |
| Profile nickname | The exact nickname of the eSIM profile to enable, as returned by `get_eSimConfig`. The nickname must match exactly - case-sensitive. |
| Active SIM setting | After enabling an eSIM profile, confirm the `wan0.activeSim` is set to `esim` in the network configuration (see `set_network`) for the profile to be used for data. |

