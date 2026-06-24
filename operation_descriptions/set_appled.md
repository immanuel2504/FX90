## 1. Description

The `set_appled` command sets the color, brightness, flash behavior, and duration of the application LED on the reader.

This command allows you to configure:

- The LED color through `color`
- The LED brightness through `brightness`
- Whether the LED flashes through `flash`
- How long the LED state persists through `seconds`

Use this command to:

- Signal application state to operators on the floor using the reader LED
- Flash the application LED to draw attention to a reader requiring action
- Set a timed LED state that automatically resets after a defined duration
- Override the default LED behavior from application logic

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Application LED Control |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/app-led` |
| Related Commands | [get_appled](get_appled.md) |
| Supported Colors | `red`, `amber`, `green`, `blue`, `false` (off) |
| Supported Brightness Values | `low`, `med`, `high` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Decide on the LED color, flash behavior, and duration before sending this command.

| What You Need | Details |
|---|---|
| LED color | One of `red`, `amber`, `green`, `blue`, or `"false"` (string) to turn the LED off. |
| Flash behavior | Whether the LED should blink (`true`) or remain solid (`false`). |
| Duration | How long in seconds the LED state should persist. Set to `0` for indefinite (until the next `set_appled` command). |
| Brightness | Optional - one of `low`, `med`, or `high`. If omitted, the reader applies its default brightness. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or produce unexpected LED behavior.

### Color Values

- `color` must be one of the supported string values: `red`, `amber`, `green`, `blue`, or `false`. An unrecognized color value will be rejected.
- To turn the LED off, set `color` to the string `"false"` - not the boolean `false`.

### Flash and Duration

- `flash: true` causes the LED to blink at the reader's default blink rate. `flash: false` keeps the LED solid.
- When `seconds` is greater than `0`, the LED state reverts to the application default after the duration expires. When `seconds` is `0`, the state persists indefinitely until explicitly changed.

### Brightness

- `brightness` must be one of `low`, `med`, or `high`. An unrecognized string will be rejected.
