# `set_logs` — OpenAPI schema feedback

**Commands:** `get_logs`, `set_logs`  
**REST endpoints:** `GET /cloud/logs`, `PUT /cloud/logs`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_logs` command and found a few documentation gaps.

---

## 1. `level` has no `enum`

- `components[].level` is `type: string` with example `DEBUG`, but there is no `enum`.
- Could you confirm the valid log levels (e.g. `ERROR`, `WARNING`, `INFO`, `DEBUG`) and add an `enum`?

---

## 2. `componentName` has no `enum` or reference

- `components[].componentName` is `type: string` with example `radio_control`, but there is no `enum`.
- Could you list the valid component names, or reference how to obtain them (e.g. from `get_logs`)?

---

## 3. Field descriptions

- The request/response fields (`componentName`, `level`, `radioPacketLog`) have no descriptions.
- Adding descriptions would improve clarity.

---

## Question

Please confirm the allowed values for `level` and `componentName` so we can decide whether an `enum` should be added.
