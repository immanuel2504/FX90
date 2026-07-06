# `get_gpiStatus` — schema clarification (scenario)

**Command:** `get_gpiStatus`  
**REST endpoint:** `GET /cloud/gpi`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_gpiStatus` command for `/cloud/gpi` in `openAPISpec.yaml`.

When I call `GET /cloud/gpi`, the example response is:

```json
{
  "1": "HIGH",
  "2": "LOW",
  "3": "HIGH",
  "4": "LOW"
}
```

The schema already constrains each port with `enum: [HIGH, LOW]` — thank you, that is correct. Two smaller items are missing compared with the MQTT `get_gpiStatus` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal:

* the per-port fields have **no descriptions** (the Zebra IoTC MQTT documentation has e.g. "State of GPI port 1. Allowed values: HIGH, LOW.")
* there is **no `required` list**, whereas the Zebra IoTC MQTT documentation marks ports `1` and `2` as `required`.

Could you please add the per-port descriptions and confirm whether ports `1` and `2` should be `required` on FXR90?
