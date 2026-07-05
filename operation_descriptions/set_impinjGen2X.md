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
| REST Endpoint | `PUT /cloud/impinjGen2X` |
| Related Commands | [get_impinjGen2X](get_impinjGen2X.md), [start](start.md), [get_mode](get_mode.md) |
| Supported Features | `fastID`, `tagProtect`, `tagFocus`, `tagQuieting` |
| Supported TagProtect Actions | `enableTagProtection`, `disableTagProtection`, `enableTagVisibility`, `disableTagVisibility` |
| Supported TagQuieting Modes | `basic` (quiet/unquiet by EPC list), `advanced` (pre-select with mask) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Decide which Gen2X feature to configure. At least one feature object must be included in the payload. To apply the saved Gen2X configuration during inventory, send `start` with `applyImpinjGen2X: true`.

| What You Need | Details |
|---|---|
| Feature selection | At least one of `fastID`, `tagProtect`, `tagFocus`, or `tagQuieting` must be present. An empty payload will be rejected. |
| FastID | Decide whether to enable or disable TID embedding. Optionally specify a TID word selector (`TID[0]`-`TID[3]`). |
| TagProtect action | Choose one of: `enableTagProtection` (protect a specific tag), `disableTagProtection` (remove protection from a tag), `enableTagVisibility` (allow reading protected tags), `disableTagVisibility` (block reading protected tags). |
| TagProtect password | An 8-character hex string (32-bit) is required for all TagProtect actions. |
| TagProtect tag EPC | `tagID` (hex EPC) is required for `enableTagProtection` and `disableTagProtection`. It must be omitted for `enableTagVisibility` and `disableTagVisibility`. |
| TagFocus | Whether to enable or disable the feature. TagFocus targets session S1. |
| TagQuieting | For basic: provide `action` (`quiet`/`unquiet`) and the `tagIDs` EPC array. For advanced: provide the `preSelect` array, `tagQuietMasks`, `target`, and `stateAwareAction`. |
| Activation | Gen2X settings are saved but not applied until `start` is sent with `applyImpinjGen2X: true`. |

