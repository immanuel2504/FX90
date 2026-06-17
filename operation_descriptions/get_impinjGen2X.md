## Description

The `get_impinjGen2X` command retrieves the Impinj Gen2X configuration currently saved on the reader.

Use this command to:

- Check whether FastID, TagProtect, TagFocus, or TagQuieting has been configured
- Review Gen2X settings before applying them with `start`
- Confirm the effect of a previous `set_impinjGen2X` command

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_impinjGen2X](set_impinjGen2X.md), [start](start.md), [get_mode](get_mode.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Retrieve saved Impinj Gen2X configuration |
| Supported API Versions | V1.0 |

## Before You Begin

No command payload fields are required. If no Gen2X configuration has been saved, the response payload can be an empty object.

## Response Payload Summary

| Field | Type | Description |
|---|---|---|
| `payload.fastID` | object | FastID configuration, present when configured. |
| `payload.tagProtect` | object | TagProtect protection or visibility configuration, present when configured. |
| `payload.tagFocus` | object | TagFocus configuration, present when configured. |
| `payload.tagQuieting` | object | Basic or advanced TagQuieting configuration, present when configured. |
