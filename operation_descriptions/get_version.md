The `get_version` command retrieves detailed hardware and software component version information from the reader's software stack.

This command returns:
- Reader application, radio firmware, and cloud agent versions
- Reader model and serial number
- Available OS upgrade paths and rollback firmware details

No additional payload fields are required to retrieve the full version set. The reader echoes the supplied `command_id` in the response.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Version Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | get_status, get_readerCapabilities, set_os, revertback |
| Supported Operations | Retrieve firmware, model, serial number, and upgrade details |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_version` to:
- Confirm the installed firmware versions (Reader App, Radio Firmware) before an OS update
- Verify the exact reader model (e.g., FXR90) when applying model-specific configuration
- Capture the serial number for asset tracking, remote fleet management, or support cases
- Audit available OS upgrade paths or rollback capabilities across a fleet
