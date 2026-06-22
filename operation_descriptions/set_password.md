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
| Required Request Fields | `command`, `command_id`, `payload` |
| Required Payload Fields | `userName`, `currentPassword`, `newPassword` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm the current password and the target username before sending this command. Using the wrong current password will cause the command to fail.

| What You Need | Details |
|---|---|
| Username | The username of the account to update (e.g., `admin`). |
| Current password | The account's existing password. Required for authentication - the command will fail if this is incorrect. |
| New password | The new password to set. Apply your organization's password policy (minimum length, complexity requirements). |

## 4. Rules and Constraints

Violating any of these rules will cause the command to fail or the password change to be rejected.

### Required Fields

- `userName`, `currentPassword`, and `newPassword` are all required. Omitting any field will cause the command to be rejected.

### Authentication

- `currentPassword` must match the account's existing password exactly. An incorrect current password will cause the command to fail with an authentication error.

### Password Policy

- The `newPassword` must meet the reader's password complexity requirements. A password that does not meet minimum length or character requirements will be rejected.
- Do not reuse the current password as the new password.

### Apply Timing

- The password change takes effect immediately after the command is acknowledged.
- Subsequent REST API login attempts must use the new password.

### Security Note

- Never hardcode `currentPassword` or `newPassword` values in your payload source code or configuration files. Supply all password values from a secrets manager or secure environment variable at runtime.
- Transmit password change commands only over an encrypted channel (TLS-protected MQTT or HTTPS).
