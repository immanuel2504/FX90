## 1. Description

The `get_supportedStandardList` command retrieves the list of RF regulatory standards supported by the reader and the channel details for each.

This command returns:

- Supported standard names
- LBT and hopping configurability per standard
- Enabled channel data per standard

No additional payload fields are required to retrieve the supported standard list.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Supported Standard Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | get_region, set_region, get_SupportedRegionList |
| Supported Operations | Retrieve supported regulatory standards and channels |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_supportedStandardList` to:

- Discover which regulatory standards apply for a region
- Determine whether LBT or channel hopping is configurable
- Inspect channel availability before tuning RF settings
