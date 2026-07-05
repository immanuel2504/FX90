# `set_timeZone` — schema clarification (scenario)

**Commands:** `get_timeZone`, `set_timeZone`  
**REST endpoints:** `GET /cloud/timeZone`, `PUT /cloud/timeZone`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_timeZone` command for `/cloud/timeZone` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `PUT /cloud/timeZone`, the example request is:

```json
{
  "timeZone": "Asia/Dubai"
}
```

On success, the `200` response is defined as:

```yaml
responses:
  '200':
    description: OK
```

There is no `content`/`schema`, so it is unclear what the response body looks like. Other set commands document a response body (typically `type: string`, empty). Could a response schema be added for consistency?

Also, `timeZone` is defined only as:

```yaml
timeZone:
  type: string
```

The expected format is not stated. Could a description be added noting the format (e.g. IANA time zone identifier such as `Asia/Dubai`)?

This will make the OpenAPI specification clearer and avoid confusion for API users.
