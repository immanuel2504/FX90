# `get_SupportedRegionList` — OpenAPI schema feedback

**Command:** `get_SupportedRegionList`  
**REST endpoint:** `GET /cloud/supportedRegionList`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_SupportedRegionList` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_SupportedRegionList` command and compared the `GET /cloud/supportedRegionList` response in `openAPISpec.yaml` with the MQTT `get_SupportedRegionList` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The shape (`SupportedRegions` array of strings) matches; only a small documentation item is missing.

---

## 1. `SupportedRegions` has no description

- In `openAPISpec.yaml`, `SupportedRegions` is `type: array` of `string` with an example list but no description.
- The Zebra IoTC MQTT documentation describes it as the array containing "the list of countries supported by the reader." Please add the description.

---

## 2. No `required` list

- The Zebra IoTC MQTT documentation returns `SupportedRegions` on every success response. `openAPISpec.yaml` has no `required` list — please confirm and add `required: [SupportedRegions]` if appropriate.

---

## Note

The MQTT `get_SupportedRegionList` command in the Zebra IoTC documentation is the complete reference. This endpoint is already well typed; the only ask is a field description (and optionally the `required` list).
