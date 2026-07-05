# `set_dataToRG` — OpenAPI schema feedback

**Command:** `set_dataToRG`  
**REST endpoint:** `PUT /cloud/setdataToRG`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_dataToRG` command and found a documentation gap.

---

## 1. No request body defined despite "Sets data to RG"

- The summary/description says the command "Sets data to RG", but the endpoint defines no `requestBody`/schema.
- Could you clarify what data is sent to RG (Reader Gateway)? If a request body is expected, please add its schema; if it is intentionally empty, a note would help.

---

## 2. PUT response

- The response schema is `type: string` (empty string example) with no description explaining the expected response.

---

## Question

Does `set_dataToRG` require a request body? If so, what is its schema?
