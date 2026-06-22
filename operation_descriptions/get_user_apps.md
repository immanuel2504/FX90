## 1. Description

The `get_user_apps` command retrieves the list of user applications installed on the reader.

This command returns:

- An array of installed user apps, each with name, autostart flag, running status, and metadata

No additional payload fields are required to retrieve all installed user apps.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | User Application Inventory Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/apps` |
| Related Commands | [install_user_app](install_user_app.md), [uninstall-user-app](uninstall-user-app.md), [start_user_app](start_user_app.md), [stop_user_app](stop_user_app.md), [autostart_user_app](autostart_user_app.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the list of installed user applications |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_user_apps` to:

- Confirm which user apps are installed before issuing start, stop, or uninstall commands
- Check whether a user app is currently running
- Verify autostart configuration per installed app
- Audit deployed applications across a fleet of readers

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `name` | Is the expected app present in the list? | Confirms successful installation before attempting to start or configure the app. |
| `running` | Is the app currently running? | Required before sending `stop_user_app`; also confirms a successful `start_user_app`. |
| `autostart` | Is autostart enabled? | Determines whether the app will resume automatically after a reboot. |
