## Description

The `get_preSelection` command retrieves the current rxSawFilter pre-selection state.

Use this command to:

- Check whether rxSawFilter is enabled or disabled
- Verify RF pre-selection before starting inventory
- Confirm the effect of a previous `set_preSelection` command

## Command Details

| Property | Value |
|---|---|
| Pattern Name | rxSawFilter Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_preSelection](set_preSelection.md), [start](start.md), [get_status](get_status.md) |
| Supported Operations | Retrieve rxSawFilter state |
| Supported API Versions | V1.0 |

## Before You Begin

No command payload fields are required. Use this command before changing the pre-selection state or before starting inventory in deployments where receiver filtering matters.
