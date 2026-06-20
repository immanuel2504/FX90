The `set_passthru` command sends a pass-through payload to a reader component.

Use this command to:

- Forward component-specific commands not covered by standard APIs
- Query or control low-level reader component behavior
- Support diagnostics or vendor-specific workflows

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Pass-Through Command |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_status](get_status.md), [set_config](set_config.md) |
| Supported Operations | Send a component pass-through command |
| Supported API Versions | V1.0 |

## Before You Begin

Use this command only when you know the target component and payload string expected by that component. Invalid pass-through commands may return component-specific errors.
