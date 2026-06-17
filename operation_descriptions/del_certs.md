## Description

The `del_certs` command removes an installed certificate from the reader by name and type.

Use this command to:

- Remove expired or replaced TLS certificates
- Clean up unused certificate entries
- Rotate credentials before installing a replacement with `set_update_cert`

## Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Deletion |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_certs](get_certs.md), [set_update_cert](set_update_cert.md), [refresh-cert](refresh-cert.md) |
| Supported Certificate Types | `client`, `server`, `app` |
| Supported API Versions | V1.0 |


## Before You Begin

Confirm the certificate is no longer in use. Cross-reference the certificate `name` with endpoint configuration and `get_certs`.

| What You Need | Details |
|---|---|
| Certificate name | Exact `name` from `get_certs`. |
| Certificate type | `client`, `server`, or `app`. |
