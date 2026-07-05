# `set_startUserapp` / `set_stopUserapp` / `set_autostartUserapp` / `set_uninstallUserapp` — schema clarification (scenario)

**Commands:** `set_startUserapp`, `set_stopUserapp`, `set_autostartUserapp`, `set_uninstallUserapp`  
**REST endpoints:**  
- `PUT /cloud/apps/{appname}/start`  
- `PUT /cloud/apps/{appname}/stop`  
- `PUT /cloud/apps/{appname}/autostart`  
- `PUT /cloud/apps/{appname}/uninstall`  

**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the user-application lifecycle commands for `/cloud/apps/{appname}/...` in `openAPISpec.yaml`. They share the same structure, so I am raising them together. The `appname` field is already well documented (REST path parameter vs MQTT payload) — thank you.

I need clarification using this scenario:

When I call, for example, `PUT /cloud/apps/mylogger/start`, on success the `200` response is defined as:

```yaml
responses:
  '200':
    description: OK
```

There is no `content`/`schema` for any of the four commands, so it is unclear what the response body looks like. Other set commands document a response body (typically `type: string`, empty). Could a response schema be added for consistency across all four?

Additionally, for `set_autostartUserapp`, the request field `autostart`:

```json
{
  "appname": "mylogger",
  "autostart": true
}
```

is `required` and has an example but no description. Could a short description be added (e.g. "Set to true to enable autostart on boot, false to disable")?

This will make the OpenAPI specification clearer and avoid confusion for API users.
