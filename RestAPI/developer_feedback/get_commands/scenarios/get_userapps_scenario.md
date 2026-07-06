# `get_userapps` — schema clarification (scenario)

**Command:** `get_userapps`  
**REST endpoint:** `GET /cloud/apps`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_userapps` command for `/cloud/apps` in `openAPISpec.yaml`.

When I call `GET /cloud/apps`, the example response is an array of app objects:

```json
[
  { "appname": "mylogger", "runningStatus": true, "autostart": false, "metadata": "APP_TYPE: DA" }
]
```

The schema types the fields correctly, but none of them have descriptions and there is no `required` list:

```yaml
appname: { type: string }
runningStatus: { type: boolean }
autostart: { type: boolean }
metadata: { type: string }
```

The MQTT `get_userapps` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal:

* describes each field (e.g. `runningStatus` = "Whether the user application is currently running", `autostart` = "Whether the user application is configured to start automatically"),
* marks `appname`, `autostart`, `metadata`, `runningStatus` as `required` per item,
* applies `minItems: 1` / `uniqueItems: true` on the array and `default: true` on `autostart`.

Could you please add the descriptions, the item-level `required` list, and the array/field constraints?
