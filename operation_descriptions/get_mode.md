## 1. Description

The `get_mode` command retrieves the reader's current operating mode and the RF settings associated with that mode.

This command returns:

- The operating mode type (SIMPLE, INVENTORY, PORTAL, etc.)
- Active antennas/beams and transmit power
- Environment profile and mode-specific settings

No additional payload fields are required to retrieve the active mode.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_mode, start, stop, get_config |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve active operating mode and RF settings |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_mode` to:

- Confirm the active mode before starting an inventory
- Verify antenna/beam and transmit power selection
- Check the environment profile in use
- Review mode-specific settings before changing them

> **Note:** Run `get_mode` before `set_mode` to review current RF settings and avoid disrupting an active read cycle.
