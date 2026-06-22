## 1. Description

The `get_preSelection` command retrieves the current rxSawFilter pre-selection state from the reader.

This command returns:

- Whether the rxSawFilter (receive SAW filter pre-selection) is enabled or disabled

No additional payload fields are required.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | rxSawFilter Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/preSelection` |
| Related Commands | [set_preSelection](set_preSelection.md), [start](start.md), [get_status](get_status.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the rxSawFilter pre-selection state |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_preSelection` to:

- Check whether rxSawFilter is enabled or disabled before starting inventory
- Verify the RF pre-selection state in deployments where receiver filtering matters
- Confirm the effect of a prior `set_preSelection` call

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `rxSawFilter` | Is the filter enabled or disabled? | Enabling the SAW filter improves receiver selectivity in noisy RF environments but may reduce sensitivity in clean environments. |
