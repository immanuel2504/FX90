The `get_stackled` command retrieves the current stack LED state.

Use this command to:

- Check the active stack LED color and brightness
- Determine whether the LED is flashing
- See how much time remains for a timed LED state

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Stack LED Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_stackled](set_stackled.md) |
| Supported Operations | Retrieve stack LED state |
| Supported API Versions | V1.0 |

## Before You Begin

No command payload fields are required. Use this command after `set_stackled` to confirm the current visible LED state.
