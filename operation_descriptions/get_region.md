## 1. Description

The `get_region` command retrieves the reader's currently configured RF region and the regulatory parameters in effect.

This command returns:

- The active region and regulatory standard
- Listen-before-talk (LBT) state
- Enabled channels and minimum transmit power

No additional payload fields are required to retrieve the active region settings.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Region Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_region, get_SupportedRegionList, get_SupportedStandardlist |
| Supported Operations | Retrieve active RF region and regulatory settings |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_region` to:

- Confirm the reader is set to the correct regulatory region
- Verify LBT and channel configuration before inventory
- Audit minimum transmit power for the region
- Validate region settings after deployment to a new country
