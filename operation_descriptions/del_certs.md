## 1. Description

The `del_certs` command removes an installed certificate from the reader. When you run this command, the certificate identified by name and type is deleted from the reader's certificate store.

> **The server certificate cannot be deleted through this API.** Only `client` and `app` certificates can be removed — the `type` field accepts `client` or `app` only. The reader's server certificate is required for TLS and has no delete operation.

Use this command to:

- Remove expired or revoked client TLS certificates before installing a replacement
- Clean up the certificate store after a certificate rotation
- Delete client or app certificates that are no longer needed for MQTT or HTTPS authentication

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Deletion |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| REST Endpoint | `DELETE /cloud/certificates/{certname}` |
| Related Commands | [get_certs](get_certs.md), [set_update_cert](set_update_cert.md), [refresh-cert](refresh-cert.md), [del_CACertificate](del_CACertificate.md) |
| Required Payload Fields | `name`, `type` |
| Supported Certificate Types | `client`, `app` (the `server` certificate cannot be deleted) |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm the certificate is no longer in use before sending this command. Cross-reference the certificate name and type with your active endpoint configuration and the list returned by `get_certs`.

| What You Need | Details |
|---|---|
| Certificate name | The exact `name` of the certificate to delete, as returned by `get_certs`. The name is case-sensitive. |
| Certificate type | The type of the certificate: `client` or `app`. The type must match the installed certificate. The `server` certificate cannot be deleted. |
| Active use check | Confirm the certificate is not currently used for an active MQTT TLS or HTTPS endpoint connection. Deleting an in-use certificate will cause TLS handshake failures on the next reconnect. |

