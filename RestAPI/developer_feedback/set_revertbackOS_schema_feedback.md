# `set_revertbackOS` — OpenAPI schema feedback

**Command:** `set_revertbackOS`  
**REST endpoint:** `PUT /cloud/revertbackOS`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_revertbackOS` command and found one minor documentation gap. The request correctly takes an empty object.

---

## 1. PUT response has no schema

- The `200` response is `description: OK` only, with no `content`/`schema`.
- Could a response schema be added for consistency with other commands (e.g. `type: string`, empty)?

---

## Question

Should the response mirror the other set commands (`type: string`, empty)?
