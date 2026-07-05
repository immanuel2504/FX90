# `set_mode` — OpenAPI schema feedback

**Commands:** `get_mode`, `set_mode`  
**REST endpoints:** `GET /cloud/mode`, `PUT /cloud/mode`  
**Reference:** `openAPISpec.yaml` (compared against `Command Schemas.json`)  

Hi,

I reviewed the `set_mode` command and compared `openAPISpec.yaml` with `Command Schemas.json`. The MQTT schema in `Command Schemas.json` is much richer; `openAPISpec.yaml` is missing several constraints.

---

## 1. `type` has no `enum`

- In `openAPISpec.yaml`, `type` is `type: string` with example `CUSTOM`, but there is no `enum`.
- `Command Schemas.json` defines `type` with `enum: [SIMPLE, INVENTORY, PORTAL, CONVEYOR, CUSTOM, DIRECTIONALITY]` and `default: SIMPLE`. Please add the same `enum`/`default`.

---

## 2. `environment` field is missing entirely

- `Command Schemas.json` defines an `environment` field with `enum: [LOW_INTERFERENCE, HIGH_INTERFERENCE, VERY_HIGH_INTERFERENCE, AUTO_DETECT, DEMO]` (`default: HIGH_INTERFERENCE`) and a detailed description.
- This field is absent from `openAPISpec.yaml`. If it is supported over REST, please add it.

---

## 3. Missing `enum`s / descriptions on nested fields

- `query.sel`, `query.session`, `query.target`, `reportFilter.type`, and `antennaStopCondition.type` are plain `type: string` with examples but no `enum` or descriptions in `openAPISpec.yaml`.
- `inventoryProtocol.mode` already has an `enum` (`GEN2X`, `GEN2`, `HYBRID`) — thank you.
- `Command Schemas.json` has descriptions and cross-field constraints (e.g. `antennas` vs `beams`, `transmitPower` array length must match `antennas`). Please align.

---

## 4. Complex fields need full schema definitions and examples

Several important `set_mode` fields appear only in the request **examples** (or are missing entirely) and are **not defined as schema properties** in `openAPISpec.yaml`. Because they are complex/nested, please add proper schema definitions **and** worked examples for each:

| Field | Status in `openAPISpec.yaml` | Request |
|-------|------------------------------|---------|
| `selects` | Used in examples only; no schema property | Add schema (Gen2 select params) + examples |
| `accesses` | Not present | Add schema (access operations: read/write/lock/kill) + examples |
| `tagMetaData` | Defined as `array` of `string` only | Add allowed values + object forms (e.g. `userDefined`, `antennaPortNames`) with examples |
| `radioStartConditions` | Used in examples only; no schema property | Add schema + examples |
| `radioStopConditions` | Used in examples only; no schema property | Add schema + examples |
| `reportFilter` | `duration`/`type` only, no `enum`/description | Add `type` enum + description + examples |
| `modeSpecificSettings` | Used in examples only; no schema property | Add schema (`oneOf` inventory/portal/directionality) + examples |
| `antennaStopCondition` | Object only (examples also show array form) | Support both object and array forms + examples |
| `query` | Object only (examples also show array form) | Support both forms; add `sel`/`session`/`target` enums + examples |

`Command Schemas.json` already defines most of these (via `$ref`s such as `select.v1`, `query.v1`, `inventorysettings.v1`, `antennaStopCondition.v1`) with descriptions and examples — please port them to `openAPISpec.yaml`.

---

## Note

The MQTT `set_mode` schema in `Command Schemas.json` is the complete reference. This is a request to bring `openAPISpec.yaml` in line with it (enums, `environment`, the complex fields above, and rich examples).
