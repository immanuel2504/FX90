# `set_cableLossCompensation` — schema clarification (scenario)

**Commands:** `get_cableLossCompensation`, `set_cableLossCompensation`  
**REST endpoints:** `GET /cloud/cableLossCompensation`, `PUT /cloud/cableLossCompensation`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_cableLossCompensation` command for `/cloud/cableLossCompensation` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/cableLossCompensation`, the example request is:

```json
{
  "1": { "cableLength": 90, "cableLossPerHundredFt": 18 },
  "2": { "cableLength": 18, "cableLossPerHundredFt": 19 }
}
```

Two things are unclear from the schema:

1. **Numbered keys** — the object keys `1`, `2`, `3`, `4` have no description. I assume they map to antenna ports, but the schema does not say so, nor how many are valid per device type. Could a description be added?

2. **Units and range** — `cableLength` and `cableLossPerHundredFt` are defined only as:

```yaml
cableLength:
  type: number
cableLossPerHundredFt:
  type: number
```

Since there is no unit or range, `cableLength: 90` could be feet, meters, or anything. Could you add descriptions with the unit of measure (e.g. feet, dB per 100 ft) and any valid range?

Also, please add a description for the `200` response, which currently returns an empty string.

This will make the OpenAPI specification clearer and avoid confusion for API users.
