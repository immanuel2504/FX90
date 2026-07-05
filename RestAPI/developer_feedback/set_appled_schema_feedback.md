# `get_appled` / `set_appled` — OpenAPI schema feedback

**Commands:** `get_appled`, `set_appled`  
**REST endpoints:** `GET /cloud/app-led`, `PUT /cloud/app-led`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_appled` and `set_appled` commands and found a few documentation gaps. The API contract itself is consistent, but some schema metadata could be improved.

---

## 1. `set_appled` — `color` has no `enum`

- `color` is defined as `type: string` with example `amber`, but there is no `enum`.
- The equivalent `set_stackled` command defines `color` with `enum: [red, amber, green, blue, off]` and a description. For consistency, could the same `enum` and description be added to `set_appled`?

---

## 2. `get_appled` — `status` has no `enum`

- The GET response `status` is `type: string` with example `DEFAULT`, but there is no `enum`.
- Could you confirm the allowed values (e.g. `DEFAULT`, `NON_DEFAULT`) and add an `enum` if the set is fixed?

---

## 3. Field descriptions

- The `set_appled` request fields (`color`, `flash`, `seconds`) and the `get_appled` response field (`status`) have no descriptions.
- Adding descriptions (including the unit for `seconds`) would make the documentation clearer.

---

## 4. PUT response

- The `set_appled` response schema is `type: string` (empty string example) with no description explaining the expected response.
- Could a short description be added?

---

## Question

Please confirm the allowed values for `set_appled.color` and `get_appled.status` so we can decide whether an `enum` should be added.
