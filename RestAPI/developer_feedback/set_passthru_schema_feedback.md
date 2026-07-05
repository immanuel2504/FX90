# `set_passthru` — OpenAPI schema feedback

**Command:** `set_passthru`  
**REST endpoint:** `PUT /cloud/pass-through`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_passthru` command and found a few documentation gaps.

---

## 1. `operationId` is `status`

- The `operationId` for this PUT is `status`, which is not a verb-based, descriptive identifier and does not match the naming used by other operations (e.g. `setPassthru`).
- Could the `operationId` be renamed to something like `setPassthru` for consistency?

---

## 2. `component` has no `enum`

- `component` is `type: string` with example `RC`, but there is no `enum`.
- Could you confirm the valid components (e.g. `RC`) and add an `enum` if the set is fixed?

---

## 3. Field descriptions

- The request fields (`component`, `payload`) and the response field (`response`) have no descriptions.
- Adding descriptions (including the valid `payload` values such as `mode`, `status`) would improve clarity.

---

## Question

Please confirm the allowed values for `component` and `payload` so we can decide whether an `enum` should be added.
