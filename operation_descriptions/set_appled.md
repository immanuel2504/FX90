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

