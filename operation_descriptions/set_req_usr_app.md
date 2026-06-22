## 1. Description

The `set_req_usr_app` command sends a custom request or data payload to a user application running on the reader.

This command allows you to configure:

- The target user application through `appname`
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
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | `appname`, `command` (inner) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm the target user application is installed and running before sending this command. A request to a stopped or missing application will fail.

| What You Need | Details |
|---|---|
| Application name | The exact `appname` value from `get_user_apps`. The name is case-sensitive and must match exactly. |
| Command or data | The string or JSON object to pass to the user application via `payload.command`. The expected format is defined by the user application, not by the reader API. |
| Application state | Use `get_user_apps` to confirm the target application is running (`running: true`) before sending. A stopped application may not be able to process the request. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or the user application to not receive the request.

### Required Fields

- `appname` and `command` (inner payload field) are both required. Omitting either will cause the command to be rejected.

### Application Name

- `appname` must exactly match an installed application name returned by `get_user_apps`. An unrecognized or misspelled name will cause the command to fail.

### Application State

- The target user application must be installed and running. Sending to a stopped application may result in the command being dropped or returning an error.
- Use `start_user_app` to start the application before sending if it is not currently running.

### Command Payload

- The `command` field value is passed directly to the user application. Its format and valid values are defined by the user application, not the reader firmware. Ensure the application can handle the provided value.

### Apply Timing

- The request is delivered to the user application immediately after the command is acknowledged. Processing time depends on the user application's response time.

### Security Note

- The `command` field may contain application-specific credentials or sensitive data depending on the user application's interface. If so, supply these values from a secrets manager or environment variable at runtime rather than hardcoding them in the payload.
