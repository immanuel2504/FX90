# `set_eSimConfig` — OpenAPI schema feedback

**Commands:** `get_eSimConfig`, `set_eSimConfig`  
**REST endpoints:** `GET /cloud/eSimConfig`, `PUT /cloud/eSimConfig`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_eSimConfig` command and found a few documentation gaps.

---

## 1. `operation` has no `enum`

- `set_eSimConfig.operation` is `type: string` with example `enable`, but there is no `enum`.
- Could you confirm the valid operations (e.g. `enable`, `disable`, …) and add an `enum`?

---

## 2. `get_eSimConfig` — `enabled` is a boolean typed as string

- In the GET response, `profiles[].enabled` is `type: string` with example `"true"`.
- Should this be `type: boolean`, or is it intentionally a string-encoded boolean? If it must stay a string, an `enum: ["true", "false"]` would make the allowed values explicit.

---

## 3. Field descriptions

- The request fields (`operation`, `profileNickName`) and the response fields (`eid`, `imei`, `profiles[].*`) have no descriptions.
- Adding descriptions would improve clarity.

---

## 4. PUT response has no schema

- The `200` response is `description: OK` only, with no `content`/`schema`.
- Could a response schema be added for consistency with other commands?

---

## Question

Please confirm the allowed values for `operation`, and whether `profiles[].enabled` should be `boolean` or a string-encoded boolean.
