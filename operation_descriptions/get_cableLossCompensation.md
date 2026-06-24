## 1. Description

The `get_cableLossCompensation` command retrieves the cable loss compensation values configured on the reader for read points 1 through 4.

This command returns:

- Cable length per read point
- Cable loss per hundred feet per read point

No additional payload fields are required. Values are returned using fixed read-point keys `1`, `2`, `3`, and `4`.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Cable Loss Compensation Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/cableLossCompensation` |
| Related Commands | [set_cableLossCompensation](set_cableLossCompensation.md), [get_config](get_config.md), [get_readPoints](get_readPoints.md) |
| Supported Operations | Retrieve per-read-point cable loss compensation values |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_cableLossCompensation` to:

- Review compensation values before adjusting transmit power settings
- Verify cabling assumptions per antenna or read point
- Audit RF link budgets across all read points
- Confirm settings after replacing antenna cabling

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `1.cableLength` | What cable length is configured for read point 1? | Cable length feeds into the loss calculation that adjusts effective transmit power. |
| `1.cableLoss` | What loss per 100 ft is configured for read point 1? | Higher cable loss requires the reader to transmit at a higher power to compensate. |
| Per-port consistency | Are all active read points configured? | Unconfigured ports default to zero compensation, which may underpower long cable runs. |
