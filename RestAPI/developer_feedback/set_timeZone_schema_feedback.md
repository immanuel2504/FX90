# `set_timeZone` — OpenAPI schema feedback

**Commands:** `get_timeZone`, `set_timeZone`  
**REST endpoints:** `GET /cloud/timeZone`, `PUT /cloud/timeZone`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_timeZone` command and found a few documentation gaps.

---

## 1. PUT response has no schema

- The `set_timeZone` `200` response is defined as `description: OK` only, with no `content`/`schema`.
- Other set commands document the response (typically `type: string`, empty). Could a response schema be added for consistency?

---

## 2. `timeZone` format not documented

- `timeZone` is `type: string` with example `Asia/Dubai`, but the expected format is not stated.
- Could a description be added noting the format (e.g. IANA time zone identifier)? An `enum` is likely impractical here, so a description/format note would be sufficient.

---

## Question

Should the response schema mirror the other set commands (`type: string`, empty), and can the `timeZone` format be documented as an IANA identifier?
