## Description

The `set_impinjGen2X` command configures Impinj Gen2X proprietary RFID features on the reader.

Use this command to:

- Enable or disable FastID
- Configure TagProtect protection or visibility behavior
- Enable or disable TagFocus
- Quiet or unquiet tags using basic or advanced TagQuieting

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_impinjGen2X](get_impinjGen2X.md), [start](start.md), [get_mode](get_mode.md) |
| Supported Operations | Configure FastID, TagProtect, TagFocus, and TagQuieting |
| Supported API Versions | V1.0 |

## Before You Begin

Configure Gen2X before starting RFID inventory. To apply the saved Gen2X configuration, send `start` with `applyImpinjGen2X: true`. Do not combine BLE scan types with `applyImpinjGen2X`.
