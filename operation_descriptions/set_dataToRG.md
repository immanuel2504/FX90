## Description

The `set_dataToRG` command sends data to the reader gateway layer.

Use this command to:

- Trigger gateway-side data handling
- Pass integration data toward reader gateway processing
- Support user-application or backend workflows that depend on RG data injection

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Reader Gateway Data Injection |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_req_usr_app](set_req_usr_app.md), [get_config](get_config.md) |
| Supported Operations | Send data to reader gateway |
| Supported API Versions | V1.0 |

## Before You Begin

The current payload schema is an empty object. Use this command only for workflows where the reader gateway expects this trigger.
