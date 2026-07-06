# `set_mode` — OpenAPI schema feedback

**Commands:** `get_mode`, `set_mode`  
**REST endpoints:** `GET /cloud/mode`, `PUT /cloud/mode`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `set_mode` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `set_mode` command and compared `openAPISpec.yaml` with the MQTT `set_mode` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The MQTT schema in the IoTC documentation is much richer; `openAPISpec.yaml` is missing several constraints.

---

## 1. `type` has no `enum`

- In `openAPISpec.yaml`, `type` is `type: string` with example `CUSTOM`, but there is no `enum`.
- The MQTT command in the Zebra IoTC documentation defines `type` with `enum: [SIMPLE, INVENTORY, PORTAL, CONVEYOR, CUSTOM, DIRECTIONALITY]` and `default: SIMPLE`. Please add the same `enum`/`default`.

---

## 2. `environment` field is missing entirely

- The MQTT command in the Zebra IoTC documentation defines an `environment` field with `enum: [LOW_INTERFERENCE, HIGH_INTERFERENCE, VERY_HIGH_INTERFERENCE, AUTO_DETECT, DEMO]` (`default: HIGH_INTERFERENCE`) and a detailed description.
- This field is absent from `openAPISpec.yaml`. If it is supported over REST, please add it.

---

## 3. Missing `enum`s / descriptions on nested fields

- `query.sel`, `query.session`, `query.target`, `reportFilter.type`, and `antennaStopCondition.type` are plain `type: string` with examples but no `enum` or descriptions in `openAPISpec.yaml`.
- `inventoryProtocol.mode` already has an `enum` (`GEN2X`, `GEN2`, `HYBRID`) — thank you.
- The MQTT command in the Zebra IoTC documentation has descriptions and cross-field constraints (e.g. `antennas` vs `beams`, `transmitPower` array length must match `antennas`). Please align.

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

The MQTT command in the Zebra IoTC documentation already defines most of these (via `$ref`s such as `select.v1`, `query.v1`, `inventorysettings.v1`, `antennaStopCondition.v1`) with descriptions and examples — please port them to `openAPISpec.yaml`.

---

## 5. Visual comparison of the two schemas

Legend: `✅` = present · `❌ MISSING` = absent · `[…]` = allowed enum values.

### 5.1 MQTT reference — Zebra IoTC documentation (MQTT `set_mode` command) → `operatingMode.v1` (complete)

```text
MQTT set_mode command (Zebra IoTC documentation)
        │
        ▼
operatingMode.v1
│
├── type*                           ✅ enum + default
├── environment                     ✅ enum + default
├── antennas                        ✅ array
├── filter                          ✅ tagidfilter.v1
├── transmitPower                   ✅ number | array<number>
├── antennaStopCondition            ✅ object | array
│   ├── type                        ✅ enum
│   └── value
├── query                           ✅ object | array
│   ├── tagPopulation
│   ├── sel                         ✅ enum
│   ├── session                     ✅ enum
│   └── target                      ✅ enum
├── selects                         ✅ select.v1
│   ├── target                      ✅ enum
│   ├── action                      ✅ enum
│   ├── membank                     ✅ enum
│   ├── pointer
│   ├── length
│   ├── mask
│   └── truncate
├── delayAfterSelects
├── accesses                        ✅ access_cmds.v1
├── delayBetweenAntennaCycles
├── tagMetaData
│   ├── string values               ✅ enum
│   └── object forms                ✅ supported
├── radioStartConditions
│   ├── type                        ✅ enum
│   └── gpis
├── radioStopConditions
│   ├── duration
│   ├── antennaCycles
│   ├── tagCount
│   ├── durationAfterNoMoreUniqueTags
│   └── gpis
├── reportFilter
│   ├── duration
│   └── type                        ✅ enum
├── rssiFilter
├── modeSpecificSettings
│   ├── Inventory Settings
│   ├── Portal Settings
│   └── Directionality Settings
└── beams
    ├── azimuth
    ├── elevation
    └── polarization                ✅ enum
```

### 5.2 REST as currently written — `openAPISpec.yaml` → `PUT /cloud/mode` request body (incomplete)

