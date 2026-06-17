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
| Supported Operations | Update stack LED color, brightness, flash, and duration |
| Supported API Versions | V1.0 |

## Before You Begin

Choose the visible LED state you want to apply. Use `get_stackled` afterward if you need to verify the current state.
