## 1. Description

The `get_readerCapabilities` command retrieves the static hardware and software capabilities of the reader.

This command returns (all fields nested under a top-level `capabilities` object):

- GPIO capacity (number of GPIs and GPOs available)
- Whether LLRP is supported
- Supported endpoint types for data and management
- API versions accepted by the reader

No additional payload fields are required to retrieve the full capability set.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Capability Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/readerCapabilities` |
| Related Commands | [get_version](get_version.md), [get_status](get_status.md), [get_config](get_config.md) |
| Supported Operations | Retrieve static reader hardware and software capabilities |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_readerCapabilities` to:

- Discover how many GPI and GPO pins are available before wiring logic
- Confirm whether LLRP is supported on this reader model
- Determine which endpoint types can be configured for data and management
- Verify which API versions the reader accepts before sending commands
- Audit hardware capabilities across a mixed fleet

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `capabilities.numGPIs` | How many GPI pins are available? | Limits how many external input triggers (sensors, beam breaks) can be wired. |
| `capabilities.numGPOs` | How many GPO pins are available? | Limits how many external output devices (lights, gates) can be driven. |
| `capabilities.llrpSupported` | Is LLRP supported? | Determines whether the reader can be managed via LLRP-based tools. |
| `capabilities.endpointTypesSupported` | Which endpoint types are supported? | Governs which data delivery options can be configured in `set_config`. |
| `capabilities.apiSupported.versions` | Which API versions are accepted? | Ensures the management application targets a compatible API version. |
