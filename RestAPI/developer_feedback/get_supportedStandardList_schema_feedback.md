# `get_SupportedStandardList` — OpenAPI schema feedback

**Command:** `get_SupportedStandardList`  
**REST endpoint:** `GET /cloud/supportedStandardList`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_SupportedStandardList` command and found a few documentation gaps.

---

## 1. Field name inconsistency: `channeldata` vs `channelData`

- The response uses `channeldata` (lowercase `d`), while the `get_region` response uses `channelData` (camelCase).
- Could you confirm the correct casing? If the device actually returns `channeldata`, we will keep it; otherwise the schema should be aligned to `channelData`.

---

## 2. Boolean values typed as strings

- `isChannelSelectable`, `isHoppingConfigurable`, and `isLBTConfigurable` are defined as `type: string` with values like `"false"`.
- Should these be `type: boolean`, or are they intentionally string-encoded booleans? If they must stay strings, an `enum: ["true", "false"]` would make the allowed values explicit.

---

## 3. Field descriptions

- The response fields (`StandardName`, `channeldata`, `isChannelSelectable`, `isHoppingConfigurable`, `isLBTConfigurable`) and the `region` query parameter have no descriptions.
- Adding descriptions would improve clarity.

---

## Question

Please confirm (a) the correct casing for `channeldata`/`channelData`, and (b) whether the `is*` fields should be `boolean` or string-encoded.
