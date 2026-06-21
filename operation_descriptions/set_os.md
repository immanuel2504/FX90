## 1. Description

The `set_os` command updates the reader's operating system firmware by downloading and installing a build from a URL.

This command allows you to configure:

- The firmware download URL through `url`
- The download authentication method through `authenticationType`
- Download credentials through `options`
- Optional custom HTTP headers through `headers`

Use this command to:

- Upgrade the reader to a newer OS build
- Deploy firmware from an internal HTTP(S) artifact repository
- Perform a scheduled firmware update across a fleet of readers

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | OS Firmware Update |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_version](get_version.md), [revertback](revertback.md), [get_status](get_status.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | `url`, `authenticationType` |
| Supported Authentication Types | `NONE`, `BASIC` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Gather all firmware download details before sending this command. A failed OS update can take the reader offline — plan for maintenance downtime and ensure the firmware URL is reachable from the reader's network before proceeding.

| What You Need | Details |
|---|---|
| Firmware URL | The HTTP(S) URL of the firmware directory. The reader fetches a file list from this URL, then downloads the appropriate build. |
| Authentication type | `NONE` if no download credentials are required, or `BASIC` for username/password HTTP authentication. |
| Download credentials | Required when `authenticationType` is `BASIC`. Provide `options.username` and `options.password`. |
| JWT bearer token | Optional — supply a JWT in `headers.Authorization` for token-based authentication, regardless of `authenticationType`. |
| Network reachability | The reader must be able to reach the firmware URL on the network. Confirm firewall rules allow HTTP(S) outbound on the port used by the firmware server. |
| Current firmware version | Use `get_version` to confirm the reader's current build before initiating an update. |
| Rollback plan | If the update fails, use `revertback` to return to the previous OS version. |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or the firmware update to not complete.

### Required Fields

- `url` and `authenticationType` are required in the payload. Omitting either will cause the command to be rejected.

### Authentication

- When `authenticationType` is `BASIC`, `options.username` and `options.password` must both be provided. Omitting either field will cause the download to fail with an HTTP 401 error.
- When `authenticationType` is `NONE`, the `options` object must be omitted or empty.

### URL Reachability

- The reader must have network connectivity to the firmware URL at the time this command is sent. An unreachable URL will result in a download timeout.
- HTTPS is strongly recommended for firmware download URLs to prevent tampering with the firmware image in transit.

### Apply Timing

- Firmware updates are applied immediately after the download completes. The reader will reboot as part of the update process.
- Plan for the reader to be offline during the update and reboot. Inventory and API connectivity will be interrupted.
- After reboot, use `get_version` to confirm the new firmware version was successfully applied.

### Rollback

- The previous OS version is retained and can be restored using the `revertback` command if the update produces unexpected behavior.

### Security Note

- Never hardcode download credentials (`username`, `password`) or JWT tokens in your payload. Supply all sensitive values from a secrets manager or environment variable at runtime.
- Use HTTPS for firmware download URLs to prevent the firmware image from being tampered with or replaced in transit.
