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
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Configure FastID, TagProtect, TagFocus, and TagQuieting |
| Supported API Versions | V1.0 |

## Before You Begin

Configure Gen2X before starting RFID inventory. To apply the saved Gen2X configuration, send `start` with `applyImpinjGen2X: true`. Do not combine BLE scan types with `applyImpinjGen2X`.

## Request Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `payload.fastID.enabled` | boolean | Conditional | Enables or disables FastID. |
| `payload.fastID.tidSelector` | string | No | Optional TID selector value such as `TID[0]`. |
| `payload.tagProtect.action` | string | Conditional | Protection action: `enableTagProtection`, `disableTagProtection`, `enableTagVisibility`, or `disableTagVisibility`. |
| `payload.tagProtect.password` | string | Conditional | 8-character hexadecimal protection password. |
| `payload.tagProtect.tagID` | string | Conditional | Target EPC/tag ID for tag protection actions. |
| `payload.tagProtect.enableShortRange` | boolean | No | Enables short-range protection behavior where applicable. |
| `payload.tagFocus.enabled` | boolean | Conditional | Enables or disables TagFocus. |
| `payload.tagQuieting.basic` | object | Conditional | Basic quiet/unquiet configuration by tag ID. |
| `payload.tagQuieting.advanced` | object | Conditional | Advanced quiet/unquiet configuration using preselect and state-aware masks. |
