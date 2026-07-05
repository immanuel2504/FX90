# `set_revertbackOS` — schema clarification (scenario)

**Command:** `set_revertbackOS`  
**REST endpoint:** `PUT /cloud/revertbackOS`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_revertbackOS` command for `/cloud/revertbackOS` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/revertbackOS` with an empty body:

```json
{}
```

On success, the `200` response is defined as:

```yaml
responses:
  '200':
    description: OK
```

There is no `content`/`schema`, so it is unclear what the response body looks like. Other set commands document a response body (typically `type: string`, empty). Could a response schema be added for consistency?

This will make the OpenAPI specification clearer and avoid confusion for API users.
