# `get_cableLossCompensation` — OpenAPI schema feedback

**Command:** `get_cableLossCompensation`  
**REST endpoint:** `GET /cloud/cableLossCompensation`  
**Reference:** `openAPISpec.yaml` (compared against the MQTT `get_cableLossCompensation` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal)  

Hi,

I reviewed the `get_cableLossCompensation` command and compared the `GET /cloud/cableLossCompensation` response in `openAPISpec.yaml` with the MQTT `get_cableLossCompensation` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal. The structure matches, but a few constraints and descriptions are missing.

---

## 1. Numbered keys are unexplained

- The response is an object keyed by read-point numbers (`1`, `2`, `3`, `4`), each with `cableLength` and `cableLossPerHundredFt`, but there is no description explaining that the keys are read-point/antenna port numbers.
- The Zebra IoTC MQTT documentation describes each block as "Cable loss compensation values for read point N." Please add descriptions.

---

## 2. `cableLength` / `cableLossPerHundredFt` have no descriptions or constraints

- Both are `type: number` with no description and no bounds in `openAPISpec.yaml`.
- The Zebra IoTC MQTT documentation describes them and applies `minimum: 0`. Please add the descriptions and `minimum: 0`. Also consider documenting the units (cable length and loss per hundred feet).

---

## 3. No `required` list

- The Zebra IoTC MQTT documentation marks read points `1`–`4` (and the inner `cableLength`/`cableLossPerHundredFt`) as `required`. `openAPISpec.yaml` has no `required` list — please confirm and add if appropriate.

---

## Note

The MQTT `get_cableLossCompensation` command in the Zebra IoTC documentation is the complete reference. This is a request to add descriptions, the `minimum: 0` constraint, and (optionally) the `required` list. (Note: not applicable to ATR7000 readers.)
