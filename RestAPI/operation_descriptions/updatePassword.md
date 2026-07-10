## 1. Description

The `PUT /cloud/updatePassword` REST endpoint changes the password for a reader user account.

This endpoint allows you to configure:

- The username of the account to update through `userName`
- The current password for authentication through `currentPassword`
- The new password to set through `newPassword`

Use this endpoint to:

- Rotate reader credentials as part of a security policy
- Set a new password during initial reader provisioning
- Respond to a credential exposure or security incident

## 2. Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | Password Change |
| REST Endpoint | `PUT /cloud/updatePassword` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |
| Related Endpoints | [localRestLogin](localRestLogin.md) |
| Required Request Fields | `userName`, `currentPassword`, `newPassword` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm the current password and the target username before sending this request. Using the wrong current password will cause the request to fail.

| What You Need | Details |
|---|---|
| Username | The username of the account to update (e.g., `admin`). |
| Current password | The account's existing password. Required for authentication - the request will fail if this is incorrect. |
| New password | The new password to set. Apply your organization's password policy (minimum length, complexity requirements). |
