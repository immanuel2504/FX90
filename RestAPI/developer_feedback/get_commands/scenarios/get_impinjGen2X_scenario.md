# `get_impinjGen2X` — schema clarification (scenario)

**Command:** `get_impinjGen2X`  
**REST endpoint:** `GET /cloud/impinjGen2X`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_impinjGen2X` command for `/cloud/impinjGen2X` in `openAPISpec.yaml`.

When I call `GET /cloud/impinjGen2X`, one of the documented examples (`fastID_configured`) returns:

```json
{
  "fastID": {
    "enabled": true,
    "tidSelector": "TID[0]"
  }
}
```

But the `fastID` object in the schema defines only `enabled`:

```yaml
fastID:
  type: object
  properties:
    enabled:
      type: boolean
  required:
    - enabled
```

So `tidSelector` is returned in the example (and defined by the MQTT `get_impinjGen2X` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal) but is **not declared as a property**. In the Zebra IoTC MQTT documentation it is:

```yaml
tidSelector:
  type: string
  enum: [TID[0], TID[1], TID[2], TID[3]]
```

Could you please add `tidSelector` to the `fastID` object (with this `enum` and a description)? The `PUT /cloud/impinjGen2X` request already defines `fastID.tidSelector`, so this simply aligns the GET response with it. The rest of the `get_impinjGen2X` response schema already looks good.
