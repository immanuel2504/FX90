## 1. Description

The `set_os` command updates the reader's operating system firmware from an HTTP(S) URL.

Use it to:

- Upgrade the reader to a newer OS build
- Deploy firmware from an internal HTTP(S) repository
- Roll forward after validating available upgrades via `get_version`

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | OS Firmware Update |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_version](get_version.md), [revertback](revertback.md), [get_status](get_status.md) |
| Supported Operations | Update OS firmware from URL |
| Supported API Versions | V1.0 |


## 3. Before You Begin

Gather these details before sending the command. A failed OS update can leave the reader offline — plan for downtime and verify the firmware URL is reachable from the reader.

| What You Need | Details |
|---|---|
| Firmware URL | HTTP(S) URL of the firmware folder (GET returns a JSON file list). |
| Authentication | `NONE` or `BASIC` (username/password), or JWT via `headers.Authorization`. |
| TLS validation | Whether to verify server cert/hostname; CA cert path or inline content if needed. |

## 4. Authentication Types

The `authenticationType` field controls HTTP(S) server authentication.

| authenticationType | Description | Credentials Required |
|---|---|---|
| `NONE` | No HTTP authentication | None |
| `BASIC` | Username/password auth | `options.username`, `options.password` |

JWT bearer tokens may be supplied via `payload.headers.Authorization` regardless of `authenticationType`.
