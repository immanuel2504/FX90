## 1. Description

The `GET /cloud/version` REST endpoint retrieves detailed hardware and software component version information from the reader's software stack.

This endpoint returns:

- Reader application, radio firmware, and cloud agent versions
- Radio control application version
- Reader model and serial number
- Available OS upgrade paths and rollback firmware details

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/version` |
| Operation ID | `getVersion` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Command | `get_version` |
| MQTT Equivalent | `get_version` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/version` to:

- Confirm installed firmware versions before or after a system update
- Verify the exact reader model when applying model-specific configuration
- Capture the serial number for asset tracking or support cases
- Audit available OS upgrade paths or rollback capabilities across a fleet

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `readerApplication` | Current reader software version | Determines which features and API operations are available. |
| `radioFirmware` | Firmware running on the radio module | Affects RF behavior, read performance, and hardware compatibility. |
| `model` | Reader model identifier | Drives physical capabilities and model-specific configuration options. |
| `serialNumber` | Unique reader serial number | Identifies the device for support cases and asset records. |
| `availableOsUpgrades` | Is the object empty or populated? | A populated object means a downloaded OS upgrade is ready to install. |
