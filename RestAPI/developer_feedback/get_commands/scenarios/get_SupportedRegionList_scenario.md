# `get_SupportedRegionList` — schema clarification (scenario)

**Command:** `get_SupportedRegionList`  
**REST endpoint:** `GET /cloud/supportedRegionList`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_SupportedRegionList` command for `/cloud/supportedRegionList` in `openAPISpec.yaml`.

When I call `GET /cloud/supportedRegionList`, the example response is:

```json
{
  "SupportedRegions": ["Argentina", "Australia", "Canada", "India", "..."]
}
```

The schema types this correctly as an array of strings:

```yaml
SupportedRegions:
  type: array
  items:
    type: string
```

Compared with the MQTT `get_SupportedRegionList` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal, the only thing missing is that `SupportedRegions` has **no description** (and there is no `required` list). The Zebra IoTC MQTT documentation describes it as "the list of countries supported by the reader."

Could you please add a description for `SupportedRegions` (and confirm whether it should be `required`)?
