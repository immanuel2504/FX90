## 1. Description

The `set_impinjGen2X` command sets the Impinj Gen2X configuration on the reader.

Use it to:

- Enable or tune Impinj Gen2X-specific RF features
- Configure Gen2X parameters for tag read performance
- Align Gen2X settings with Impinj tag populations

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_impinjGen2X](get_impinjGen2X.md), [set_mode](set_mode.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Set Impinj Gen2X configuration |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Review current Gen2X settings with `get_impinjGen2X` once schemas are available.
