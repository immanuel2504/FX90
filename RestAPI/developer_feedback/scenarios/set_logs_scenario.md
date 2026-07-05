# `set_logs` — schema clarification (scenario)

**Commands:** `get_logs`, `set_logs`  
**REST endpoints:** `GET /cloud/logs`, `PUT /cloud/logs`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_logs` command for `/cloud/logs` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/logs`, the example request is:

```json
{
  "components": [
    { "componentName": "radio_control", "level": "DEBUG" }
  ]
}
```

But `componentName` and `level` are defined only as:

```yaml
componentName:
  type: string
level:
  type: string
```

Since there is no `enum`, Swagger treats these as any string value. For example, `"level": "DEBUG"`, `"level": "abc"`, or `"componentName": "test"` would all be valid according to the schema.

Could you please confirm:

* the valid log `level` values (e.g. `ERROR`, `WARNING`, `INFO`, `DEBUG`) and add an `enum`
* the valid `componentName` values, or reference how to obtain them (e.g. from `get_logs`)

Also, please add descriptions for `componentName`, `level`, and `radioPacketLog`.

This will make the OpenAPI specification clearer and avoid confusion for API users.
