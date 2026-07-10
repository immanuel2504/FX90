## 1. Description

The `DELETE /cloud/certificates/{certname}` REST endpoint removes an installed certificate from the reader. When you call this endpoint, the certificate identified by the `{certname}` path parameter and its `type` is deleted from the reader's certificate store.

Use this endpoint to:

- Remove expired or revoked TLS certificates before installing a replacement
- Clean up the certificate store after a certificate rotation
- Delete client or server certificates that are no longer needed for MQTT or HTTPS authentication

## 2. Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | Certificate Deletion |
| REST Endpoint | `DELETE /cloud/certificates/{certname}` |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |
| Related Endpoints | [getCertificates](getCertificates.md), [setUpdatecertificate](setUpdatecertificate.md), [setRefreshCertificate](setRefreshCertificate.md) |
| Path Parameter | `certname` (the certificate name to delete) |
| Required Request Fields | `type` |
| Supported Certificate Types | `client`, `server`, `app` |
| Supported API Versions | V1.0 |

## 3. Before You Begin

Confirm the certificate is no longer in use before sending this request. Cross-reference the certificate name and type with your active endpoint configuration and the list returned by `GET /cloud/certificates`.

| What You Need | Details |
|---|---|
| Certificate name | The exact name of the certificate to delete, supplied as the `{certname}` path parameter, as returned by `GET /cloud/certificates`. The name is case-sensitive. |
| Certificate type | The `type` of the certificate: `client`, `server`, or `app`, sent in the request body. The type must match the installed certificate. |
| Active use check | Confirm the certificate is not currently used for an active MQTT TLS or HTTPS endpoint connection. Deleting an in-use certificate will cause TLS handshake failures on the next reconnect. |
