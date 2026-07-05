# `del_certificate` — schema clarification (scenario)

**Command:** `del_certificate`  
**REST endpoint:** `DELETE /cloud/certificates/{certname}`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `del_certificate` command for `/cloud/certificates/{certname}` in `openAPISpec.yaml`.

I need clarification using this scenario:

To delete a client certificate named `reader`, the spec currently expects a **request body** on the DELETE call:

```json
{
  "name": "reader",
  "type": "client"
}
```

Two things are unclear:

1. **Where does `type` go?** — Our endpoint checklist expects `type` as a **query parameter** (`DELETE /cloud/certificates/reader?type=client`), but the spec defines it in a request body. A request body on DELETE is unusual and not supported by all HTTP clients. Could you confirm the intended location — query parameter or body?

2. **`type` values** — `type` is defined only as `type: string`, so `"client"`, `"server"`, or `"abc"` would all be valid. Could you confirm the valid types and add an `enum`?

Also, please add a response schema for the `200` response (currently `description: OK` only, with no body defined).

This will make the OpenAPI specification clearer and avoid confusion for API users.
