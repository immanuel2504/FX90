# `set_gpo` — OpenAPI schema feedback

**Commands:** `get_gpoStatus`, `set_gpo`  
**REST endpoints:** `GET /cloud/gpo`, `PUT /cloud/gpo`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_gpo` command and found a couple of minor documentation gaps. The API contract itself is consistent.

---

## 1. Field descriptions and valid range

- The `set_gpo` request fields `port` (`type: number`) and `state` (`type: boolean`) have no descriptions.
- The endpoint description notes the maximum ports per device type (FXR90 = 4). Could a valid range/`minimum`/`maximum` (or description) be added to `port` so integrators know the allowed port numbers?

---

## 2. PUT response

- The response schema is `type: string` (empty string example) with no description explaining the expected response.
- Could a short description be added?

---

## Question

Should `port` be constrained (e.g. `minimum: 1`, `maximum: 4` for FXR90), or is it left open because the range depends on the device type?
