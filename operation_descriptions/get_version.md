## 1. Description

The `get_version` command retrieves detailed hardware and software component version information from the reader's software stack.

This command returns:

- Reader application, radio firmware, and cloud agent versions
- Radio control application version
- Reader model and serial number
- Available OS upgrade paths and rollback firmware details

No additional payload fields are required to retrieve the full version set.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Version Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/version` |
| Related Commands | [get_status](get_status.md), [get_readerCapabilities](get_readerCapabilities.md), [set_os](set_os.md), [revertback](revertback.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve firmware, model, serial number, and upgrade details |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_version` to:

- Confirm the installed firmware versions before or after a system update
- Verify the exact reader model when applying model-specific configuration
- Capture the serial number for asset tracking, remote fleet management, or support cases
- Audit available OS upgrade paths or rollback capabilities across a fleet

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `readerApplication` | Current reader software version | Determines which features and API operations are available. |
| `radioFirmware` | Firmware running on the radio module | Affects RF behavior, read performance, and hardware compatibility. |
| `cloudAgentApplication` | Cloud agent version | Governs MQTT protocol behavior and cloud connectivity. |
| `model` | Reader model identifier | Drives physical capabilities, antenna limits, and model-specific settings. |
| `serialNumber` | Unique reader serial number | Identifies the device for support cases and asset records. |
| `availableOsUpgrades` | Is the object empty or populated? | A populated object means a downloaded OS upgrade is ready to install. |
