# `set_password` — OpenAPI schema feedback

**Command:** `set_password`  
**REST endpoint:** `PUT /cloud/updatePassword`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_password` command and found a few documentation gaps.

---

## 1. Field descriptions

- The request fields `currentPassword`, `newPassword`, and `userName` have no descriptions.
- Adding descriptions would improve clarity.

---

## 2. No `required` fields declared

- None of the request fields are marked `required`, although all three appear necessary.
- Could `required: [currentPassword, newPassword, userName]` be added?

---

## 3. Password complexity rules not documented

- `newPassword` has no `pattern`, `minLength`, or description of complexity requirements, even though the example (`Mypass@123`) suggests rules exist.
- Could the password requirements be documented (e.g. length, character classes)?

---

## 4. PUT response

- The response schema is `type: string` (empty string example) with no description explaining the expected response.

---

## Question

Please confirm which fields are required and the password complexity rules for `newPassword`.
