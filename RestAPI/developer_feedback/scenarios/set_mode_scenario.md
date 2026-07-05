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

3. **Complex fields lack schema definitions and examples** — several fields appear only in the request examples (or not at all) and have no schema property in `openAPISpec.yaml`. For example, a real `set_mode` request may include:

```json
{
  "type": "CUSTOM",
  "antennas": [1],
  "selects": [
    { "target": "S1", "action": "INVB_NOTHING", "membank": "TID", "pointer": 6, "length": 24, "mask": "800600" }
  ],
  "tagMetaData": ["RSSI", "ANTENNA", { "antennaPortNames": ["East", "West"] }],
  "reportFilter": { "duration": 0, "type": "PER_ANTENNA" },
  "radioStartConditions": {},
  "radioStopConditions": {},
  "modeSpecificSettings": { "interval": { "unit": "seconds", "value": 0 } }
}
```

But `selects`, `accesses`, `radioStartConditions`, `radioStopConditions`, and `modeSpecificSettings` are **not defined as schema properties**, and `tagMetaData` is only `array<string>` (it also accepts object forms). Please add full schema definitions **and worked examples** for:

- `selects` (Gen2 select params)
- `accesses` (access operations: read/write/lock/kill)
- `tagMetaData` (allowed string values + object forms like `userDefined`, `antennaPortNames`)
- `radioStartConditions`, `radioStopConditions`
- `reportFilter` (`type` enum)
- `modeSpecificSettings` (`oneOf` inventory/portal/directionality)

`Command Schemas.json` already defines most of these (via `$ref`s such as `select.v1`, `query.v1`, `inventorysettings.v1`) — please port them to `openAPISpec.yaml`.

This will make the OpenAPI specification clearer and avoid confusion for API users.
