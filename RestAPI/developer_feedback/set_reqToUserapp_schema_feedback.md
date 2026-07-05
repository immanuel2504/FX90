# `set_reqToUserapp` — OpenAPI schema feedback

**Command:** `set_reqToUserapp`  
**REST endpoint:** `PUT /cloud/apps/{appname}/pass-through`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_reqToUserapp` command and found a couple of documentation gaps.

---

## 1. Field descriptions

- The request fields (`command`, `command.message`, `userapp`) have no descriptions.
- Adding descriptions would improve clarity, especially since `command` is an open object that is passed through to the user application.

---

## 2. Response body is an untyped object

- The `200` response schema is `type: object` with no `properties`, description, or example.
- Since the response is application-defined, could a description be added noting that the payload is passed through from the user application (and is not fixed)?

---

## Question

Is the response payload intentionally application-defined (pass-through), or should it have a fixed schema?
