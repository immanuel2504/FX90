## 1. Description

The `del_CACertificate` command removes an installed CA (Certificate Authority) root certificate from the reader. When you run this command, the CA certificate identified by name is permanently deleted from the reader's CA certificate store.

Use this command to:

- Remove a CA certificate that is no longer trusted or has been compromised
- Clean up the CA store before installing a replacement with `set_installCACertificate`
- Rotate PKI trust anchors on the reader as part of a certificate lifecycle policy

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | CA Certificate Deletion |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_CACertificates](get_CACertificates.md), [set_installCACertificate](set_installCACertificate.md), [del_certs](del_certs.md) |
| Required Payload Fields | `name` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm the CA certificate is safe to remove before sending this command. Deleting a CA that is actively used for TLS verification will cause all TLS connections that depend on it to fail.

| What You Need | Details |
|---|---|
| CA certificate name | The exact `name` of the CA certificate to delete, as returned by `get_CACertificates`. The name is case-sensitive. |
| Active use check | Identify all MQTT or HTTPS endpoints whose server or client certificates are issued by this CA. Remove those dependencies or install a replacement CA before deleting. |

