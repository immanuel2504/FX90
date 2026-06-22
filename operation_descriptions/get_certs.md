## 1. Description

The `get_certs` command retrieves the list of certificates installed on the reader.

This command returns:

- An array of installed certificates, each with name, type, serial number, and validity dates

No additional payload fields are required to retrieve all installed certificates.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Inventory Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/certificates` |
| Related Commands | [set_update_cert](set_update_cert.md), [del_certs](del_certs.md), [refresh-cert](refresh-cert.md) |
| Required Request Fields | command, command_id |
| Supported Operations | Retrieve the list of installed certificates |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_certs` to:

- Audit which certificates are installed and their types
- Check certificate validity windows before expiry
- Confirm a certificate was successfully installed or removed
- Retrieve the full certificate list before a scheduled rotation

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| `name` | Does the certificate name match what was installed? | Confirms the correct certificate is present for TLS or authentication. |
| `type` | What type of certificate is it? | Differentiates between device, CA, and client certificates used for different purposes. |
| `notValidAfter` | When does it expire? | Expired certificates will cause TLS handshake failures and connectivity loss. |
| `serialNumber` | Does the serial match the expected certificate? | Verifies the exact certificate instance installed, useful for rotation audits. |
