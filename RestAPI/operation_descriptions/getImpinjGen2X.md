The `GET /cloud/impinjGen2X` REST endpoint and the `get_impinjGen2X` MQTT command retrieve the Impinj Gen2X feature configuration saved on the reader.

This operation can return configuration for:
- FastID
- TagProtect
- TagFocus
- TagQuieting

## 1. Operation Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration Query |
| Supported Protocols | REST (HTTP/HTTPS), MQTT |
| Applies To | FXR90 |
| Related Operations | `setImpinjGen2X`, `startInventory` |
| REST Endpoint | `GET /cloud/impinjGen2X` |
| MQTT Command | `get_impinjGen2X` |

## 2. When to Use This Endpoint

Use this endpoint to verify saved Gen2X settings before starting RFID inventory. If no Gen2X configuration has been saved, the response can be an empty object.

| Field | What to Check |
|---|---|
| `fastID.enabled` | Whether FastID is enabled. |
| `tagProtect` | Tag protection or visibility action settings. |
| `tagFocus.enabled` | Whether TagFocus is enabled. |
| `tagQuieting` | Basic or advanced quieting settings. |
