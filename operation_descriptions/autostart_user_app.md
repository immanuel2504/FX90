The `autostart_user_app` command configures whether a user application starts automatically when the reader boots.

Use this command to:

- Enable autostart for production user apps
- Disable autostart for test or manual-only apps
- Standardize boot behavior across a fleet

## Command Details

| Property | Value |
|---|---|
| Pattern Name | User Application Autostart Configuration |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/apps/{appname}/autostart` |
| Related Commands | [get_user_apps](get_user_apps.md), [start_user_app](start_user_app.md), [install_user_app](install_user_app.md) |
| Required Payload Fields | `appname`, `autostart` |
| Supported API Versions | V1.0 |

MQTT command key: `autostart_user_app`.
