## Description

The `get_readPoints` command retrieves the read points available on the reader.

Use this command to:

- Identify available antenna/read-point identifiers
- Verify read-point availability before applying cable loss settings
- Map physical read points before configuring inventory behavior

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Read Point Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_cableLossCompensation](get_cableLossCompensation.md), [set_cableLossCompensation](set_cableLossCompensation.md), [set_mode](set_mode.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Retrieve reader read points |
| Supported API Versions | V1.0 |

## Before You Begin

No command payload fields are required. Use the returned read-point list when configuring features that refer to antenna or read-point identifiers.

## Response Payload Summary

| Field | Type | Description |
|---|---|---|
| `payload` | array of strings | List of read-point identifiers available on the reader. |
