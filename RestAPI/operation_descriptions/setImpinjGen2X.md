The `PUT /cloud/impinjGen2X` REST endpoint and the `set_impinjGen2X` MQTT command configure Impinj Gen2X RFID features on the reader.

Use this operation to:
- Enable or disable FastID
- Configure TagProtect protection or visibility actions
- Enable or disable TagFocus
- Quiet or unquiet tags using basic or advanced TagQuieting

## 1. Operation Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration Update |
| Supported Protocols | REST (HTTP/HTTPS), MQTT |
| Applies To | FXR90 |
| Related Operations | `getImpinjGen2X`, `startInventory` |
| REST Endpoint | `PUT /cloud/impinjGen2X` |
| MQTT Command | `set_impinjGen2X` |

## 2. Before You Begin

Configure Gen2X before starting RFID inventory. To apply the saved configuration during inventory, call `PUT /cloud/start` with `applyImpinjGen2X: true`.

| Feature | Notes |
|---|---|
| `fastID` | Enables or disables FastID. |
| `tagProtect` | Requires action and password; tag-specific actions require `tagID`. |
| `tagFocus` | Enables or disables TagFocus mode. |
| `tagQuieting` | Supports basic tag ID lists and advanced pre-select masks. |
