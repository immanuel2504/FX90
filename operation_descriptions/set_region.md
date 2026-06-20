The `set_region` command updates the reader's RF region and regulatory standard.

Use this command to:

- Set the reader region for the deployment country
- Apply the correct regulatory standard
- Reconfigure a reader that has moved to a different region

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Region Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_region](get_region.md), [get_SupportedRegionList](get_SupportedRegionList.md), [get_SupportedStandardlist](get_SupportedStandardlist.md) |
| Supported Operations | Update RF region configuration |
| Supported API Versions | V1.0 |

## Before You Begin

Use `get_SupportedRegionList` and `get_SupportedStandardlist` to choose a valid country and regulatory standard before updating region settings.
