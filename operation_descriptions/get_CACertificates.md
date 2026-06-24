## 1. Description

The `get_CACertificates` command retrieves the list of CA certificates installed on the reader.

This command returns:

- An array of installed CA certificate names and their details

No additional payload fields are required to retrieve the CA certificate list.

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | CA Certificate Inventory Query |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [set_installCACertificate](set_installCACertificate.md), [del_CACertificate](del_CACertificate.md), [get_certs](get_certs.md) |
| Supported Operations | List installed CA certificates |
| Supported Response Sections | payload, response |
| Supported API Versions | V1.0 |

## 3. When to Use This Command

Use `get_CACertificates` to:

- Audit installed CA trust anchors before adding or removing a CA certificate
- Confirm a CA certificate exists before referencing it in a TLS endpoint configuration
- Verify that a CA certificate installation or deletion completed successfully

Key fields to check in the response:

| Field | What to Check | Why It Matters |
|---|---|---|
| Certificate name | Is the expected CA certificate listed? | A missing CA certificate will cause TLS chain validation to fail for endpoints that depend on it. |
| Count | How many CA certificates are installed? | Confirms no accidental duplicates or missing entries after certificate management operations. |
