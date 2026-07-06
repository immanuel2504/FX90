# `get_region` — OpenAPI schema feedback

**Command:** `get_region`  
**REST endpoint:** `GET /cloud/region`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_region` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_region` command and compared the `GET /cloud/region` response in `openAPISpec.yaml` with the MQTT `get_region` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The field set matches, but the item type of `channelData` differs and descriptions are missing.

---

## 1. `channelData` item type mismatch (`integer` vs `string`)

- In `openAPISpec.yaml`, `channelData` is `type: array` with `items: type: integer`, and the example uses integers (`[915250, 915750, 903250, 926750]`).
- The Zebra IoTC MQTT documentation defines `channelData` as an array of **strings** (e.g. `["915750", "915250", "903250"]`).
- This is the same string-vs-number question raised for `get_SupportedStandardList` (`channeldata`). Please confirm whether the device returns channel values as strings or integers, and align the item type (and example) accordingly.

---

## 2. Fields have no descriptions

- None of the response fields (`FrequencyHopping`, `region`, `regulatoryStandard`, `lbtEnabled`, `channelData`, `country`, `minTxPowerSupported`, `maxTxPowerSupported`) have descriptions.
- The Zebra IoTC MQTT documentation provides a description for each (e.g. `FrequencyHopping` = "Whether frequency hopping is enabled for the active regulatory standard", `lbtEnabled` = "Whether Listen Before Talk (LBT) is enabled…"). Please port these descriptions.

---

## 3. No `required` list

- The Zebra IoTC MQTT documentation marks all region fields as `required`; `openAPISpec.yaml` has no `required` list. Please confirm and add if appropriate.

---

## Note

The MQTT `get_region` command in the Zebra IoTC documentation is the complete reference. The key item to confirm is the `channelData` item type (string vs integer); descriptions and the `required` list are the remaining alignment items.
