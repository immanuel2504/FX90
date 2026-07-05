# `set_cableLossCompensation` — OpenAPI schema feedback

**Commands:** `get_cableLossCompensation`, `set_cableLossCompensation`  
**REST endpoints:** `GET /cloud/cableLossCompensation`, `PUT /cloud/cableLossCompensation`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_cableLossCompensation` command and found a few documentation gaps. The API contract itself is consistent.

---

## 1. Field descriptions and units

- The fields `cableLength` and `cableLossPerHundredFt` (`type: number`) have no descriptions or units in either the GET or PUT schema.
- Could descriptions be added, including the unit of measure (e.g. feet for `cableLength`, dB per 100 ft for `cableLossPerHundredFt`) and any valid range?

---

## 2. Numbered keys `1`–`4` are not explained

- The request/response use object keys `1`, `2`, `3`, `4` (antenna ports) with no description.
- Could a description be added clarifying that these keys map to antenna port numbers, and how many are valid per device type?

---

## 3. PUT response

- The `200` response schema is `type: string` (empty string example) with no description.
- (The `400`/`500` error responses are documented — thank you.)

---

## Question

Please confirm the units and valid ranges for `cableLength` and `cableLossPerHundredFt`, and the number of supported antenna port keys.
