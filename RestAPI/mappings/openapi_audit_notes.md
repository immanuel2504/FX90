# REST API OpenAPI — Audit Notes

**Project:** FXR90 IoT Connector REST API  
**Spec files:** `RestAPI/FXR90.yaml`, `RestAPI/openapi.yaml`, `RestAPI/FXR90-rest-api.yaml`  
**Viewer:** `RestAPI/swagger.html` → loads `FXR90-rest-api.yaml`  
**Build script:** `RestAPI/scripts/build_openapi.py`  
**Last updated:** 2026-07-05  

This document records what was reviewed, what was changed, and what remains open — for handoff if someone asks why the spec looks a certain way or what was cleaned up.

---

## 1. Operation ID fix (completed)

### Problem

13 REST operations had **no `operationId`** in the path YAML files. The build script (`build_openapi.py`) falls back to keys like `GET__cloud__gpo` (HTTP method + path) to match markdown files in `RestAPI/operation_descriptions/`.

That produced:

- Awkward Swagger UI operation IDs
- Inconsistent naming vs the other 55 operations (camelCase `operationId`s)
- Markdown files named `GET__cloud__gpo.md`, `PUT__cloud__preSelection.md`, etc.

### What we did

Added proper `operationId` values to path files and `FXR90.yaml`, renamed matching markdown files, and updated `rest_mqtt_map.json`.

| Path | Method | New `operationId` |
|------|--------|-------------------|
| `/cloud/gpo` | GET | `getGpoStatus` |
| `/cloud/eSimConfig` | GET | `getEsimConfig` |
| `/cloud/ntpServer` | GET | `getNtpServer` |
| `/cloud/preSelection` | GET | `getPreSelection` |
| `/cloud/preSelection` | PUT | `setPreSelection` |
| `/cloud/updatePassword` | PUT | `updatePassword` |
| `/cloud/logs/syslog` | GET | `getLogsSyslog` |
| `/cloud/logs/syslog` | DELETE | `delLogsSyslog` |
| `/cloud/logs/RcLog` | GET | `getRcLog` |
| `/cloud/logs/RgErrorLog` | GET | `getRgErrorLog` |
| `/cloud/logs/RgWarningLog` | GET | `getRgWarningLog` |
| `/cloud/logs/radioPacketLog` | GET | `getRadioPacketLog` |
| `/cloud/logs/radioPacketLog` | DELETE | `delRadioPacketLog` |

### Markdown renames (examples)

| Old filename | New filename |
|--------------|--------------|
| `GET__cloud__gpo.md` | `getGpoStatus.md` |
| `PUT__cloud__preSelection.md` | `setPreSelection.md` |
| `GET__cloud__logs__syslog.md` | `getLogsSyslog.md` |

### Result after rebuild

```
Total operations: 68
With operationId: 68
Missing operationId: 0
REST op docs: 68 file(s), 68 operation(s) updated
openapi-spec-validator: VALID
```

### How operation IDs map to docs

`build_openapi.py` uses this logic:

1. If the operation has `operationId` → look for `operation_descriptions/{operationId}.md`
2. Otherwise → fallback key `{METHOD}__{path with slashes as __}` (e.g. `GET__cloud__gpo`)

All operations now use option 1.

---

## 2. Schemas section review (Swagger UI)

### What Swagger shows

Swagger UI lists **every** entry under `components/schemas`. The spec declares **151 schemas**. Many at the **top** of the list are legacy Zebra domain models (`*.v1`) from the original Stoplight export — not the flat per-operation Request/Response types that most endpoints use.

### Architecture issue (not yet fixed)

There are effectively **two schema layers**:

| Layer | Count | Source | Used by endpoints? |
|-------|------:|--------|-------------------|
| Domain models (`*.v1`, aliases) | ~68 in `FXR90.yaml` | Original Zebra/Stoplight export | Mostly **no** |
| Operation Request/Response | ~83 extra in `openapi.yaml` | Accumulated via build merge | **Yes** |

`build_openapi.py` merges schemas from `FXR90.yaml` with any existing schemas in `openapi.yaml`, so operation-specific types persist even when they are not defined in `FXR90.yaml`.

Paths under `RestAPI/paths/` reference operation schemas like `getConfigResponse`, `setGpoRequest` — not domain types like `readerversion.v1` or `readernetwork.v1`.

### Naming inconsistencies (still open)

Three conventions coexist:

- **camelCase operation schemas:** `getGPIStatusResponse`, `setGpoRequest`
- **snake_case / MQTT-style:** `get_gpoResponse`, `get_logs_syslogResponse`
- **HTTP verb prefix:** `put_preSelectionRequest`, `put_updatePasswordRequest`

Auto-generated error schema names also exist, e.g. `setImpinjGen2XResponseschema_422`.

---

## 3. Unused schemas (not removed — documented only)

### How “unused” was defined

Start from all **68 path operations**, follow every `#/components/schemas/...` reference (including nested refs inside other schemas). Any declared schema never reached = **unused by endpoints**.

### Summary

| Metric | Count |
|--------|------:|
| Total declared schemas | 151 |
| Reachable from endpoints | 117 |
| **Not used by any endpoint** | **34** |

