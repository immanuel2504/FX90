# `del_certificate` — OpenAPI schema feedback

**Command:** `del_certificate`  
**REST endpoint:** `DELETE /cloud/certificates/{certname}`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `del_certificate` command and found a few documentation gaps.

---

## 1. `type` passed via request body vs query parameter

- The DELETE operation defines `type` inside a `requestBody`, but our endpoint checklist expects `type` as a query parameter (`?type=...`).
- Could you confirm the intended location for `type` on the REST DELETE call — request body or query parameter? DELETE with a request body is unusual and not supported by all clients.

---

## 2. `type` has no `enum`

- `type` is `type: string` with example `client`, but there is no `enum`.
- Could you confirm the valid certificate types (e.g. `client`, `server`) and add an `enum`?

---

## 3. PUT/DELETE response has no schema

- The `200` response is `description: OK` only, with no `content`/`schema`.
- Could a response schema be added for consistency with other commands?

---

## Question

Please confirm (a) whether `type` should be a query parameter or request body field for the REST DELETE, and (b) the valid values for `type`.
