## 1. Description

The `set_password` command allows you to edit the `admin` and `rfidadm` password.

Only the password is changed. `userName` selects **which** of the two accounts to update — it does not rename an account, and it cannot create one.

This command allows you to configure:

- Which account to change through `userName` (`admin` or `rfidadm`)
- That account's existing password through `currentPassword`
- The new password to set through `newPassword`

Use this command to:

- Rotate reader credentials as part of a security policy
- Set a new password during initial reader provisioning
- Respond to a credential exposure or security incident

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Password Change |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `PUT /cloud/updatePassword` |
| Related Commands | [localrest_login](localrest_login.md) |
| Required Payload Fields | `userName`, `currentPassword`, `newPassword` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm the current password and the target account before sending this command. Using the wrong current password will cause the command to fail.

| What You Need | Details |
|---|---|
| Account | Which account to change, supplied in `userName`: `admin` or `rfidadm`. This selects the account only — the account itself is not renamed. |
| Current password | The account's existing password. Required for authentication - the command will fail if this is incorrect. |
| New password | The new password to set. Apply your organization's password policy (minimum length, complexity requirements). |

