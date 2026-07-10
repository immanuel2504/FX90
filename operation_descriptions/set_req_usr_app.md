## 1. Description

The `set_req_usr_app` command sends a custom request or data payload to a user application running on the reader.

This command allows you to configure:

- The target user application through `userapp`
- The command or data payload to deliver through `command`

Use this command to:

- Invoke custom logic in an installed user application
- Pass structured data or control commands to the application layer
- Integrate third-party processing running directly on the reader

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | User Application Request |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/apps/{appname}/pass-through` |
| Related Commands | [get_user_apps](get_user_apps.md), [start_user_app](start_user_app.md), [stop_user_app](stop_user_app.md) |
| Required Payload Fields | `userapp`, `command` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm the target user application is installed and running before sending this command. A request to a stopped or missing application will fail.

| What You Need | Details |
|---|---|
| Application name | The exact application name, supplied as `userapp` (from `get_user_apps`). The name is case-sensitive and must match exactly. |
| Command or data | The `command` object to pass to the user application (for example, `command.message`). The expected structure is defined by the user application, not by the reader API. |
| Application state | Use `get_user_apps` to confirm the target application is running (`runningStatus: true`) before sending. A stopped application may not be able to process the request. |

