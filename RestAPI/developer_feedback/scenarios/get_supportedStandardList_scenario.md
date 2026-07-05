# `get_SupportedStandardList` — schema clarification (scenario)

**Command:** `get_SupportedStandardList`  
**REST endpoint:** `GET /cloud/supportedStandardList`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_SupportedStandardList` command for `/cloud/supportedStandardList` in `openAPISpec.yaml`.

I need clarification using this scenario:

When I call `GET /cloud/supportedStandardList?region=Argentina`, the example response is:

```json
{
  "SupportedStandards": [
    {
      "StandardName": "ARGENTINA",
      "channeldata": ["915750", "915250"],
      "isChannelSelectable": "false",
      "isHoppingConfigurable": "false",
      "isLBTConfigurable": "false"
    }
  ]
}
```

Two things are unclear from the schema:

1. **Field name casing** — this response uses `channeldata` (lowercase `d`), but the `get_region` response uses `channelData` (camelCase). Could you confirm the correct casing so the two responses are consistent?

2. **Boolean values typed as strings** — `isChannelSelectable`, `isHoppingConfigurable`, and `isLBTConfigurable` return `"false"` (a string), but they represent true/false values. The schema defines them as:

```yaml
isChannelSelectable:
  type: string
```

Should these be `type: boolean`? If they must remain strings, please add:

```yaml
enum: ["true", "false"]
```

Also, please add descriptions for these response fields and the `region` query parameter.

This will make the OpenAPI specification clearer and avoid confusion for API users.
