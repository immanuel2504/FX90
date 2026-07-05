The `PUT /cloud/impinjGen2X` REST endpoint configures Impinj Gen2X proprietary RFID features on the FXR90 reader, covering FastID acceleration, TagProtect security, TagFocus singulation control, and TagQuieting (basic and advanced) behavior.

**This endpoint allows you to configure:**

- FastID for combined EPC + TID reads in a single inventory operation
- TagProtect for password-based tag protection and visibility control
- TagFocus to suppress already-read tags during dense inventory
- TagQuieting (basic or advanced) to silence specific tags by EPC or by Gen2 select masks

### Endpoint Details

| Property | Value |
|---|---|
| Pattern Name | Impinj Gen2X Configuration Update |
| Communication Type | Client to Device (HTTP request/response) |
| Applies To | FXR90 Series |
| REST Endpoint | `PUT /cloud/impinjGen2X` |
| Related Endpoints | `GET /cloud/impinjGen2X`, `PUT /cloud/start`, `PUT /cloud/stop` |
| Authentication | Bearer token (`Authorization: Bearer <token>`) |
| Content-Type | `application/json` |
| Success Response | `200 OK` |
| Error Responses | `422 Unprocessable Entity`, `500 Internal Server Error` |
| Supported Features | FastID, TagProtect, TagFocus, TagQuieting (basic and advanced) |
| Supported TagProtect Actions | `enableTagProtection`, `disableTagProtection`, `enableTagVisibility`, `disableTagVisibility` |
| Supported TagQuieting Basic Actions | `quiet`, `unquiet` |
| Supported Gen2 Memory Banks | EPC, TID, USER, RESERVED |
| Supported Select Targets | S0, S1, S2, S3, SL |
| Supported Tag Quiet Masks | S0A, S0B, S1A, S1B, S2A, S2B, S3A, S3B, SL_ASSERT, SL_DEASSERT |
| Mutually Exclusive Features | FastID, TagFocus, TagQuieting (only one reader-scoped feature active at a time) |

---

## 2. Before You Begin

Decide which Gen2X feature you need to configure before sending this request. You can send a minimal payload targeting only one feature (for example, only `fastID` or only `tagProtect`), but you cannot combine mutually exclusive reader-scoped features in a single request.

| What You Need | Details |
|---|---|
| Authentication | Obtain a valid bearer token and include it in the `Authorization` header of every request. |
| Network reachability | The reader's HTTPS endpoint must be reachable from your client. Verify connectivity before issuing the request. |
| Feature decision | Choose exactly one reader-scoped feature (`fastID`, `tagFocus`, or `tagQuieting`) per request. `tagProtect` is tag-scoped and can be configured independently. |
| TagProtect credentials | For any `tagProtect` action, have the 8-character hex access password ready. For tag-specific actions (`enableTagProtection`, `disableTagProtection`), also have the target EPC (`tagID`). |
| Tag ID list (Basic Quieting) | For `tagQuieting.basic`, prepare the list of EPCs to quiet or unquiet. A maximum of **31 tag IDs** is supported per request. |
| Pre-select strategy (Advanced Quieting) | For `tagQuieting.advanced`, decide on the Gen2 select pre-conditions (`preSelect` array), including target session/SL flag, action, and memory mask. |
| Quiet mask flags | For `tagQuieting.advanced`, know which session flags (`S0A`-`S3B`, `SL_ASSERT`, `SL_DEASSERT`) define the quieted state. |
| Inventory state | `PUT /cloud/impinjGen2X` should be called **before** starting inventory. Stop any active inventory first by calling `PUT /cloud/stop`. |
| Activation | The saved configuration is **not active** until you call `PUT /cloud/start` with `applyImpinjGen2X: true` in the request body. |

---

## 3. Choosing a Gen2X Feature

The Gen2X feature you select determines the reader's behavior during inventory. Choose based on your operational goal.

| Feature | Description | Scope |
|---|---|---|
| `fastID` | Returns the EPC and TID together in a single read, eliminating the need for a separate TID read. Best for applications that require chip-level identity (anti-counterfeit, authentication). | Reader-scoped |
| `tagProtect` | Password-protects individual tags or controls reader visibility of protected tags. Use for securing sensitive items or restricting access. | Tag-scoped |
| `tagFocus` | Silences already-read tags so the reader focuses only on new tags entering the field. Ideal for portal and conveyor applications. | Reader-scoped |
| `tagQuieting` (basic) | Silences a specific list of tag EPCs from being reported during inventory. Use when you know exactly which tags to suppress. | Reader-scoped |
| `tagQuieting` (advanced) | Uses Gen2 select pre-conditions (mask + state-aware action) to silence tags based on memory content or session state. Use for complex filtering in dense environments. | Reader-scoped |

> Mutually exclusive: Only one of `fastID`, `tagFocus`, or `tagQuieting` can be active at a time. `tagProtect` can coexist with any one of them because it operates at the tag level.

---

## 4. Choosing TagProtect Actions

TagProtect operations either lock/unlock individual tags or temporarily allow the reader to see already-protected tags. Each action has specific field requirements.

