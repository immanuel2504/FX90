The `get_gpi_status` command retrieves the current state of each general-purpose input (GPI) pin on the reader.

This command returns:

- The HIGH/LOW state of each GPI pin (1–4)

No additional payload fields are required to retrieve all pin states.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | GPI Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | get_gpostatus, set_gpo, get_readerCapabilites |
| Supported Operations | Retrieve current GPI pin states |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_gpi_status` to:

- Read the current state of external sensors wired to GPI pins
- Confirm a trigger source (e.g. motion sensor, beam break) before enabling start/stop triggers
- Audit input state during troubleshooting
