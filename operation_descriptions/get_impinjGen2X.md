## 1. Description

The `get_impinjGen2X` command retrieves the Impinj Gen2X configuration currently saved on the reader.

This command returns:

- Whether FastID, TagFocus, TagProtect, or TagQuieting is configured
- The parameters for each enabled Gen2X feature

No additional payload fields are required. If no Gen2X configuration has been saved, the response payload will be an empty object.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/impinjGen2X` |
| Related Commands | [set_impinjGen2X](set_impinjGen2X.md), [start](start.md), [get_mode](get_mode.md) |
| Supported Operations | Retrieve saved Impinj Gen2X configuration |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_impinjGen2X` to:

- Check whether FastID, TagProtect, TagFocus, or TagQuieting has been configured
- Review Gen2X settings before applying them with a `start` command
- Confirm the effect of a prior `set_impinjGen2X` call

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `fastId` | Is FastID enabled? | FastID embeds the TID in the singulation response, enabling faster tag identification without a separate read. |
| `tagFocus` | Is TagFocus configured? | TagFocus reduces re-reading of already-singulated tags in dense tag populations. |
| `tagQuieting` | Is TagQuieting set? | TagQuieting suppresses repeated reads of the same tag EPC within a session. |
| `tagProtect` | Is TagProtect active? | TagProtect applies Impinj proprietary tag locking features for secure deployments. |
