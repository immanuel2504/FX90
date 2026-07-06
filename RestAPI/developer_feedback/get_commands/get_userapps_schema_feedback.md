# `get_userapps` — OpenAPI schema feedback

**Command:** `get_userapps`  
**REST endpoint:** `GET /cloud/apps`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_userapps` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_userapps` command and compared the `GET /cloud/apps` response in `openAPISpec.yaml` with the MQTT `get_userapps` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The response is an array of app objects; the fields match but are under-specified.

---

## 1. Fields have no descriptions

- The per-app fields (`appname`, `runningStatus`, `autostart`, `metadata`) have no descriptions.
- The Zebra IoTC MQTT documentation describes each (e.g. `runningStatus` = "Whether the user application is currently running", `autostart` = "Whether the user application is configured to start automatically", `metadata` = "User application metadata reported by the reader"). Please port these descriptions.

---

## 2. No `required` list on the item

- The Zebra IoTC MQTT documentation marks `appname`, `autostart`, `metadata`, and `runningStatus` as `required` for each array item. `openAPISpec.yaml` has no `required` list — please confirm and add.

---

## 3. Missing array/field constraints

- The Zebra IoTC MQTT documentation applies `minItems: 1` and `uniqueItems: true` on the array, a `default: true` on `autostart`, and `minLength: 1` on the string fields.
- These are absent in `openAPISpec.yaml`. Please add them if they apply to the REST response.

---

## Note

The MQTT `get_userapps` command in the Zebra IoTC documentation is the complete reference. This is a request to add field descriptions, the item-level `required` list, and the array/field constraints to the `GET /cloud/apps` response schema.
