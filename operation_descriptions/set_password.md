## Description

The `set_password` command changes a reader user's password.

Use this command to:

- Rotate reader credentials
- Set a new password during provisioning
- Recover from or respond to credential exposure

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Password Change |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [localrest_login](localrest_login.md) |
| Required Request Fields | `command`, `command_id`, `payload` |
| Supported Operations | Change reader user password |
| Supported API Versions | V1.0 |

## Before You Begin

Confirm the current password and target user before sending the command. Store passwords securely and avoid hardcoding credentials in source code or documentation.

## Request Fields

| Field | Type | Required | Description |
|---|---|---|---|
| `payload.currentPassword` | string | No | Current password for the target user. |
| `payload.newPassword` | string | No | New password to assign. |
| `payload.userName` | string | No | User account whose password should be changed. |
