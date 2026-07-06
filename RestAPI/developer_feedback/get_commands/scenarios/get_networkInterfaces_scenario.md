# `get_networkInterfaces` — schema clarification (scenario)

**Command:** `get_networkInterfaces`  
**REST endpoint:** `GET /cloud/networkInterfaces`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_networkInterfaces` command for `/cloud/networkInterfaces` in `openAPISpec.yaml`.

When I call `GET /cloud/networkInterfaces`, the example response is:

```json
{
  "availableNetworkInterfaces": ["eth0", "mlan0", "bnep0", "wan0"]
}
```

The schema types this correctly as an array of strings:

```yaml
availableNetworkInterfaces:
  type: array
  items:
    type: string
```

Compared with the MQTT `get_networkInterfaces` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal, the only missing items are a **description** for `availableNetworkInterfaces` ("Available network interface names reported by the reader") and the **`required` list** (the Zebra IoTC MQTT documentation marks it `required`).

Could you please add the field description (and confirm whether it should be `required`)?
