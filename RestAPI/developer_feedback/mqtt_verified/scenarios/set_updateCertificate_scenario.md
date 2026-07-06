# `set_updateCertificate` — schema clarification (scenario)

**Command:** `set_updateCertificate`  
**REST endpoint:** `PUT /cloud/certificates`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_updateCertificate` command for `/cloud/certificates` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/certificates`, the example request is:

```json
{
  "authenticationType": "BASIC",
  "authenticationOptions": { "username": "zebra", "password": "zebra" },
  "name": "reader",
  "type": "client",
  "url": "https://10.117.229.15/reader.pfx",
  "pfxPassword": "abcd12345"
}
```

`authenticationType` already has an `enum` (`NONE`, `BASIC`) — thank you. Two things are still unclear:

1. **`type` values** — `type` is defined only as:

```yaml
type:
  type: string
```

So `"type": "client"`, `"type": "server"`, or `"type": "abc"` would all be valid. The Zebra IoTC MQTT documentation already restricts this to `enum: [client, server, app]` — please copy the same `enum` into `openAPISpec.yaml` (note `app` is a valid third value).

2. **Required fields** — no fields are marked `required`, so an empty body would be valid according to the schema. The Zebra IoTC MQTT documentation already declares `required: [name, type, url]` — please align `openAPISpec.yaml`.

Also, please add:

* descriptions for the request fields
* a response schema for the `200` response (currently `description: OK` only, with no body defined)

This will make the OpenAPI specification clearer and avoid confusion for API users.
