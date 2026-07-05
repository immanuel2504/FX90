# `set_gpo` — schema clarification (scenario)

**Commands:** `get_gpoStatus`, `set_gpo`  
**REST endpoints:** `GET /cloud/gpo`, `PUT /cloud/gpo`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_gpo` command for `/cloud/gpo` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/gpo`, the example request is:

```json
{
  "port": 3,
  "state": true
}
```

But `port` is defined only as:

```yaml
port:
  type: number
```

Since there is no `minimum`/`maximum`, Swagger treats this as any number. For example, `port: 3`, `port: 99`, or `port: -1` would all be valid according to the schema, even though the endpoint description says FXR90 has only 4 GPO pins.

Could you please confirm the valid port range and add `minimum`/`maximum` (or a description) to the schema?

Also, please add:

* descriptions for `port` and `state`
* a description for the `PUT /cloud/gpo` response, because it currently returns an empty string and the schema does not explain it

This will make the OpenAPI specification clearer and avoid confusion for API users.
