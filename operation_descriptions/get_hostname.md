## 1. Description

The `get_hostname` command retrieves the reader's currently configured network hostname.

This command returns:

- The hostname string currently assigned to the reader

No additional payload fields are required to retrieve the hostname.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Hostname Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/hostName` |
| Related Commands | [set_hostname](set_hostname.md), [get_network](get_network.md) |
| Supported Operations | Retrieve the configured reader hostname |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_hostname` to:

- Verify the hostname assigned to a reader during provisioning
- Confirm the hostname matches the expected naming convention for the deployment
- Retrieve the current hostname before changing it with `set_hostname`
- Verify the result of a prior `set_hostname` call

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `hostName` | Does it match the expected naming convention? | The hostname identifies the reader on the local network and in management systems; a mismatch may indicate the wrong reader was configured. |
