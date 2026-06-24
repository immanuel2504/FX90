## 1. Description

The `set_mode` command configures the reader's operating mode and all RF settings associated with that mode.

This command allows you to configure:

- The operating mode type through `type`
- Antenna port selection and transmit power through `antennas`
- The RF environment profile through `environmentProfile`
- Mode-specific behavior through `modeSpecificSettings`
- Gen2 query, select, and access settings
- Report filtering, RSSI filtering, and metadata options

Use this command to:

- Switch between SIMPLE, INVENTORY, PORTAL, CONVEYOR, CUSTOM, or DIRECTIONALITY modes
- Tune antenna ports and transmit power for the deployment environment
- Configure portal triggers, inventory intervals, or directionality zone plans
- Apply tag filtering and reporting behavior before starting inventory

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Operating Mode Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/mode` |
| Related Commands | [get_mode](get_mode.md), [start](start.md), [stop](stop.md), [get_readerCapabilities](get_readerCapabilities.md) |
| Supported Mode Types | `SIMPLE`, `INVENTORY`, `PORTAL`, `CONVEYOR`, `CUSTOM`, `DIRECTIONALITY` |
| Supported Environment Profiles | `LOW_INTERFERENCE`, `HIGH_INTERFERENCE`, `VERY_HIGH_INTERFERENCE`, `AUTO_DETECT`, `DEMO` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Decide on your mode configuration before sending this command. Changing mode while inventory is active can disrupt reads - call `stop` first if the reader is currently reading.

| What You Need | Details |
|---|---|
| Mode type | One of `SIMPLE`, `INVENTORY`, `PORTAL`, `CONVEYOR`, `CUSTOM`, or `DIRECTIONALITY`. |
| Antenna ports and power | Which antenna ports (or ATR beams) to enable and the transmit power in dBm for each. |
| Mode-specific settings | Inventory interval for `INVENTORY`; GPI triggers and stop interval for `PORTAL`; zone plan for `DIRECTIONALITY`. Only include the sub-object relevant to the chosen mode type. |
| Environment profile | Optional - set to match the RF environment at the deployment site. Use `AUTO_DETECT` if unsure. |
| Active inventory | If the reader is currently reading tags, send `stop` before changing the mode to avoid disrupting ongoing inventory. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or inventory to behave unexpectedly.

### Mode Configuration

- `modeSpecificSettings` is only required for modes that define one (e.g., `INVENTORY`, `PORTAL`, `DIRECTIONALITY`). Including a `modeSpecificSettings` sub-object for a mode type that does not use it may be ignored or rejected.
- For `DIRECTIONALITY` mode, a zone plan or beam configuration must be supplied within `modeSpecificSettings`.

### Antenna and Power

- Transmit power values must be within the limits set by the reader's configured region (`get_region`). Values exceeding `maxTxPowerSupported` will be rejected.
