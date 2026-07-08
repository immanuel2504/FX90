The `PUT /cloud/certificates` REST endpoint is used to install or update a certificate on the reader by downloading a PFX file from a URL.

## 2. Endpoint Details

| Property | Value |
|---|---|
| REST Endpoint | `PUT /cloud/certificates` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` where a request body is required |

## 3. Usage Notes

This REST endpoint corresponds to the `set_updateCertificate` MQTT command where applicable. REST and MQTT use the same certificate install payload fields: `name`, `type`, `url`, `authenticationType`, `options`, and `pfxPassword`.

Allowed `type` values are `client`, `server`, and `app`. Allowed `authenticationType` values are `NONE` and `BASIC`.
