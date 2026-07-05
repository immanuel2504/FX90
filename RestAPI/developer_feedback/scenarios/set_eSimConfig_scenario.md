# `set_eSimConfig` — schema clarification (scenario)

**Commands:** `get_eSimConfig`, `set_eSimConfig`  
**REST endpoints:** `GET /cloud/eSimConfig`, `PUT /cloud/eSimConfig`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_eSimConfig` command for `/cloud/eSimConfig` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/eSimConfig`, the example request is:

```json
{
  "operation": "enable",
  "profileNickName": "gnd1"
}
```

`operation` is defined only as:

```yaml
operation:
  type: string
```

So `"operation": "enable"`, `"operation": "disable"`, or `"operation": "abc"` would all be valid. Could you confirm the valid operations and add an `enum`?

Also, in the `get_eSimConfig` response, `enabled` is returned as a string:

```json
{
  "profiles": [
    { "enabled": "true", "iccid": "8944500411193057192F" }
  ]
}
```

The schema defines it as `type: string`. Should `enabled` be `type: boolean`? If it must remain a string, please add `enum: ["true", "false"]`.

Also, please add:

* descriptions for the request/response fields
* a response schema for the `200` response (currently `description: OK` only, with no body defined)

This will make the OpenAPI specification clearer and avoid confusion for API users.
