## 1. Description

The `get_hostname` command retrieves the reader's currently configured network hostname.

This command returns:

- The reader hostname string

No additional payload fields are required to retrieve the hostname.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Hostname Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_hostname](set_hostname.md), [get_network](get_network.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the configured reader hostname |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_hostname` to:

- Confirm the reader's network hostname before changing it
- Verify the result of a prior `set_hostname` call
- Audit hostname consistency across a fleet of readers

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `hostname` | Does it match the expected naming convention? | The hostname is used for device identification on the local network and in management systems. |
