# `set_hostName` — OpenAPI schema feedback

**Commands:** `get_hostName`, `set_hostName`  
**REST endpoints:** `GET /cloud/hostName`, `PUT /cloud/hostName`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `set_hostName` command and found a field naming inconsistency plus a few documentation gaps.

---

## 1. Request/response field name inconsistency: `hostname` vs `hostName`

- The `set_hostName` request uses `hostname` (all lowercase).
- The `get_hostName` response uses `hostName` (camelCase).
- Could you confirm which casing the device expects for the request? The GET/PUT field names should match unless there is a specific reason they differ.

---

## 2. Field descriptions and constraints

- `hostname`/`hostName` have no descriptions, and no `pattern`/length constraints for valid hostnames.
- Adding a description and any validation rules (allowed characters, max length) would improve clarity.

---

## 3. PUT response

- The response schema is `type: string` (empty string example) with no description explaining the expected response.

---

## Question

Please confirm the correct request field name (`hostname` vs `hostName`) and any hostname validation rules.
