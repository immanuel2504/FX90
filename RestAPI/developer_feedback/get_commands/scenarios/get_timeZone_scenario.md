# `get_timeZone` — schema clarification (scenario)

**Command:** `get_timeZone`  
**REST endpoint:** `GET /cloud/timeZone`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_timeZone` command for `/cloud/timeZone` in `openAPISpec.yaml`.

When I call `GET /cloud/timeZone`, the example response is:

```json
{
  "timeZone": "UTC"
}
```

But the schema defines `timeZone` only as:

```yaml
timeZone:
  type: string
  example: "UTC"
```

Since there is no `enum`, any string is valid. The MQTT `get_timeZone` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal constrains `timeZone` to a fixed list of allowed zones (e.g. `Coordinated Universal Time`, `Pacific Time (US & Canada)`, `Chennai, Kolkata, Mumbai, New Delhi`, and `(GMT±hh:mm) …` variants).

Note that the example value `"UTC"` is **not** one of the allowed values in that list (the closest are `Coordinated Universal Time` / `(UTC) Coordinated Universal Time`).

Could you please add the `enum` to the GET response schema, update the example to a valid value, and add a description for `timeZone`?
