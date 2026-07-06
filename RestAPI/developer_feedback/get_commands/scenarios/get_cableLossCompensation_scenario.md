# `get_cableLossCompensation` — schema clarification (scenario)

**Command:** `get_cableLossCompensation`  
**REST endpoint:** `GET /cloud/cableLossCompensation`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_cableLossCompensation` command for `/cloud/cableLossCompensation` in `openAPISpec.yaml`.

When I call `GET /cloud/cableLossCompensation`, the example response is:

```json
{
  "1": { "cableLength": 10, "cableLossPerHundredFt": 10 },
  "2": { "cableLength": 10, "cableLossPerHundredFt": 10 }
}
```

The schema defines the numbered blocks and their two numeric fields, but with no descriptions and no bounds:

```yaml
'1':
  type: object
  properties:
    cableLength: { type: number }
    cableLossPerHundredFt: { type: number }
```

Compared with the MQTT `get_cableLossCompensation` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal:

* the numbered keys (`1`–`4`) are **not explained** as read-point/antenna port numbers,
* `cableLength` / `cableLossPerHundredFt` have **no descriptions** and no `minimum: 0` (both are non-negative in the Zebra IoTC MQTT documentation),
* there is **no `required` list**, whereas the Zebra IoTC MQTT documentation marks the read points and both inner fields as `required`.

Could you please add descriptions (including what the numbered keys represent and the units), the `minimum: 0` constraint, and the `required` list? (Not applicable to ATR7000 readers.)
