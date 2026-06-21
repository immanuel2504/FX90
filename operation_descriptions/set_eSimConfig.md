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
| Related Commands | [get_eSimConfig](get_eSimConfig.md), [get_network](get_network.md), [set_network](set_network.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | `enable` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Use `get_eSimConfig` first to retrieve the exact profile nickname available on the reader before sending this command.

| What You Need | Details |
|---|---|
| Operation | The eSIM operation to perform. Currently supported: `enable`. |
| Profile nickname | The exact nickname of the eSIM profile to enable, as returned by `get_eSimConfig`. The nickname must match exactly — case-sensitive. |
| Active SIM setting | After enabling an eSIM profile, confirm the `wan0.activeSim` is set to `esim` in the network configuration (see `set_network`) for the profile to be used for data. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or the cellular interface to remain unchanged.

### Operation

- `operation` must be a supported value (`enable`). An unrecognized operation string will be rejected.

### Profile Nickname

- `profileNickName` must exactly match a profile nickname returned by `get_eSimConfig`. An unknown or mismatched nickname will cause the command to fail.
- The nickname comparison is case-sensitive. Use the exact string from the `get_eSimConfig` response.

### Apply Timing

- The eSIM profile change takes effect after the command is acknowledged. The cellular interface may restart to apply the new profile.
- Verify the profile is active by calling `get_eSimConfig` after the command completes.

### Security Note

- No credentials or secrets are required in the `set_eSimConfig` payload. Do not include authentication data in eSIM configuration requests.
