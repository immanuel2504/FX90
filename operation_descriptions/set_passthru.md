## 1. Description

The `set_passthru` command sends a pass-through payload directly to a specific reader component, bypassing the standard API layer.

This command allows you to configure:

- The target component through `component`
- The raw command or query string to send to that component through `payload`

Use this command to:

- Forward component-specific commands not covered by standard MQTT API operations
- Query or control low-level reader component behavior for diagnostics
- Support vendor-specific or advanced troubleshooting workflows

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Pass-Through Command |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/pass-through` |
| Related Commands | [get_status](get_status.md), [set_config](set_config.md) |
| Required Payload Fields | `component`, `payload` (inner) |
| Supported Components | `RC` (Radio Control) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Know the target component and the exact payload string it expects before sending this command. Invalid pass-through commands may produce component-specific errors that are not surfaced through standard error codes.

| What You Need | Details |
|---|---|
| Component name | The reader component to target. Currently supported: `RC` (Radio Control). |
| Payload string | The command or query string expected by the target component (for the `RC` component, common values include `mode` and `status`). The format is component-specific and must be obtained from the component's low-level documentation. |
