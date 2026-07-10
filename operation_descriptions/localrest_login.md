The `localrest_login` command authenticates a session with the reader's local REST interface.

Use this command to:

- Establish an authenticated session for local REST API access
- Obtain credentials for subsequent local configuration calls

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Local REST Login |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/localRestLogin` |
| Related Commands | [set_password](set_password.md) |
| Supported API Versions | V1.0 |

## Before You Begin

Have valid admin reader credentials available before authenticating. On success, the response contains `code` (`0` = success) and `message` (the session bearer token used for subsequent local REST calls).

| What You Need | Details |
|---|---|
| Admin credentials | A valid reader admin username and password to authenticate the local REST session. |
