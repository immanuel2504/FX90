## 1. Description

The `get_SupportedRegionList` command retrieves the list of RF regions this reader is permitted to operate in.

This command returns:

- The set of supported country or region names that can be applied via `set_region`

No additional payload fields are required to retrieve the supported region list.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Supported Region Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/supportedRegionList` |
| Related Commands | [get_region](get_region.md), [set_region](set_region.md), [get_supportedStandardList](get_supportedStandardList.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the list of permitted RF regions for this reader |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_SupportedRegionList` to:

- Determine valid values before calling `set_region`
- Confirm that the target deployment region is supported by this hardware
- Build a region picker in a provisioning or configuration UI

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Region list | Is the target deployment region present? | Attempting to set an unsupported region via `set_region` will result in an error. |
