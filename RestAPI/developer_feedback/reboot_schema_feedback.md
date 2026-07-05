# `reboot` — OpenAPI schema feedback

**Command:** `reboot`  
**REST endpoint:** `PUT /cloud/reboot`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `reboot` command and found a couple of minor documentation gaps.

---

## 1. Description mentions a device ID that is not in the schema

- The description states the reader is restarted "with the device ID provided", but the REST endpoint defines no request body or parameter for a device ID.
- Could you clarify whether a device ID is required? If it is MQTT-only (topic-based), the REST description could be adjusted to avoid confusion.

---

## 2. PUT response

- The response schema is `type: string` (empty string example) with no description explaining the expected response.
- Could a short description be added?

---

## Question

Is a device ID required for the REST `PUT /cloud/reboot` call, or is it implied by the connection/topic (MQTT only)?
