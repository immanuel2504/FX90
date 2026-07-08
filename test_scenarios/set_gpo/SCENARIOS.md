# set_gpo — test scenarios

| | |
|---|---|
| MQTT command | `set_gpo` (publish envelope from `mqtt/`) |
| REST endpoint | `PUT /cloud/gpo` (send body from `rest/`) |
| Verify with | matching `get_` command / GET endpoint after every test |

| # | File | Expect | Why / what breaks | Analogy (you are the user) | Verify |
|---|---|---|---|---|---|
| 01 | `mqtt/01_valid_full.json` · `rest/01_valid_full.json` | **ACCEPTED** | The schema's own documented example. The golden path. | Like handing in a perfectly filled-out form - the clerk stamps it and files it. If the reader rejects THIS one, the reader (or the schema) has a bug. | success + setting really applied (read back) + command_id echoed |
| 04 | `mqtt/04_missing_required_port.json` · `rest/04_missing_required_port.json` | **REJECTED** | Required field 'port' removed. Reader must fail with a clear message naming the field. | Like submitting a passport application without writing your name - the office cannot even start processing it and hands it straight back. | failure + field named + command_id echoed; state unchanged (read back) |
| 05 | `mqtt/05_missing_required_state.json` · `rest/05_missing_required_state.json` | **REJECTED** | Required field 'state' removed. Reader must fail with a clear message naming the field. | Like submitting a passport application without writing your name - the office cannot even start processing it and hands it straight back. | failure + field named + command_id echoed; state unchanged (read back) |
| 06 | `mqtt/06_wrong_type_port.json` · `rest/06_wrong_type_port.json` | **REJECTED** | 'port' should be number but a str was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 07 | `mqtt/07_wrong_type_state.json` · `rest/07_wrong_type_state.json` | **REJECTED** | 'state' should be boolean but a str was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 08 | `mqtt/08_boundary_high_port.json` · `rest/08_boundary_high_port.json` | **REJECTED** | 'port' maximum is 4; sending 5. | Like setting a kitchen oven to 900 degrees - the dial physically stops far earlier; anything past the limit must be refused, not silently clamped. | failure + field named + command_id echoed; state unchanged (read back) |
| 09 | `mqtt/09_unknown_field.json` · `rest/09_unknown_field.json` | **CHECK BEHAVIOUR** | An extra field the schema does not define. Note whether the reader ignores it or rejects it - and that it is consistent across commands. | Like scribbling an extra line onto an official form - a lenient clerk ignores it, a strict one rejects the whole page. Verify which one the reader is, and that it is consistent. | record behaviour; must be consistent across commands |
| 10 | `mqtt/10_empty_payload.json` · `rest/10_empty_payload.json` | **REJECTED (unless all fields optional)** | Empty payload object. | Like handing in a completely blank form - nothing to act on; the reader should say so clearly, not crash or half-apply defaults. | failure + field named + command_id echoed; state unchanged (read back) |
| 11 | `mqtt/11_mqtt_missing_command_id.json` *(MQTT only)* | **REJECTED** | Envelope without command_id - reader must reject (response cannot be correlated). | Like mailing a letter with no return address - even if the reader acts on it, you will never be able to match the reply to your request. | failure + field named + command_id echoed; state unchanged (read back) |
| 12 | `mqtt/12_mqtt_wrong_command_name.json` *(MQTT only)* | **REJECTED / NO RESPONSE** | Command name 'set_gpo_TYPO' does not exist. | Like addressing the envelope to a department that does not exist - nobody should pick it up. | failure + field named + command_id echoed; state unchanged (read back) |

**Rejected scenarios:** always read the value back afterwards — a reject that still half-applied the change is the worst bug class.
