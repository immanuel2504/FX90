# `set_mode` — schema clarification (scenario)

**Commands:** `get_mode`, `set_mode`  
**REST endpoints:** `GET /cloud/mode`, `PUT /cloud/mode`  
**Reference:** `openAPISpec.yaml` (compared against `Command Schemas.json`)  

Hi,

I reviewed the `set_mode` command for `/cloud/mode` and compared `openAPISpec.yaml` against `Command Schemas.json`.

I need clarification using this scenario:

When I call `PUT /cloud/mode`, the example request includes:

```json
{
  "type": "CUSTOM",
  "antennas": [1, 2, 3, 4],
  "query": { "sel": "ALL", "session": "S1", "target": "A" }
}
```

In `openAPISpec.yaml`, `type` is defined only as:

```yaml
type:
  type: string
```

So `"type": "CUSTOM"`, `"type": "abc"`, or `"type": "test"` would all be valid. But `Command Schemas.json` restricts it:

```yaml
type:
  enum: [SIMPLE, INVENTORY, PORTAL, CONVEYOR, CUSTOM, DIRECTIONALITY]
  default: SIMPLE
```

Please add the same `enum`/`default` to `openAPISpec.yaml`.

Two more items found while comparing with `Command Schemas.json`:

1. **Missing `environment` field** — `Command Schemas.json` defines `environment` with `enum: [LOW_INTERFERENCE, HIGH_INTERFERENCE, VERY_HIGH_INTERFERENCE, AUTO_DETECT, DEMO]` (default `HIGH_INTERFERENCE`), but it is absent from `openAPISpec.yaml`. Is it supported over REST?

2. **Missing enums/descriptions** — `query.sel`, `query.session`, `query.target`, `reportFilter.type`, and `antennaStopCondition.type` are free-form strings in `openAPISpec.yaml`, while `Command Schemas.json` documents them with descriptions and cross-field constraints. Please align.

This will make the OpenAPI specification clearer and avoid confusion for API users.
