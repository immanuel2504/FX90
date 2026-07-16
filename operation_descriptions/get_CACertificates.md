## 1. Description

The `get_CACertificates` command retrieves the list of CA (Certificate Authority) certificates currently installed on the reader.

The response payload is an array of the installed CA certificate names.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | CA Certificate Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `GET /cloud/caCertificates` |
| Related Commands | [set_installCACertificate](set_installCACertificate.md), [del_CACertificate](del_CACertificate.md), [get_certs](get_certs.md) |
| Supported Operations | List installed CA certificate names |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_CACertificates` to:

- Confirm which CA certificates are installed before configuring a TLS endpoint that must trust them
- Audit the reader's CA trust store across a fleet
- Verify a CA certificate was installed successfully after `set_installCACertificate`, or removed after `del_CACertificate`
