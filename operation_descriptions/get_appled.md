The `get_appled` command retrieves the current state of the application LED on the reader.

This command returns:

- The application LED status (DEFAULT or NOT_DEFAULT)

No additional payload fields are required to retrieve the LED state.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Application LED Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_appled, get_stackled |
| Supported Operations | Retrieve current application LED state |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_appled` to:

- Confirm whether the app LED is in its default state
- Verify the effect of a prior `set_appled` call
- Audit LED state as part of a device health check
