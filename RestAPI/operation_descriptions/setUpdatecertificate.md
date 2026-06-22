The `PUT /cloud/certificates` REST endpoint is used to install or update a certificate on the reader by downloading a PFX file from a URL.

Use this endpoint to:

- Install a client, server, or application certificate.
- Download the certificate PFX file from the supplied `url`.
- Use optional BASIC download credentials through `authenticationOptions`.
- Perform the operation through the REST API using bearer-token authentication.
- Keep REST behavior aligned with the documented reader workflow.

## 2. Endpoint Details

| Property | Value |
|---|---|
| MQTT Command | `set_update_cert` |
| REST Endpoint | `PUT /cloud/certificates` |
| Operation ID | `setUpdatecertificate` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_updateCertificate` MQTT command where applicable. REST and MQTT use the same certificate install payload fields: `name`, `type`, `url`, `authenticationType`, `authenticationOptions`, and `pfxPassword`.

Allowed `type` values are `client`, `server`, and `app`. Allowed `authenticationType` values are `NONE` and `BASIC`.
