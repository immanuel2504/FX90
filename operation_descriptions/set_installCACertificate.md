## 1. Description

The `set_installCACertificate` command installs a CA (Certificate Authority) root certificate on the reader by providing the PEM-encoded certificate content inline in the payload.

This command allows you to configure:

- The CA certificate name on the reader through `name`
- The PEM-encoded certificate content through `content`

Use this command to:

- Trust a private CA so the reader can validate TLS connections to your MQTT or HTTPS endpoints
- Add a CA root certificate required for chain validation before mutual TLS is configured
- Support your organization's PKI for both client and server TLS certificate validation

## 2. Command Details

| Property | Value |
|---|---|
| Pattern Name | CA Certificate Installation |
| Communication Type | Bidirectional (Cloud to Device, Device to Cloud) |
| Applies To | FXR90 |
| Related Commands | [get_CACertificates](get_CACertificates.md), [del_CACertificate](del_CACertificate.md), [set_update_cert](set_update_cert.md) |
| Required Payload Fields | `name`, `content` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Have the CA certificate's PEM content ready before sending this command. Invalid PEM content will be rejected and the CA will not be installed.

| What You Need | Details |
|---|---|
| CA certificate name | A unique name to assign this CA certificate on the reader. If a CA with this name already exists, it will be replaced. |
| PEM content | The full PEM-encoded CA certificate string, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` headers and footers. |
| Certificate validity | Confirm the CA certificate is not expired before installing it. An expired CA root will still install but will fail to validate any certificates it issued. |
| Intended use | Know which MQTT broker or HTTP endpoint TLS certificate is issued by this CA, so you can verify the chain after installation. |

