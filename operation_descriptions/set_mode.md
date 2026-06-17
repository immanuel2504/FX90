## 1. Description

The `set_mode` command configures the reader's operating mode and the RF settings associated with that mode.

Use it to:

- Switch between SIMPLE, INVENTORY, PORTAL, CONVEYOR, CUSTOM, or DIRECTIONALITY modes
- Tune antennas, transmit power, and environment profile for the deployment
- Configure mode-specific settings (inventory interval, portal triggers, directionality zones)

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_mode](get_mode.md), [start](start.md), [stop](stop.md), [get_config](get_config.md) |
| Supported Operations | Configure operating mode and RF parameters |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather these details before sending the command. Changing mode while inventory is active can disrupt reads — call `stop` first if needed.

| What You Need | Details |
|---|---|
| Mode type | One of `SIMPLE`, `INVENTORY`, `PORTAL`, `CONVEYOR`, `CUSTOM`, `DIRECTIONALITY`. |
| Antennas / power | Which antenna ports (or ATR beams) and TX power in dBm. |
| Mode-specific settings | Inventory interval, portal GPI triggers, or directionality zone plan — depends on `type`. |
| Environment | Optional RF environment profile (`LOW_INTERFERENCE`, `HIGH_INTERFERENCE`, `VERY_HIGH_INTERFERENCE`, `AUTO_DETECT`, `DEMO`). |

## 4. Operating Modes

The `type` field in the payload defines the operating mode.

| type | Description | modeSpecificSettings |
|---|---|---|
| `SIMPLE` | Basic continuous read | Not required |
| `INVENTORY` | Timed or triggered inventory | `interval` (unit + value) |
| `PORTAL` | Portal/dock read with GPI triggers | `startTrigger`, `stopInterval` |
| `CONVEYOR` | Conveyor-style read | Mode-specific conveyor settings |
| `CUSTOM` | Custom mode configuration | Custom settings object |
| `DIRECTIONALITY` | Zone-based direction detection | `basicConfig`, `beamConfig`, zone plan |
