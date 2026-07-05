# `set_passthru` — schema clarification (scenario)

**Command:** `set_passthru`  
**REST endpoint:** `PUT /cloud/pass-through`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_passthru` command for `/cloud/pass-through` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/pass-through`, the example request is:

```json
{
  "component": "RC",
  "payload": "status"
}
```

But `component` and `payload` are defined only as:

```yaml
component:
  type: string
payload:
  type: string
```

Since there is no `enum`, Swagger treats these as any string value. For example, `"component": "RC"`, `"component": "abc"`, or `"payload": "test"` would all be valid according to the schema.

Could you please confirm the valid `component` values (e.g. `RC`) and the valid `payload` values (e.g. `mode`, `status`) and add `enum`s if the sets are fixed?

Two more items:

* The `operationId` for this endpoint is `status`, which is not descriptive. Could it be renamed (e.g. `setPassthru`)?
* Please add descriptions for `component`, `payload`, and the `response` field.

This will make the OpenAPI specification clearer and avoid confusion for API users.
