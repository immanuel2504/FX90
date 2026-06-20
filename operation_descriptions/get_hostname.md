The `get_hostname` command retrieves the reader's configured hostname.

This command returns:

- The reader hostname

No additional payload fields are required to retrieve the hostname.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Hostname Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_hostname, get_network |
| Supported Operations | Retrieve the reader hostname |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_hostname` to:

- Confirm the reader's network hostname
- Verify the result of a prior `set_hostname` call
- Audit hostname consistency across a fleet
