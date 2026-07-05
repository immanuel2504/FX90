## 1. Description

The `set_preSelection` command enables or disables the rxSawFilter pre-selection feature on the reader.

This command allows you to configure:

- The rxSawFilter (receive SAW filter pre-selection) state through `preSelection`

Use this command to:

- Enable rxSawFilter to improve receiver selectivity in noisy RF environments
- Disable rxSawFilter when operating in clean RF environments where sensitivity is the priority
- Tune receiver filtering behavior before starting RFID inventory

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | rxSawFilter Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/preSelection` |
| Related Commands | [get_preSelection](get_preSelection.md), [start](start.md), [get_status](get_status.md) |
| Required Payload Fields | `preSelection` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Determine the appropriate rxSawFilter state for the deployment environment before sending this command. Use `get_preSelection` to check the current state before changing it.

| What You Need | Details |
|---|---|
| Filter state | `true` to enable rxSawFilter (better selectivity in noisy environments), or `false` to disable it (better sensitivity in clean environments). |
| Deployment RF environment | Consider enabling the filter when the reader operates near other UHF RFID systems or dense RF infrastructure. Disable it in quiet, isolated RF environments to maximize read range. |

