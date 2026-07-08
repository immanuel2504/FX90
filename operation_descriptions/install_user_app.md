The `install_user_app` command installs a user application (`.deb` package) on the reader from an HTTP(S) file server.

Use this command to:

- Deploy custom on-reader applications
- Update user-app packages from a central repository
- Extend reader functionality with Zebra-approved `.deb` packages

## Command Details

| Property | Value |
|---|---|
| Pattern Name | User Application Installation |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/apps/install` |
| Related Commands | [get_user_apps](get_user_apps.md), [uninstall-user-app](uninstall-user-app.md), [start_user_app](start_user_app.md) |
| Supported Authentication Types | `NONE`, `BASIC` |
| Supported API Versions | V1.0 |


MQTT command key: `install_user_app`.

## Before You Begin

Gather download server details before sending. The reader must reach the URL from its network.

| What You Need | Details |
|---|---|
| File server URL | HTTP or HTTPS base URL hosting the `.deb` package. |
| Filename | Exact `.deb` filename on the server. |
| Authentication | `NONE` or `BASIC` (with `options.username` / `options.password`). |
| TLS verification | `verifyPeer`, `verifyHost`, and optional CA cert path or inline content. |

## Authentication Types

| authenticationType | Description | Credentials Required |
|---|---|---|
| `NONE` | No HTTP authentication | None |
| `BASIC` | Username/password auth | `options.username`, `options.password` |
