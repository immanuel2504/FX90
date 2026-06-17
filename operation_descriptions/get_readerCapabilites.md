## 1. Description

The `get_readerCapabilites` command retrieves the static hardware and software capabilities of the reader.

This command returns:

- GPIO capacity (number of GPIs and GPOs)
- Protocol support (e.g. LLRP)
- Supported endpoint types and API versions

No additional payload fields are required to retrieve the capability set.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Capability Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | get_version, get_status, get_config |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve static reader capabilities |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_readerCapabilites` to:

- Discover how many GPI/GPO pins are available before wiring logic
- Confirm whether LLRP is supported on this model
- Determine which endpoint types can be configured for data/management
- Verify the API versions the reader accepts

> **Note:** Capabilities are static per model; cache the result rather than polling it repeatedly.
