## 1. Description

The `get_certs` command retrieves the list of certificates installed on the reader.

This command returns:

- An array of installed certificates, each with name, type, serial, and validity dates

No additional payload fields are required to retrieve all installed certificates.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Inventory Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | set_update_cert, del_certs, refresh-cert |
| Supported Operations | Retrieve the list of installed certificates |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_certs` to:

- Audit which certificates are installed and their types
- Check certificate validity windows before expiry
- Confirm a certificate was installed or removed
- Retrieve the full list of certificates on the device
