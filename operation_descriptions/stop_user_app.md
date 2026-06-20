The `stop_user_app` command stops a running user application on the reader.

Use this command to:

- Halt a user app before uninstalling or updating
- Free CPU/memory resources on the reader
- Pause application logic during maintenance

## Command Details

| Property | Value |
|---|---|
| Pattern Name | User Application Control — Stop |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [start_user_app](start_user_app.md), [get_user_apps](get_user_apps.md) |
| Supported API Versions | V1.0 |

MQTT command key: `set_stopUserapp`.
