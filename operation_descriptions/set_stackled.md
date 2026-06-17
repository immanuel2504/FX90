## Description

The `set_stackled` command updates the stack LED state on the reader.

Use this command to:

- Set the LED color for operator-visible status
- Control LED brightness
- Flash the LED for alert or location workflows
- Apply a timed LED state

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Stack LED Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_stackled](get_stackled.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Update stack LED color, brightness, flash, and duration |
| Supported API Versions | V1.0 |

## Before You Begin

Choose the visible LED state you want to apply. Use `get_stackled` afterward if you need to verify the current state.

## Request Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `payload.color` | string | No | LED color. Supported values include `red`, `amber`, `green`, `blue`, and `off`/`false` depending on reader behavior. |
| `payload.brightness` | string | No | LED brightness: `low`, `med`, or `high`. |
| `payload.flash` | boolean | No | Whether the LED should flash. |
| `payload.seconds` | integer | No | Duration in seconds. Use `0` for an indefinite state where supported. |
