The `uninstall-user-app` command removes a user application from the reader.

Use this command to:

- Remove a decommissioned user application
- Free storage before installing a replacement
- Clean up test or development packages

## Command Details

| Property | Value |
|---|---|
| Pattern Name | User Application Removal |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/apps/{appname}/uninstall` |
| Related Commands | [get_user_apps](get_user_apps.md), [install_user_app](install_user_app.md), [stop_user_app](stop_user_app.md) |
| Required Payload Fields | `appname` |
| Supported API Versions | V1.0 |

## Before You Begin

Stop the app with `stop_user_app` before uninstalling if it is currently running.

| What You Need | Details |
|---|---|
| App name | Exact `appname` from `get_user_apps`. |
