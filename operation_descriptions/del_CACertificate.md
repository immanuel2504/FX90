The `del_CACertificate` command removes an installed CA (Certificate Authority) root certificate from the reader.

Use this command to:

- Remove a CA certificate that is no longer trusted
- Clean up CA entries before installing a replacement with `set_installCACertificate`
- Rotate PKI trust anchors on the device

## Command Details

| Property | Value |
|---|---|
| Pattern Name | CA Certificate Deletion |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_CACertificates](get_CACertificates.md), [set_installCACertificate](set_installCACertificate.md) |
| Supported API Versions | V1.0 |

## Before You Begin

Deleting a CA certificate used for TLS verification on active endpoints will cause connection failures.

| What You Need | Details |
|---|---|
| CA name | Exact `name` of the CA certificate to delete. |
