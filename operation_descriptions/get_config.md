The `get_config` command retrieves the reader's full configuration, including RF/XML configuration, GPIO and LED defaults, and reader-gateway endpoint settings.

This command returns:

- The current reader XML configuration
- GPIO and LED default states
- Reader-gateway settings (tag data retention, batching, and endpoint configuration)

No additional payload fields are required to retrieve the full configuration.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Configuration Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_config, set_importCloudConfig, get_status, get_readerCapabilites |
| Supported Operations | Retrieve active reader configuration details |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_config` to:

- Review the active configuration before calling `set_config`
- Audit GPIO/LED default states across readers
- Inspect tag-data retention and batching settings
- Confirm configured data/management endpoints
