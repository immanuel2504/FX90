## Description

The `set_preSelection` command enables or disables the rxSawFilter pre-selection feature.

Use this command to:

- Enable rxSawFilter before RFID inventory
- Disable rxSawFilter for troubleshooting or alternate RF behavior
- Tune receiver filtering for the deployment environment

## Command Details

| Property | Value |
|---|---|
| Pattern Name | rxSawFilter Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_preSelection](get_preSelection.md), [start](start.md), [get_status](get_status.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Enable or disable rxSawFilter |
| Supported API Versions | V1.0 |

## Before You Begin

Use `get_preSelection` if you need to confirm the current state before changing it.

## Request Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `payload.preSelection` | boolean | Yes | Set to `true` to enable rxSawFilter or `false` to disable it. |
