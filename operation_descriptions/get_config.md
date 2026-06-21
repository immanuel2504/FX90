## 1. Description

The `get_config` command retrieves the reader's full configuration, including RF and XML settings, GPIO and LED defaults, and reader-gateway endpoint settings.

This command returns:

- The current reader XML configuration
- GPIO and LED default states
- Reader-gateway settings including tag data retention, batching, and endpoint configuration

No additional payload fields are required to retrieve the full configuration.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_config](set_config.md), [set_importCloudConfig](set_importCloudConfig.md), [get_status](get_status.md), [get_readerCapabilities](get_readerCapabilities.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve active reader configuration |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_config` to:

- Review the active configuration before calling `set_config`
- Audit GPIO and LED default states across a fleet of readers
- Inspect tag-data retention and batching settings
- Confirm which data and management endpoints are configured

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `xmlConfig` | Is the XML configuration as expected? | Defines the RF and reader behavior used during inventory operations. |
| `readerGateway` | Are endpoint URLs and credentials correct? | Determines where tag data is delivered and how the reader authenticates. |
| `gpiDefaults` | What are the default GPI states? | Ensures GPI-triggered logic starts from the expected initial state. |
| `ledDefaults` | What are the LED default states? | Confirms expected LED behavior on startup and after a reboot. |
