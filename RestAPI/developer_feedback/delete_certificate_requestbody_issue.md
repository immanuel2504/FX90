# Design issue: `DELETE /cloud/certificates/{certname}` carries a request body

**Status:** Open — needs a device-side decision. No spec change has been made.
**Affects:** `DELETE /cloud/certificates/{certname}` (operationId `delCertificate`)
**Raised:** 2026-07-13

## What the API does today

The delete operation requires a JSON request body containing the certificate type:

```http
DELETE /cloud/certificates/reader HTTP/1.1
Authorization: Bearer <token>
Content-Type: application/json

{ "type": "client" }
```

`type` is a required field (`server` | `client` | `app`). The certificate name comes from the
`{certname}` path parameter, but the type does not — it can only be supplied in the body.

## Why this is a problem

**HTTP does not define semantics for a DELETE request body.** RFC 9110 §9.3.5 states that a
payload on DELETE has no defined meaning and that sending one "might cause some existing
implementations to reject the request."

The practical consequences:

- **Intermediaries may strip it.** Some proxies, load balancers, CDNs and API gateways drop
  DELETE bodies in transit. The reader would then receive a request with no `type` and fail —
  and the failure would look like a device fault, not a network one.
- **Client libraries may not send it.** Several widely used HTTP clients either omit the body on
  DELETE or require a non-obvious workaround. `XMLHttpRequest` and older `fetch` polyfills are
  examples; some generated SDKs simply drop it.
- **Tooling rejects it.** OpenAPI 3.0 forbids `requestBody` on DELETE outright. The classic
  Swagger Editor reports it as a semantic error. OpenAPI 3.1 permits it, but only because 3.1
  defers to HTTP, which leaves it undefined.

This is a latent field-reliability issue, not just a documentation nit. It works on a direct
LAN connection to the reader and may fail once a proxy sits in the path.

## Recommended change (device-side)

Move `type` to a query parameter:

```http
DELETE /cloud/certificates/reader?type=client HTTP/1.1
Authorization: Bearer <token>
```

This is safe for intermediaries, works in every HTTP client, and satisfies both OpenAPI 3.0 and
3.1. `PUT /cloud/certificates/{certname}` (refresh) has the same shape and should be considered
alongside it, though PUT with a body is well-defined and therefore not urgent.

## Why the spec was NOT changed

The OpenAPI file must describe what the device actually does. Rewriting the spec to show a query
parameter while the firmware still reads a JSON body would make the documentation wrong and break
every client generated from it.

The change has to land in the firmware first. Once it does, the spec follows.

## Interim guidance

Nothing to fix in the spec. `RestDeveloperfile_final.yaml` is valid OpenAPI 3.1 and documents the
current behaviour correctly.

The "Semantic error / Unable to render" message seen in `editor.swagger.io` is that tool applying
OpenAPI **3.0** rules — the classic Swagger Editor does not support 3.1 at all. Use a 3.1-capable
renderer instead:

- `editor-next.swagger.io`
- Swagger UI 5.x
- Redocly

The spec relies on 3.1-only features that cannot be expressed in 3.0 without losing real
validation — `patternProperties` (read-point keys 1-8 on cable loss compensation), `const` and
`contains` (the mutually-exclusive `tagQuietMasks` rules on Impinj Gen2X), and `type: 'null'`.
Downgrading the spec to 3.0 to satisfy the old editor would silently discard those constraints and
is not recommended.
