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
| Related Commands | [get_status](get_status.md), [set_config](set_config.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | `component`, `payload` (inner) |
| Supported Components | `RC` (Radio Control) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Know the target component and the exact payload string it expects before sending this command. Invalid pass-through commands may produce component-specific errors that are not surfaced through standard error codes.

| What You Need | Details |
|---|---|
| Component name | The reader component to target. Currently supported: `RC` (Radio Control). |
| Payload string | The command or query string expected by the target component. The format is component-specific and must be obtained from the component's low-level documentation. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or produce unexpected component behavior.

### Required Fields

- `component` and `payload` (inner string) are both required. Omitting either will cause the command to be rejected.

### Component Names

- `component` must be a recognized component identifier. Unrecognized component names will be rejected or produce a no-operation response.

### Payload Format

- The inner `payload` field is a raw string passed directly to the target component. The format and valid values are specific to the component and must match what the component expects.
- Malformed or unrecognized payload strings will produce component-level errors that may not clearly indicate the cause of failure.

### Apply Timing

- The command is forwarded to the component immediately. The response time depends on how quickly the component processes the pass-through request.

### Security Note

- Pass-through commands bypass standard validation. Only send payloads from trusted, well-understood sources. Do not expose the pass-through interface to untrusted input.