| Action | What It Does | Required Fields | Key Constraints |
|---|---|---|---|
| `enableTagProtection` | Permanently protects a tag; the tag becomes invisible to standard reads until unprotected. | `password`, `tagID` | `password` must be exactly 8 hex characters. Optional `enableShortRange` reduces read range during protection. |
| `disableTagProtection` | Removes protection from a previously protected tag, restoring normal visibility. | `password`, `tagID` | `password` must match the tag's existing access password exactly. |
| `enableTagVisibility` | Temporarily allows the reader to read protected tags during this session. Does not change the tag's protection state. | `password` | Reader-scoped; affects all protected tags in field. |
| `disableTagVisibility` | Restores the default behavior where protected tags are hidden from the reader. | `password` | Reverts the effect of `enableTagVisibility`. |

> Important: `enableTagProtection` and `disableTagProtection` are tag-specific (require `tagID`). `enableTagVisibility` and `disableTagVisibility` are reader-wide visibility toggles.

---

## 5. Choosing TagQuieting Strategy

TagQuieting silences tags from being reported during inventory. Choose between **basic** (EPC-list based) and **advanced** (Gen2 select mask based) depending on your filtering complexity.

### Basic TagQuieting

| Field | What It Controls |
|---|---|
| `action: quiet` | Silences the listed tags from being reported in future inventories. |
| `action: unquiet` | Restores reporting for previously quieted tags. |
| `tagIDs` | Array of EPCs (hex strings) to quiet or unquiet. Maximum **31 EPCs** per request. |

### Advanced TagQuieting

Advanced quieting uses Gen2 select pre-conditions to silence tags based on memory content and state, instead of explicit EPC lists.

| Field | What It Controls |
|---|---|
| `preSelect[]` | Array of Gen2 select operations applied **before** quieting. Each entry contains `target`, `action`, and `mask`. |
| `preSelect[].target` | The session flag or SL to act upon (`S0`, `S1`, `S2`, `S3`, `SL`). |
| `preSelect[].action` | The state-aware action to take on match/mismatch (e.g., `ASSERTSL_NOTHING`, `INVB_INVA`, `DEASSERTSL_NOTHING`, `INVA_INVB`). |
| `preSelect[].mask` | The memory mask: `bank` (EPC/TID/USER/RESERVED), `pointer` (bit offset), `length` (bits), `value` (hex). |
| `tagQuietMasks` | Array of session-flag combinations defining the quieted state (`S0A`, `S2B`, `SL_ASSERT`, `SL_DEASSERT`, etc.). |
| `target` | The target session/flag used for the actual quieting operation. |
| `stateAwareAction` | The compound state action (e.g., `ASSERTSL_DEASSERTSL`, `DEASSERTSL_ASSERTSL`) applied during quieting. |

> Important: Use `basic` when you have a discrete list of EPCs. Use `advanced` when filtering by memory content, session state, or complex multi-step Gen2 select conditions.

---

## 6. Choosing FastID and TagFocus

These two reader-scoped features improve inventory performance but cannot be combined.

### `fastID`

| Field | What It Controls |
|---|---|
| `enabled: true` | Reader returns EPC + TID together in a single read, reducing total operations. |
| `enabled: false` | Reverts to standard EPC-only reads. |

**Use FastID when:** Your application needs TID for every tag (e.g., authentication, chip-level traceability) and you want to avoid the extra round-trip of a separate TID read.

### `tagFocus`

| Field | What It Controls |
|---|---|
| `enabled: true` | Once a tag is read, it is silenced for the rest of the inventory cycle. The reader focuses only on new tags entering the field. |
| `enabled: false` | Standard inventory behavior; tags can be reported multiple times. |

**Use TagFocus when:** You operate portals, conveyors, or other scenarios with many duplicate reads of the same tag set and want unique-tag reporting.

---

## 7. Applying the Configuration

Calling this endpoint only **saves** the configuration on the reader; it is not active until inventory is started with the activation flag.

### REST Workflow

```text
PUT  /cloud/stop                 -> stop any active inventory
PUT  /cloud/impinjGen2X          -> save the configuration
GET  /cloud/impinjGen2X          -> verify the saved configuration
PUT  /cloud/start                -> body: { "applyImpinjGen2X": true }
```

### Request Format

Every request to this endpoint follows this structure:

```http
PUT /cloud/impinjGen2X HTTP/1.1
Host: <reader-address>
Authorization: Bearer <token>
Content-Type: application/json

{
  // one or more Gen2X feature objects
}
```

### Success Response (`200 OK`)

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Configuration saved successfully"
}
```

### Error Responses

| Status Code | Meaning | When It Occurs |
|---|---|---|
| `422 Unprocessable Entity` | Validation error | Empty body, mutually exclusive features sent together, invalid enum value, or constraint violation. |
| `500 Internal Server Error` | Reader-side failure | Internal reader error while persisting the configuration. |

> Persistence: The reader stores the last saved configuration and restores it across reboots and reconnects. The configuration is only applied during inventory when `applyImpinjGen2X: true` is sent in the `PUT /cloud/start` request body.

---
