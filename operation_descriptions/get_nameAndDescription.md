## 1. Description

The `get_nameAndDescription` command retrieves the human-friendly name and description assigned to the reader.

This command returns:

- The reader name
- The reader description

No additional payload fields are required to retrieve the name and description.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Name & Description Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_nameAndDescription, get_hostname, get_network |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the reader name and description |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_nameAndDescription` to:

- Confirm the friendly name shown in management tools
- Verify the result of a prior `set_nameAndDescription` call
- Audit naming conventions across a fleet

> **Note:** Use `get_nameAndDescription` before `set_nameAndDescription` to preserve existing values you don't intend to change.
