## 1. Description

The `get_mode` command retrieves the reader's current operating mode and the RF settings associated with that mode.

This command returns:

- The operating mode type (`SIMPLE`, `INVENTORY`, `PORTAL`, `CONVEYOR`, or `CUSTOM`)
- Active antennas or beams and their transmit power settings
- The environment profile in use
- Mode-specific configuration settings (portal, conveyor, directionality, etc.)
- Gen2 query, select, and access settings
- Report filtering, RSSI filtering, metadata fields, and radio start/stop conditions

An optional `verbose` flag controls how much of the configuration is returned.

## 2. The `verbose` Flag

The payload optionally accepts a single boolean field, `verbose`, that controls the level of detail in the response:

| `verbose` | Response |
|---|---|
| `false` (or payload omitted) | Returns **only the settings explicitly configured** for the current mode. Default values are omitted. |
| `true` | Returns the **entire mode configuration**, including every default value. |

An empty payload behaves the same as `verbose: false`. Use `verbose: true` when you need to see every effective setting, including the ones the reader is applying by default.

## 3. Command Details

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

## 4. When to Use This Command

Use `get_mode` to:

- Confirm the active mode before starting an inventory session
- Verify antenna and transmit power selection before RF operations
- Check the environment profile currently in use
- Review mode-specific settings before changing them with `set_mode`
- Check tag reporting and RSSI filter settings before a site validation

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `type` | Which mode is active (`SIMPLE`, `INVENTORY`, `PORTAL`, ...)? | Determines which RF behavior and tag reporting logic the reader uses. |
| `antennas` | Are the right ports enabled with the expected transmit power? | Misconfigured antennas result in missed reads or coverage gaps. |
| `transmitPower` | Is the power level within regulatory limits? | Transmit power must stay below the regional maximum reported by `get_region`. |
| `environment` | Is the profile matched to the deployment environment? | Affects reader sensitivity and false-read filtering for the deployment environment. |
