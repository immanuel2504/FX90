## 1. Description

The `get_supportedStandardList` command retrieves the list of RF regulatory standards supported by the reader and the channel details for each.

This command returns:

- Supported regulatory standard names
- LBT and frequency hopping configurability per standard
- Whether individual channels are selectable per standard
- Enabled channel data per standard

No additional payload fields are required to retrieve the supported standard list.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Supported Standard Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/supportedStandardList` |
| Related Commands | [get_region](get_region.md), [set_region](set_region.md), [get_SupportedRegionList](get_SupportedRegionList.md) |
| Supported Operations | Retrieve supported regulatory standards and their channel details |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_supportedStandardList` to:

- Discover which regulatory standards are available for a given region
- Determine whether LBT or channel hopping is configurable per standard
- Inspect channel availability before tuning RF settings
- Populate standard selection options in provisioning tools

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `StandardName` | Is the target regulatory standard listed? | Confirms that the required standard is available before configuring the region. |
| `isLBTConfigurable` | Can LBT be enabled or disabled for this standard? (string-encoded `"true"`/`"false"`) | Some standards mandate LBT; knowing configurability prevents invalid region settings. |
| `isChannelSelectable` | Can individual channels be selected for this standard? | Determines whether `channeldata` can be supplied when setting the region. |
| `channeldata` | Which channels are available for each standard? | Determines the frequency plan the reader will use for that standard. |
