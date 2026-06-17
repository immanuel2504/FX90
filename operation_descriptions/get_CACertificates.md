## 1. Description

The `get_CACertificates` command lists CA certificates installed on the reader.

Use this command to:

- Audit installed CA trust anchors
- Confirm a CA exists before referencing it in TLS endpoints
- Verify deletion or installation of CA certs

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | CA Certificate Inventory Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_installCACertificate](set_installCACertificate.md), [del_CACertificate](del_CACertificate.md) |
| Supported Operations | List installed CA certificates |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_CACertificates` before installing or deleting CA certificates.
