## 1. Description

The `GET /cloud/config` REST endpoint retrieves the reader's full configuration, including RF and XML settings, GPIO and LED defaults, and reader-gateway endpoint settings.

This endpoint returns:

- The current reader XML configuration
- GPIO and LED default states
- Reader-gateway settings including tag data retention, batching, and endpoint configuration

No request body is required.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `GET /cloud/config` |
| Operation ID | `getConfig` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| MQTT Equivalent | `get_config` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Required Request Fields | None |
| Supported Response Sections | JSON response body |
| Supported API Versions | V1.0 |

## 3. When to Use This Endpoint

Use `GET /cloud/config` to:

- Review the active configuration before calling `PUT /cloud/config`
- Audit GPIO and LED default states across a fleet
- Inspect tag-data retention, batching, and endpoint settings
- Confirm which data and management endpoints are configured

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `xmlConfig` | Is the XML configuration as expected? | Defines RF and reader behavior used during inventory operations. |
| `readerGateway` | Are endpoint URLs and credentials correct? | Determines where tag data is delivered and how the reader authenticates. |
| `gpiDefaults` | What are the default GPI states? | Ensures GPI-triggered logic starts from the expected initial state. |
