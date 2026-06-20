The `set_update_cert` command installs or updates a certificate on the reader, fetched from an FTPS URL or supplied inline as PFX content.

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

Gather these details before sending the command. An invalid URL, wrong certificate type, or bad PFX password will cause installation to fail.

| What You Need | Details |
|---|---|
| Certificate name | Unique name for the certificate on the reader. |
| Certificate type | `server`, `client`, or `app`. |
| Source | FTPS `url` hosting the certificate/PFX, **or** inline `pfxFileName` + `pfxContent`. |
| FTPS authentication | `NONE` or `BASIC` (with `options.username` / `options.password`). |
| PFX password | Password for the PFX file, if applicable. |

## 4. Authentication Types

The `authenticationType` field controls FTPS server authentication.

| authenticationType | Description | Credentials Required |
|---|---|---|
| `NONE` | No FTPS authentication | None |
| `BASIC` | Username/password FTPS auth | `options.username`, `options.password` |
