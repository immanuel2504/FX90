# `get_appled` / `set_appled` — schema clarification (scenario)

**Commands:** `get_appled`, `set_appled`  
**REST endpoints:** `GET /cloud/app-led`, `PUT /cloud/app-led`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_appled` and `set_appled` commands for `/cloud/app-led` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/app-led`, the example request is:

```json
{
  "color": "amber",
  "flash": true,
  "seconds": 60
}
```

But the schema defines `color` only as:

```yaml
color:
  type: string
```

Since there is no `enum`, Swagger treats this as any string value. For example, `"amber"`, `"purple"`, or `"abc"` would all be valid according to the schema.

The related `set_stackled` command already restricts `color` with:

```yaml
enum: [red, amber, green, blue, off]
```

Could you please confirm the intended values for `set_appled.color` and, if fixed, add the same `enum`?

The GET response has the same issue — `status` returns `"DEFAULT"` but the schema is only `type: string`:

```json
{
  "status": "DEFAULT"
}
```

If the valid values are fixed (for example `DEFAULT`, `NON_DEFAULT`), please add an `enum`.

Also, please add:

* descriptions for `color`, `flash`, `seconds` (including the unit for `seconds`)
* a description for the `PUT /cloud/app-led` response, because it currently returns an empty string and the schema does not explain it

This will make the OpenAPI specification clearer and avoid confusion for API users.
