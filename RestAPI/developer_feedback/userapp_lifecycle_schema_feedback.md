# `set_startUserapp` / `set_stopUserapp` / `set_autostartUserapp` / `set_uninstallUserapp` — OpenAPI schema feedback

**Commands:** `set_startUserapp`, `set_stopUserapp`, `set_autostartUserapp`, `set_uninstallUserapp`  
**REST endpoints:**  
- `PUT /cloud/apps/{appname}/start`  
- `PUT /cloud/apps/{appname}/stop`  
- `PUT /cloud/apps/{appname}/autostart`  
- `PUT /cloud/apps/{appname}/uninstall`  

**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the user-application lifecycle commands together as they share the same structure. The `appname` field is already well described (REST path parameter vs MQTT payload) — thank you.

---

## 1. PUT responses have no schema

- For all four commands, the `200` response is `description: OK` only, with no `content`/`schema`.
- Other set commands document the response (typically `type: string`, empty). Could a response schema be added for consistency?

---

## 2. `set_autostartUserapp` — `autostart` has no description

- `autostart` (`type: boolean`) is `required` and has an example, but no description.
- Could a short description be added (e.g. "Set to true to enable autostart on boot, false to disable")?

---

## Question

Should the responses for these four commands mirror the other set commands (`type: string`, empty)?
