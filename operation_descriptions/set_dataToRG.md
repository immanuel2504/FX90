## 1. Description

The `set_dataToRG` command triggers the reader gateway layer to process and deliver any buffered data.

This command requires:

- An empty payload object - no additional parameters are needed

Use this command to:

- Manually trigger reader gateway data delivery when automatic forwarding is not active
- Flush buffered tag events through the reader gateway pipeline
- Support integration workflows that depend on on-demand data injection into the reader gateway

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Gateway Data Trigger |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/setdataToRG` |
| Related Commands | [set_req_usr_app](set_req_usr_app.md), [get_config](get_config.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | None (empty object `{}`) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm that the reader gateway is configured and active before using this command. Triggering data delivery when no data is buffered or when the gateway is not configured will produce no effect.

| What You Need | Details |
|---|---|
| Reader gateway state | Confirm the reader gateway is configured with valid endpoint settings (see `get_config`) before triggering data delivery. |
| Buffered data | This command is only meaningful when tag event data is buffered and awaiting delivery. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to be rejected.

### Payload Requirements

- The `payload` field must be an empty object (`{}`). No additional properties are accepted. Providing any fields within the payload object will cause the command to be rejected.

### Apply Timing

- The reader gateway data trigger is executed immediately after the command is acknowledged.

### Security Note

- No credentials or secrets are required in the `set_dataToRG` payload. Do not include authentication data in data trigger requests.
