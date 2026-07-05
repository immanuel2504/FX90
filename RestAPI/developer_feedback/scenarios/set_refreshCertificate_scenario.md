# `set_refreshCertificate` — schema clarification (scenario)

**Command:** `set_refreshCertificate`  
**REST endpoint:** `PUT /cloud/certificates/{certname}`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_refreshCertificate` command for `/cloud/certificates/{certname}` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/certificates/Server`, the example request is:

```json
{
  "name": "Server",
  "type": "server"
}
```

The `name` field is already well documented (REST path parameter vs MQTT payload) — thank you. One thing is unclear:

`type` is defined only as:

```yaml
type:
  type: string
```

So `"type": "server"`, `"type": "client"`, or `"type": "abc"` would all be valid according to the schema. Could you confirm the valid certificate types and add an `enum` and a description?

Also, please add a response schema for the `200` response (currently `description: OK` only, with no body defined).

This will make the OpenAPI specification clearer and avoid confusion for API users.
