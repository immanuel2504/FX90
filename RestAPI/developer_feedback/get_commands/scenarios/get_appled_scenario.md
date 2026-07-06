# `get_appled` — schema clarification (scenario)

**Command:** `get_appled`  
**REST endpoint:** `GET /cloud/app-led`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_appled` command for `/cloud/app-led` in `openAPISpec.yaml`.

When I call `GET /cloud/app-led`, the example response is:

```json
{
  "status": "DEFAULT"
}
```

But the schema defines `status` only as:

```yaml
type: string
```

Since there is no `enum`, Swagger treats this as any string value — `"DEFAULT"`, `"NOT_DEFAULT"`, `"abc"` would all be valid.

The MQTT `get_appled` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal constrains `status` to fixed values:

```yaml
enum:
  - DEFAULT
  - NOT_DEFAULT
default: DEFAULT
```

Could you please add this `enum` (and a description for `status`) to the GET response schema so callers know the only two valid states?
