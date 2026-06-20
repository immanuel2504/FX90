The `get_gpostatus` command retrieves the current state of each general-purpose output (GPO) pin on the reader.

This command returns:

- The HIGH/LOW state of each GPO pin (1–4)

No additional payload fields are required to retrieve all pin states.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | GPO Status Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_gpo, get_gpi_status, get_readerCapabilites |
| Supported Operations | Retrieve current GPO pin states |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_gpostatus` to:

- Confirm GPO pin states before or after a `set_gpo` call
- Verify external signaling (lights, horns, gates) is in the expected state
- Audit output state during troubleshooting
