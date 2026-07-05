## 1. Description

The `set_password` command changes the password for a reader user account.

This command allows you to configure:

- The username of the account to update through `userName`
- The current password for authentication through `currentPassword`
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

Confirm the current password and the target username before sending this command. Using the wrong current password will cause the command to fail.

| What You Need | Details |
|---|---|
| Username | The username of the account to update (e.g., `admin`). |
| Current password | The account's existing password. Required for authentication - the command will fail if this is incorrect. |
| New password | The new password to set. Apply your organization's password policy (minimum length, complexity requirements). |

