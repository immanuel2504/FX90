## 1. Description

The `get_gpi_status` command retrieves the current state of each general-purpose input (GPI) pin on the reader.

This command returns:

- The HIGH or LOW state of each GPI pin (1-4)

No additional payload fields are required to retrieve all pin states.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | GPI Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/gpi` |
| Related Commands | [get_gpostatus](get_gpostatus.md), [set_gpo](set_gpo.md), [get_readerCapabilities](get_readerCapabilities.md) |
| Supported Operations | Retrieve current GPI pin states |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_gpi_status` to:

- Read the current state of external sensors wired to GPI pins
- Confirm a trigger source (e.g., motion sensor, beam break) before enabling start or stop triggers
- Audit GPI input state during troubleshooting

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `1` | Is GPI pin 1 HIGH or LOW? | Confirms whether the wired sensor or trigger on port 1 is currently active. |
| `2` | Is GPI pin 2 HIGH or LOW? | Confirms whether the wired sensor or trigger on port 2 is currently active. |
| `3` | Is GPI pin 3 HIGH or LOW? | Confirms whether the wired sensor or trigger on port 3 is currently active. |
| `4` | Is GPI pin 4 HIGH or LOW? | Confirms whether the wired sensor or trigger on port 4 is currently active. |
