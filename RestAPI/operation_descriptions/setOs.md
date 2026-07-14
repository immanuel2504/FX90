## 1. Description

The `PUT /cloud/os` REST endpoint updates the reader's operating system firmware by downloading and installing a build from a URL.

This endpoint allows you to configure:

- The firmware download URL through `url`
- The download authentication method through `authenticationType`
- Download credentials through `options`
- Optional custom HTTP headers through `headers`

Use this endpoint to:

- Upgrade the reader to a newer OS build
- Deploy firmware from an internal HTTP(S) artifact repository
- Perform a scheduled firmware update across a fleet of readers

## 2. Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | OS Firmware Update |
| REST Endpoint | `PUT /cloud/os` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |
| Required Request Fields | `url`, `authenticationType` |
| Supported Authentication Types | `NONE`, `BASIC` |

## 3. Before You Begin

Gather all firmware download details before sending this request. A failed OS update can take the reader offline - plan for maintenance downtime and ensure the firmware URL is reachable from the reader's network before proceeding.

| What You Need | Details |
|---|---|
| Firmware URL | The HTTP(S) URL of the firmware directory. The reader fetches a file list from this URL, then downloads the appropriate build. |
| Authentication type | `NONE` if no download credentials are required, or `BASIC` for username/password HTTP authentication. |
| Download credentials | Required when `authenticationType` is `BASIC`. Provide `options.username` and `options.password`. |
| JWT bearer token | Optional - supply a JWT in `headers.Authorization` for token-based authentication, regardless of `authenticationType`. |
| Network reachability | The reader must be able to reach the firmware URL on the network. Confirm firewall rules allow HTTP(S) outbound on the port used by the firmware server. |
| Current firmware version | Use `GET /cloud/version` to confirm the reader's current build before initiating an update. |
| Rollback plan | If the update fails, use `PUT /cloud/revertbackOS` to return to the previous OS version. |