Machine-readable list: `RestAPI/mappings/unused_schemas.txt`

### Full list — 34 unused schemas

#### Alias-only wrappers (3)

These only `$ref` another schema; no path points at the alias name.

- `operatingModes` → `operatingMode.v1`
- `gpioLedConfig` → `GPIOLEDConfig.v1`
- `mgmtEventConfig` → `eventsConfig.v1`

#### Domain `*.v1` models (14)

Legacy component types not wired to REST paths (endpoints use flat `*Response` schemas instead).

- `cpustats.v1`
- `error.v1`
- `logLevel.v1`
- `memorystats.v1`
- `networkconfig.v1`
- `ntpstats.v1`
- `os_update.v1`
- `osversions.v1`
- `readerflashmemory.v1`
- `readernetwork.v1`
- `readerstats.v1`
- `readerupgradestatus.v1`
- `readerversion.v1`
- `regionconfig.v1`

#### Stoplight / legacy duplicates (17)

Alternate names superseded by operation schemas actually referenced from `paths/`.

- `SupportedRegionList`
- `SupportedRegionStandard_command`
- `SupportedStandardList_response`
- `batching`
- `getCableLossCompensation`
- `getNTPServer`
- `getNameAndDescription`
- `getReaderCapabilities`
- `getTimeZone`
- `getmodePayload`
- `getmodepayload`
- `readerConfig`
- `retention`
- `setCableLossCompensation`
- `setNTPServer`
- `setNameAndDescription`
- `setTimeZone`

### Important

- All **85 operation-style** Request/Response schemas **are used** — they are not the clutter problem.
- The **34 listed above were removed on 2026-07-05** from `FXR90.yaml`, `openapi.yaml`, and the bundled spec.
- Swagger UI Schemas section now shows **117 schemas** (down from 151).
- Plain list kept for reference: `RestAPI/mappings/unused_schemas.txt`

---

## 4. Other schema quality notes (open)

- **`error.v1`** exists but endpoints use duplicated inline error objects instead.
- **`operatingMode.v1`** is one of the few domain models actually used (`GET/PUT /cloud/mode`).
- Some schemas are empty or minimal (`setRevertbackosRequest`, many `type: string` success responses).
- Examples occasionally wrong type (`dhcp` boolean with example `'true'` string).
- `FXR90.yaml` still contains full inline `paths:` definitions (~lines 13–7439) that the build **does not use**; editable source is `RestAPI/paths/`.

---

## 5. How to rebuild after edits

```powershell
python RestAPI/scripts/build_openapi.py
```

Then open `RestAPI/swagger.html` in a browser (serves `FXR90-rest-api.yaml`).

**Edit these (source):**

- `RestAPI/paths/` — path/operation definitions
- `RestAPI/operation_descriptions/` — per-operation markdown
- `RestAPI/FXR90.yaml` — monolith metadata + domain schemas
- `RestAPI/tag_config.json` — N/A for REST (MQTT only)

**Do not hand-edit (generated):**

- `RestAPI/openapi.yaml`
- `RestAPI/FXR90-rest-api.yaml`

---

## 6. Suggested next steps (optional)

1. ~~Remove or hide the **34 unused schemas** to shorten Swagger UI.~~ **Done (2026-07-05)**
2. Normalize snake_case operation schema names (`get_gpoResponse` → `getGpoStatusResponse`, etc.).
3. Point endpoints at domain `*.v1` models where they match (`getVersionResponse` → `readerversion.v1`).
4. Reuse `error.v1` for all error responses instead of `*Responseschema_*` duplicates.
5. Trim redundant inline `paths:` block in `FXR90.yaml` if `paths/` remains the source of truth.

---

## 7. Related files

| File | Purpose |
|------|---------|
| `RestAPI/mappings/openapi_audit_notes.md` | This document |
| `RestAPI/mappings/unused_schemas.txt` | Plain list of 34 unused schema names |
| `RestAPI/mappings/rest_mqtt_map.json` | REST ↔ MQTT mapping (includes `operationId`) |
| `RestAPI/scripts/build_openapi.py` | Spec generator |

---

## 8. OpenAPI 3.0 normalization (2026-07-05)

Swagger UI validates against **OpenAPI 3.0**, but the Zebra export used **3.1 / JSON Schema 2020** features. Fixed inside `build_openapi.py`:

- down-converts schema constructs to OpenAPI 3.0
- flattens nested inline schemas into named `$ref` components
- emits `openapi: 3.0.3` in `FXR90-rest-api.yaml`
- `DELETE /cloud/certificates/{certname}` — body moved to query param `type` (OAS 3.0 rule)

Rebuild after schema edits:

```powershell
python RestAPI/scripts/build_openapi.py
```

That single script also normalizes OpenAPI 3.0 constructs and flattens nested schemas for Swagger UI.

Use **`FXR90-rest-api.yaml`** in Swagger UI (`swagger.html`).

> We fixed all 13 missing REST `operationId`s and aligned markdown docs; audited the OpenAPI schema registry and **removed 34 unused schemas** (legacy domain models and Stoplight duplicates), reducing Swagger UI from 151 to **117 schemas**.
