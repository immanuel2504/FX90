# `get_region` — schema clarification (scenario)

**Command:** `get_region`  
**REST endpoint:** `GET /cloud/region`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_region` command for `/cloud/region` in `openAPISpec.yaml`.

When I call `GET /cloud/region`, the example response is:

```json
{
  "FrequencyHopping": true,
  "channelData": [915250, 915750, 903250, 926750],
  "country": "Canada",
  "lbtEnabled": false,
  "maxTxPowerSupported": 300,
  "minTxPowerSupported": 100,
  "region": "US",
  "regulatoryStandard": "FCC"
}
```

Here `channelData` is an array of **integers** and the schema defines it as:

```yaml
channelData:
  type: array
  items:
    type: integer
```

But the MQTT `get_region` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal returns `channelData` as an array of **strings**:

```json
"channelData": ["915750", "915250", "903250"]
```

This is the same string-vs-number question raised for `get_SupportedStandardList`. Could you please confirm whether channel values are strings or integers, and align the `items` type (and example) accordingly?

Also, please add descriptions for the response fields (`FrequencyHopping`, `region`, `regulatoryStandard`, `lbtEnabled`, `channelData`, `country`, `minTxPowerSupported`, `maxTxPowerSupported`), which the Zebra IoTC MQTT documentation provides but `openAPISpec.yaml` does not.
