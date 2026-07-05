# `get_preSelection` / `set_preSelection` — schema clarification (scenario)

**Commands:** `get_preSelection`, `set_preSelection`  
**REST endpoints:** `GET /cloud/preSelection`, `PUT /cloud/preSelection`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_preSelection` and `set_preSelection` commands for `/cloud/preSelection` in `openAPISpec.yaml`.

I need one clarification using this scenario:

When I call `GET /cloud/preSelection`, the example response is:

```json
{
  "preSelection": "disabled"
}
```

But the schema defines `preSelection` only as:

```yaml
type: string
```

Since there is no `enum`, Swagger treats this as any string value. For example, values like `"disabled"`, `"enabled"`, `"abc"`, or `"test"` would all be valid according to the schema.

Could you please confirm the intended values?

If only fixed values are valid, such as:

```yaml
enum:
  - enabled
  - disabled
```

then please add the enum to the GET response schema.

Also, please add:

* a description for the `preSelection` field
* a description for the `PUT /cloud/preSelection` response, because it currently returns an empty string and the schema does not explain it

This will make the OpenAPI specification clearer and avoid confusion for API users.
