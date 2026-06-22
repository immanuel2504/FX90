## 1. Description

The `get_appled` command retrieves the current state of the application LED on the reader.

This command returns:

- The application LED status (`DEFAULT` or `NOT_DEFAULT`)

No additional payload fields are required to retrieve the LED state.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Application LED Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/app-led` |
| Related Commands | [set_appled](set_appled.md), [get_stackled](get_stackled.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the current application LED state |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_appled` to:

- Confirm whether the application LED is in its default state
- Verify the effect of a prior `set_appled` call
- Audit LED state as part of a device health or provisioning check

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `status` | Is it `DEFAULT` or `NOT_DEFAULT`? | `NOT_DEFAULT` indicates the LED has been overridden by the application; `DEFAULT` means it reflects normal reader status. |
