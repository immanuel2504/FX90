The `get_cableLossCompensation` command retrieves the per-read-point cable loss compensation values configured on the reader.

This command returns:

- Cable length per read point
- Cable loss per hundred feet per read point

No additional payload fields are required; values are returned keyed by read point (1–8).

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Cable Loss Compensation Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_cableLossCompensation, get_config |
| Supported Operations | Retrieve per-read-point cable loss values |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_cableLossCompensation` to:

- Review compensation values before adjusting transmit power
- Verify cabling assumptions per antenna/read point
- Audit RF link budgets across read points
- Confirm settings after replacing antenna cabling