```text
openAPISpec.yaml
        │
        ▼
PUT /cloud/mode  (inline request schema)          required: ❌ MISSING (MQTT requires "type")
│
├── type                            ❌ enum MISSING [SIMPLE, INVENTORY, PORTAL, CONVEYOR, CUSTOM, DIRECTIONALITY]   ❌ description MISSING
├── antennas                        ✅ array<number>                     ❌ description MISSING
├── antennaStopCondition            ⚠️ object ONLY (array form ❌ MISSING)
│   ├── type                        ❌ enum MISSING [DURATION, INVENTORY_COUNT, GPI, SINGLE_INVENTORY_LIMITED_DURATION]   ❌ description MISSING
│   └── value                       ❌ description MISSING
├── query                           ⚠️ object ONLY (array form ❌ MISSING)
│   ├── tagPopulation               ❌ description MISSING
│   ├── sel                         ❌ enum MISSING [ALL, SL, NOT_SL]        ❌ description MISSING
│   ├── session                     ❌ enum MISSING [S0, S1, S2, S3]         ❌ description MISSING
│   └── target                      ❌ enum MISSING [A, B, AB]               ❌ description MISSING
├── inventoryProtocol               ➕ EXTRA (not in MQTT operatingMode)
│   └── mode                        ✅ enum [GEN2X, GEN2, HYBRID]           ❌ description MISSING
├── reportFilter
│   ├── duration                    ❌ description MISSING
│   └── type                        ❌ enum MISSING [RADIO_WIDE, PER_ANTENNA]   ❌ description MISSING
├── tagMetaData                     ⚠️ array<string> only
│   ├── string values               ❌ enum MISSING (allowed values not listed)
│   └── object forms                ❌ MISSING (userDefined / antennaPortNames)
├── transmitPower                   ⚠️ array<number> ONLY (single-number form ❌ MISSING)   ❌ description MISSING
├── delayBetweenAntennaCycles       ❌ description MISSING
├── component                       ➕ EXTRA (not in MQTT)                ❌ description MISSING
├── payload                         ➕ EXTRA (not in MQTT)                ❌ description MISSING
└── linkProfile                     ➕ EXTRA (not in MQTT)                ❌ description MISSING

   Defined in MQTT but NOT present as REST properties (they only appear inside examples):
      environment ❌   selects ❌   accesses ❌   radioStartConditions ❌
      radioStopConditions ❌   modeSpecificSettings ❌   filter ❌
      delayAfterSelects ❌   rssiFilter ❌   beams ❌
```

---

## 6. What is missing and what is extra (summary)

### 6.1 Missing entirely from REST (defined in MQTT, not defined as REST properties)

| Field | In MQTT | In REST |
|-------|---------|---------|
| `environment` | ✅ enum + desc | ❌ only in examples |
| `selects` | ✅ `select.v1` | ❌ only in examples |
| `accesses` | ✅ `access_cmds.v1` | ❌ only in examples |
| `radioStartConditions` | ✅ | ❌ only in examples |
| `radioStopConditions` | ✅ | ❌ only in examples |
| `modeSpecificSettings` | ✅ oneOf | ❌ only in examples |
| `filter` | ✅ `tagidfilter.v1` | ❌ absent |
| `delayAfterSelects` | ✅ | ❌ absent |
| `rssiFilter` | ✅ | ❌ absent |
| `beams` | ✅ | ❌ absent |
| `required: [type]` | ✅ | ❌ no `required` list |

### 6.2 Present in both, but incomplete in REST

| Field | Missing in REST |
|-------|-----------------|
| `type` | enum ❌, description ❌ |
| `antennas` | description ❌ |
| `antennaStopCondition` | array form ❌, `type` enum ❌, descriptions ❌ |
| `query` | array form ❌; `sel`/`session`/`target` enums ❌; descriptions ❌ |
| `reportFilter` | `type` enum ❌, descriptions ❌ |
| `tagMetaData` | enum values ❌, object forms ❌, description ❌ |
| `transmitPower` | single-number form ❌, description ❌ |
| `delayBetweenAntennaCycles` | descriptions ❌ |

### 6.3 Extra in REST (not in the MQTT `operatingMode` schema)

| Field | Notes |
|-------|-------|
| `component` (string) | Stray — no equivalent in MQTT payload. Please confirm or remove. |
| `payload` (string) | Stray — no equivalent in MQTT payload. Please confirm or remove. |
| `linkProfile` (number) | Stray — not in MQTT `operatingMode` schema. Please confirm or remove. |
| `inventoryProtocol` (`mode` enum) | REST-only field with an enum but no description and no MQTT counterpart. Please confirm and add a description. |

---

## Note

The MQTT `set_mode` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal is the complete reference. This is a request to bring `openAPISpec.yaml` in line with it (enums, `environment`, the complex fields above, and rich examples).

**Shortcut:** `openAPISpec.yaml` already contains a complete `operatingMode.v1` component (mirrors the MQTT schema above). The `PUT /cloud/mode` endpoint currently uses a hand-written inline schema instead. Pointing the endpoint's `requestBody` at `#/components/schemas/operatingMode.v1` (and removing the stray `component` / `payload` / `linkProfile` fields) would resolve nearly all of the gaps above in one change.
