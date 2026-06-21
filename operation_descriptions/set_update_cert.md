The `set_update_cert` command installs or updates a certificate on the reader by downloading a PFX file from a URL.

Use it to:

- Install a new TLS certificate for MQTT or HTTP endpoints
- Update an existing certificate before expiry
- Provision client, server, or application certificates

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Installation |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_certs](get_certs.md), [del_certs](del_certs.md), [refresh-cert](refresh-cert.md) |
| Supported Operations | Install or update a certificate |
| Supported API Versions | V1.0 |


## 3. Before You Begin

Gather these details before sending the command. An invalid URL, wrong certificate type, missing download credentials, or bad PFX password will cause installation to fail.

| What You Need | Details |
|---|---|
| Certificate name | Unique name for the certificate on the reader. |
| Certificate type | `client`, `server`, or `app`. |
| Source | `url` where the certificate PFX file can be downloaded. |
| Download authentication | `NONE` or `BASIC` (with `authenticationOptions.username` / `authenticationOptions.password`). |
| PFX password | Password for the PFX certificate file, if applicable. |

## 4. Authentication Types

The `authenticationType` field controls authentication for downloading the certificate.

| authenticationType | Description | Credentials Required |
|---|---|---|
| `NONE` | No download authentication | None |
| `BASIC` | Username/password authentication | `authenticationOptions.username`, `authenticationOptions.password` |
