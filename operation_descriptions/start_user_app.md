The `start_user_app` command starts a user application installed on the reader.

Use this command to:

- Launch an installed user app on demand
- Restart an app after configuration changes
- Bring application logic online after `install_user_app`

## Command Details

| Property | Value |
|---|---|
| Pattern Name | User Application Control — Start |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [stop_user_app](stop_user_app.md), [get_user_apps](get_user_apps.md), [install_user_app](install_user_app.md) |
| Supported API Versions | V1.0 |

MQTT command key: `set_startUserapp`.
