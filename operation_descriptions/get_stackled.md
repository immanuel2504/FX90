## 1. Description

The `get_stackled` command retrieves the current state of the stack LED on the reader.

This command returns:

- The active stack LED color
- Whether the LED is currently flashing
- How much time remains for a timed LED state (if applicable)

No additional payload fields are required to retrieve the stack LED state.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Stack LED Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_stackled](set_stackled.md), [get_appled](get_appled.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the current stack LED state |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_stackled` to:

- Check the active stack LED color and brightness
- Confirm whether the LED is currently in a flashing state
- See how much time remains for a timed LED state
- Verify the effect of a prior `set_stackled` call

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `color` | What color is the LED currently showing? | Color is used to signal reader operational state to operators on the floor. |
| `flash` | Is the LED flashing? | Flashing indicates a transient or attention state versus a steady operational state. |
| `remainingTime` | Is a timer active? | A remaining time value indicates the LED state will revert automatically after the duration expires. |
