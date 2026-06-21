## 1. Description

The `set_impinjGen2X` command configures Impinj Gen2X proprietary RFID features on the reader.

This command allows you to configure:

- FastID tag TID embedding through `fastID`
- Tag protection and visibility control through `tagProtect`
- TagFocus session suppression through `tagFocus`
- Tag quieting (basic or advanced) through `tagQuieting`

Use this command to:

- Enable FastID to embed the TID in every inventory response without a separate read
- Protect specific tags with a 32-bit password to prevent unauthorized reads
- Enable TagFocus to improve read rates in dense tag environments by suppressing already-inventoried tags
- Quiet specific tags (by EPC) to exclude them from inventory responses

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_impinjGen2X](get_impinjGen2X.md), [start](start.md), [get_mode](get_mode.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Features | `fastID`, `tagProtect`, `tagFocus`, `tagQuieting` |
| Supported TagProtect Actions | `enableTagProtection`, `disableTagProtection`, `enableTagVisibility`, `disableTagVisibility` |
| Supported TagQuieting Modes | `basic` (quiet/unquiet by EPC list), `advanced` (pre-select with mask) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Decide which Gen2X feature to configure. At least one feature object must be included in the payload. To apply the saved Gen2X configuration during inventory, send `start` with `applyImpinjGen2X: true`.

| What You Need | Details |
|---|---|
| Feature selection | At least one of `fastID`, `tagProtect`, `tagFocus`, or `tagQuieting` must be present. An empty payload will be rejected. |
| FastID | Decide whether to enable or disable TID embedding. Optionally specify a TID word selector (`TID[0]`–`TID[3]`). |
| TagProtect action | Choose one of: `enableTagProtection` (protect a specific tag), `disableTagProtection` (remove protection from a tag), `enableTagVisibility` (allow reading protected tags), `disableTagVisibility` (block reading protected tags). |
| TagProtect password | An 8-character hex string (32-bit) is required for all TagProtect actions. |
| TagProtect tag EPC | `tagID` (hex EPC) is required for `enableTagProtection` and `disableTagProtection`. It must be omitted for `enableTagVisibility` and `disableTagVisibility`. |
| TagFocus | Whether to enable or disable the feature. TagFocus targets session S1. |
| TagQuieting | For basic: provide `action` (`quiet`/`unquiet`) and the `tagIDs` EPC array. For advanced: provide the `preSelect` array, `tagQuietMasks`, `target`, and `stateAwareAction`. |
| Activation | Gen2X settings are saved but not applied until `start` is sent with `applyImpinjGen2X: true`. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or Gen2X behavior to be absent from inventory.

### Payload Requirements

- The payload must contain at least one feature object: `fastID`, `tagProtect`, `tagFocus`, or `tagQuieting`. An empty payload will be rejected.
- Each feature object is independent. You can configure multiple features in a single request by including multiple feature objects.

### FastID

- `fastID.enabled` is required when the `fastID` object is included. Omitting it will cause the command to fail.
- `tidSelector` is optional. If provided, it must be one of `TID[0]`, `TID[1]`, `TID[2]`, or `TID[3]`.

### TagProtect

- `password` is required for all `tagProtect` actions. It must be exactly 8 hexadecimal characters (a 32-bit value). A password shorter or longer than 8 characters, or containing non-hex characters, will be rejected.
- `tagID` (the tag EPC in hex) is required for `enableTagProtection` and `disableTagProtection`. It must be omitted for `enableTagVisibility` and `disableTagVisibility`.
- `action` must be one of the four supported values. An unrecognized action string will be rejected.

### TagFocus

- `tagFocus.enabled` is required when the `tagFocus` object is included. TagFocus operates on session S1 — ensure the inventory session is configured accordingly.

### TagQuieting

- For `basic` mode: `action` must be `quiet` or `unquiet`. `tagIDs` must be a non-empty array of hex EPC strings.
- For `advanced` mode: `preSelect`, `tagQuietMasks`, `target`, and `stateAwareAction` are all required.
- `basic` and `advanced` are mutually exclusive within a single `tagQuieting` object. Include only one.

### Activation

- Sending `set_impinjGen2X` only saves the configuration. To apply it, send `start` with `applyImpinjGen2X: true`. Do not combine BLE scan types with `applyImpinjGen2X`.

### Security Note

- The `tagProtect.password` field contains a sensitive 32-bit credential. Never hardcode TagProtect passwords in your payload. Supply the value from a secrets manager or environment variable at runtime.
