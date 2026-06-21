## 1. Description

The `set_stackled` command sets the color, brightness, flash behavior, and duration of the stack LED on the reader.

This command allows you to configure:

- The LED color through `color`
- The LED brightness through `brightness`
- Whether the LED flashes through `flash`
- How long the LED state persists through `seconds`

Use this command to:

- Signal reader or inventory status to operators via the physical stack LED
- Flash the stack LED to locate a specific reader in a multi-reader deployment
- Apply a timed LED color that automatically resets after a defined duration
- Drive the LED from application logic in response to inventory events

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Stack LED Control |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_stackled](get_stackled.md), [set_appled](set_appled.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Colors | `red`, `amber`, `green`, `blue`, `false` (off) |
| Supported Brightness Values | `low`, `med`, `high` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Decide on the LED color, flash behavior, and duration before sending this command.

| What You Need | Details |
|---|---|
| LED color | One of `red`, `amber`, `green`, `blue`, or `"false"` (string) to turn the LED off. |
| Brightness | Optional — one of `low`, `med`, or `high`. Defaults to `high` if omitted. |
| Flash behavior | Whether the LED should blink (`true`) or remain solid (`false`). |
| Duration | How long in seconds the LED state should persist. Set to `0` for indefinite duration. A positive value causes the LED to revert after the specified time. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or produce unexpected LED behavior.

### Color Values

- `color` must be one of the supported string values: `red`, `amber`, `green`, `blue`, or `false`. An unrecognized value will be rejected.
- To turn the LED off, set `color` to the string `"false"`.

### Brightness

- `brightness` must be one of `low`, `med`, or `high`. An unrecognized string will be rejected.

### Flash and Duration

- `flash: true` causes the LED to blink at the reader's default blink rate. `flash: false` keeps the LED solid.
- When `seconds` is greater than `0`, the LED state reverts after the duration expires. When `seconds` is `0`, the state persists until explicitly changed by another `set_stackled` command.

### Apply Timing

- The LED change takes effect immediately after the command is acknowledged.
- Use `get_stackled` to verify the current state or check remaining time on a timed LED setting.

### Security Note

- No credentials or secrets are required in the `set_stackled` payload. Do not include authentication data in LED control requests.
