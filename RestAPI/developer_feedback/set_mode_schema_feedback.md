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

## Note

The MQTT `set_mode` schema in `Command Schemas.json` is the complete reference. This is a request to bring `openAPISpec.yaml` in line with it (enums, `environment`, descriptions).
