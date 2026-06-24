## 1. Description

The `get_mode` command retrieves the reader's current operating mode and the RF settings associated with that mode.

This command returns:

- The operating mode type (e.g., SIMPLE, INVENTORY, PORTAL)
- Active antennas or beams and their transmit power settings
- Environment profile in use
- Mode-specific configuration settings

No additional payload fields are required to retrieve the active mode.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/mode` |
| Related Commands | [set_mode](set_mode.md), [start](start.md), [stop](stop.md), [get_config](get_config.md) |
| Supported Operations | Retrieve active operating mode and RF settings |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_mode` to:

- Confirm the active mode before starting an inventory session
- Verify antenna and transmit power selection before RF operations
- Check the environment profile currently in use
- Review mode-specific settings before changing them with `set_mode`

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `modeType` | Which mode is active (SIMPLE, INVENTORY, PORTAL)? | Determines which RF behavior and tag reporting logic the reader uses. |
| `antennas` | Which antenna ports are active? | Confirms the physical coverage area for the current inventory session. |
| `txPower` | What is the configured transmit power? | Directly affects read range and regulatory compliance. |
| `environmentProfile` | Which environment profile is set? | Affects reader sensitivity and RF settings for the deployment environment. |
