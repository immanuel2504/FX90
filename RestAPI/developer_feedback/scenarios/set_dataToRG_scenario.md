# `set_dataToRG` — schema clarification (scenario)

**Command:** `set_dataToRG`  
**REST endpoint:** `PUT /cloud/setdataToRG`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_dataToRG` command for `/cloud/setdataToRG` in `openAPISpec.yaml`.

I need clarification using this scenario:

The description says the command "Sets data to RG":

> `set_dataToRG` — Sets data to RG.

But when I call `PUT /cloud/setdataToRG`, the endpoint defines **no request body / schema** — so it is unclear what data is actually sent to RG (Reader Gateway). The response is:

```json
""
```

Could you please confirm:

* Does `set_dataToRG` require a request body? If yes, what is its schema (fields and types)?
* If it is intentionally empty, could a note be added explaining what "data" is set and where it comes from?

Also, please add a description for the `200` response, which currently returns an empty string.

This will make the OpenAPI specification clearer and avoid confusion for API users.
