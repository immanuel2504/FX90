# `set_region` — OpenAPI schema feedback

**Commands:** `get_region`, `set_region`  
**REST endpoints:** `GET /cloud/region`, `PUT /cloud/region`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_region` command and found a few documentation gaps. The API contract itself is consistent, but some schema metadata could be improved.

---

## 1. `standardname` has no `enum` or reference to valid values

- `set_region.standardname` is `type: string` with example `CANADA_FCC_15`, but there is no `enum`.
- The valid standard names appear to come from `get_SupportedStandardList` (per region). Could the schema either list the allowed values via `enum`, or reference how to obtain them (e.g. "use the value from `get_SupportedStandardList`")?

---

## 2. `country` has no `enum` or reference

- `set_region.country` is `type: string` with example `Canada`, but there is no `enum`.
- The valid countries appear to come from `get_SupportedRegionList`. Could the schema reference this, or add an `enum`?

---

## 3. Field descriptions

- `country` and `standardname` have no descriptions in the request schema.
- Adding descriptions would improve clarity.

---

## 4. PUT response

- The response schema is `type: string` (empty string example) with no description explaining the expected response.

---

## Question

Should `country` and `standardname` be constrained by `enum`, or are they intentionally free-form strings validated against `get_SupportedRegionList` / `get_SupportedStandardList` at runtime?
