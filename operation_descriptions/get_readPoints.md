## 1. Description

The `get_readPoints` command retrieves the read points available on the reader.

This command returns:

- The list of read-point identifiers available on this reader

No additional payload fields are required.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Read Point Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/readPoints` |
| Related Commands | [get_cableLossCompensation](get_cableLossCompensation.md), [set_cableLossCompensation](set_cableLossCompensation.md), [set_mode](set_mode.md) |
| Supported Operations | Retrieve available reader read points |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_readPoints` to:

- Identify available read-point identifiers before configuring cable loss compensation
- Map physical read points before configuring inventory behavior in `set_mode`
- Verify read-point availability before referencing them in antenna configuration

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Read-point list | How many read points are returned? | Determines how many antenna ports are physically available for use. |
| Read-point IDs | Do the returned IDs match expected port numbering? | Read-point identifiers must match exactly when used in `set_cableLossCompensation` or `set_mode`. |
