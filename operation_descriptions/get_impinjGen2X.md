## 1. Description

The `get_impinjGen2X` command retrieves Impinj Gen2X configuration from the reader.

Use this command to:

- Audit Gen2X-specific RF settings
- Verify configuration before calling `set_impinjGen2X`

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_impinjGen2X](set_impinjGen2X.md), [get_mode](get_mode.md) |
| Required Request Fields | `command`, `command_id` |
| Supported Operations | Retrieve Impinj Gen2X settings |
| Supported Response Sections | payload |
| Supported API Versions | V1.0 |
