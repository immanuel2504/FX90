## 1. Description

The `set_region` command updates the reader's RF region and the regulatory standard applied during inventory.

This command allows you to configure:

- The deployment country through `country`
- The regulatory standard to apply through `standardname`

Use this command to:

- Set the correct RF region before first use in a deployment country
- Switch the reader to a different region when relocating hardware
- Apply a specific regulatory standard within a multi-standard country

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Region Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_region](get_region.md), [get_SupportedRegionList](get_SupportedRegionList.md), [get_supportedStandardList](get_supportedStandardList.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | `country`, `standardname` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Verify the target country and standard are supported before sending this command. Applying an incorrect region may make the reader non-compliant with local RF regulations.

| What You Need | Details |
|---|---|
| Country name | Use `get_SupportedRegionList` to retrieve the exact country name string accepted by the reader. |
| Standard name | Use `get_supportedStandardList` to retrieve valid standard names for the target country. |
| Active inventory | Stop inventory with `stop` before changing region. Region changes take effect immediately and affect all RF parameters. |
| LBT and channel behavior | Some standards mandate LBT always-on or restrict channel usage. Review the standard entry from `get_supportedStandardList` before applying. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or result in non-compliant RF behavior.

### Country and Standard

- Both `country` and `standardname` are required in the payload. Omitting either field will cause the command to be rejected.
- The `country` value must exactly match a country name returned by `get_SupportedRegionList`. An unrecognized country string will be rejected.
- The `standardname` must be a valid standard for the specified country, as returned by `get_supportedStandardList`. Pairing a country with an incompatible standard name will be rejected.

### Apply Timing

- Region changes are applied immediately. The reader updates its RF parameters, channel list, LBT state, and transmit power limits as soon as the command is acknowledged.
- If inventory is active when this command is sent, behavior is undefined — stop inventory first.

### Security Note

- No credentials or secrets are required in the `set_region` payload. Do not include authentication data in region configurations.
