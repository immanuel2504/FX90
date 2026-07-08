# set_installCACertificate — test scenarios

| | |
|---|---|
| MQTT command | `set_installCACertificate` (publish envelope from `mqtt/`) |
| Verify with | matching `get_` command / GET endpoint after every test |

| # | File | Expect | Why / what breaks | Analogy (you are the user) | Verify |
|---|---|---|---|---|---|
| 01 | `mqtt/01_valid_full.json` *(MQTT only)* | **ACCEPTED** | The schema's own documented example. The golden path. | Like handing in a perfectly filled-out form - the clerk stamps it and files it. If the reader rejects THIS one, the reader (or the schema) has a bug. | success + setting really applied (read back) + command_id echoed |
| 04 | `mqtt/04_missing_required_name.json` *(MQTT only)* | **REJECTED** | Required field 'name' removed. Reader must fail with a clear message naming the field. | Like submitting a passport application without writing your name - the office cannot even start processing it and hands it straight back. | failure + field named + command_id echoed; state unchanged (read back) |
| 05 | `mqtt/05_missing_required_content.json` *(MQTT only)* | **REJECTED** | Required field 'content' removed. Reader must fail with a clear message naming the field. | Like submitting a passport application without writing your name - the office cannot even start processing it and hands it straight back. | failure + field named + command_id echoed; state unchanged (read back) |
| 06 | `mqtt/06_wrong_type_name.json` *(MQTT only)* | **REJECTED** | 'name' should be string but a int was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 07 | `mqtt/07_wrong_type_content.json` *(MQTT only)* | **REJECTED** | 'content' should be string but a int was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 08 | `mqtt/08_unknown_field.json` *(MQTT only)* | **CHECK BEHAVIOUR** | An extra field the schema does not define. Note whether the reader ignores it or rejects it - and that it is consistent across commands. | Like scribbling an extra line onto an official form - a lenient clerk ignores it, a strict one rejects the whole page. Verify which one the reader is, and that it is consistent. | record behaviour; must be consistent across commands |
| 09 | `mqtt/09_empty_payload.json` *(MQTT only)* | **REJECTED (unless all fields optional)** | Empty payload object. | Like handing in a completely blank form - nothing to act on; the reader should say so clearly, not crash or half-apply defaults. | failure + field named + command_id echoed; state unchanged (read back) |
| 10 | `mqtt/10_invalid_pem_content.json` *(MQTT only)* | **CHECK BEHAVIOUR** | content is plain text, not a PEM certificate - must be rejected by parsing, not stored broken. | Like a known pothole on a road - the map (schema) and the road (firmware) are suspected to disagree here. Drive it carefully and write down what actually happens. | record behaviour; must be consistent across commands |
| 11 | `mqtt/11_reinstall_same_name.json` *(MQTT only)* | **CHECK BEHAVIOUR** | Install twice with the same name - is it replace, reject, or duplicate? Must be documented. | Like two houses on one street with the same number - the postman cannot deliver; duplicates must be refused up front. | record behaviour; must be consistent across commands |
| 12 | `mqtt/12_mqtt_missing_command_id.json` *(MQTT only)* | **REJECTED** | Envelope without command_id - reader must reject (response cannot be correlated). | Like mailing a letter with no return address - even if the reader acts on it, you will never be able to match the reply to your request. | failure + field named + command_id echoed; state unchanged (read back) |
| 13 | `mqtt/13_mqtt_wrong_command_name.json` *(MQTT only)* | **REJECTED / NO RESPONSE** | Command name 'set_installCACertificate_TYPO' does not exist. | Like addressing the envelope to a department that does not exist - nobody should pick it up. | failure + field named + command_id echoed; state unchanged (read back) |

**Rejected scenarios:** always read the value back afterwards — a reject that still half-applied the change is the worst bug class.


**Before you start:** read [WHAT_YOU_NEED.md](WHAT_YOU_NEED.md) — equipment, pre-test state, risks and recovery for `set_installCACertificate`.
