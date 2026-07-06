# `get_timeZone` — OpenAPI schema feedback

**Command:** `get_timeZone`  
**REST endpoint:** `GET /cloud/timeZone`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_timeZone` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_timeZone` command and compared the `GET /cloud/timeZone` response in `openAPISpec.yaml` with the MQTT `get_timeZone` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The response returns a single `timeZone` string, but it is under-specified.

---

## 1. `timeZone` has no `enum`

- In `openAPISpec.yaml`, `timeZone` is `type: string` with example `UTC`, but there is no `enum`.
- The Zebra IoTC MQTT documentation constrains `timeZone` to a fixed list of allowed time zones (e.g. `Coordinated Universal Time`, `Pacific Time (US & Canada)`, `Chennai, Kolkata, Mumbai, New Delhi`, and the `(GMT±hh:mm) …` variants). Please add the same `enum` so callers know the accepted values.

---

## 2. Example `UTC` is not one of the allowed values

- The example value `UTC` does not appear in the Zebra IoTC MQTT allowed list (the closest entries are `Coordinated Universal Time` and `(UTC) Coordinated Universal Time`).
- Please align the example with a value from the `enum`.

---

## 3. `timeZone` has no description

- The field has no description in `openAPISpec.yaml`. The Zebra IoTC MQTT documentation describes it as the allowed reader time zone. Please add a description.

---

## Note

The MQTT `get_timeZone` command in the Zebra IoTC documentation is the complete reference. This is a request to add the `timeZone` `enum`, fix the example to a valid value, and add a description.
