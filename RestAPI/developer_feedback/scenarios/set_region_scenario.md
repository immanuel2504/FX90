# `set_region` — schema clarification (scenario)

**Commands:** `get_region`, `set_region`  
**REST endpoints:** `GET /cloud/region`, `PUT /cloud/region`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_region` command for `/cloud/region` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/region`, the example request is:

```json
{
  "country": "Canada",
  "standardname": "CANADA_FCC_15"
}
```

But `country` and `standardname` are defined only as:

```yaml
country:
  type: string
standardname:
  type: string
```

Since there is no `enum`, Swagger treats these as any string value. For example, `"standardname": "CANADA_FCC_15"`, `"standardname": "abc"`, or `"country": "test"` would all be valid according to the schema.

In practice the valid values appear to come from `get_SupportedRegionList` (for `country`) and `get_SupportedStandardList` (for `standardname`).

Could you please confirm:

* whether these should be constrained with an `enum`, or
* documented as validated at runtime against `get_SupportedRegionList` / `get_SupportedStandardList`

Also, please add:

* descriptions for `country` and `standardname`
* a description for the `PUT /cloud/region` response, because it currently returns an empty string and the schema does not explain it

This will make the OpenAPI specification clearer and avoid confusion for API users.
