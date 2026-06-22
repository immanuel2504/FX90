## 1. Description

The `get_gpostatus` command retrieves the current state of each general-purpose output (GPO) pin on the reader.

This command returns:

- The HIGH or LOW state of each GPO pin (1-4)

No additional payload fields are required to retrieve all pin states.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | GPO Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/gpo` |
| Related Commands | [set_gpo](set_gpo.md), [get_gpi_status](get_gpi_status.md), [get_readerCapabilities](get_readerCapabilities.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve current GPO pin states |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_gpostatus` to:

- Confirm GPO pin states before or after a `set_gpo` call
- Verify that external signaling devices (lights, horns, gates) are in the expected state
- Audit output state during troubleshooting

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `1` | Is GPO pin 1 HIGH or LOW? | Confirms whether the device driven by port 1 (e.g., a light or gate) is active. |
| `2` | Is GPO pin 2 HIGH or LOW? | Confirms whether the device driven by port 2 is active. |
| `3` | Is GPO pin 3 HIGH or LOW? | Confirms whether the device driven by port 3 is active. |
| `4` | Is GPO pin 4 HIGH or LOW? | Confirms whether the device driven by port 4 is active. |
