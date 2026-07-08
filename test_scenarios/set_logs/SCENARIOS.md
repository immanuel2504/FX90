# set_logs — test scenarios

| | |
|---|---|
| MQTT command | `set_logs` (publish envelope from `mqtt/`) |
| REST endpoint | `PUT /cloud/logs` (send body from `rest/`) |
| Verify with | matching `get_` command / GET endpoint after every test |

| # | File | Expect | Why / what breaks | Analogy (you are the user) | Verify |
|---|---|---|---|---|---|
| 01 | `mqtt/01_valid_full.json` · `rest/01_valid_full.json` | **ACCEPTED** | The schema's own documented example. The golden path. | Like handing in a perfectly filled-out form - the clerk stamps it and files it. If the reader rejects THIS one, the reader (or the schema) has a bug. | success + setting really applied (read back) + command_id echoed |
| 04 | `mqtt/04_wrong_type_radioPacketLog.json` · `rest/04_wrong_type_radioPacketLog.json` | **REJECTED** | 'radioPacketLog' should be boolean but a str was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 05 | `mqtt/05_unknown_field.json` · `rest/05_unknown_field.json` | **CHECK BEHAVIOUR** | An extra field the schema does not define. Note whether the reader ignores it or rejects it - and that it is consistent across commands. | Like scribbling an extra line onto an official form - a lenient clerk ignores it, a strict one rejects the whole page. Verify which one the reader is, and that it is consistent. | record behaviour; must be consistent across commands |
| 06 | `mqtt/06_empty_payload.json` · `rest/06_empty_payload.json` | **REJECTED (unless all fields optional)** | Empty payload object. | Like handing in a completely blank form - nothing to act on; the reader should say so clearly, not crash or half-apply defaults. | failure + field named + command_id echoed; state unchanged (read back) |
| 07 | `mqtt/07_mqtt_missing_command_id.json` *(MQTT only)* | **REJECTED** | Envelope without command_id - reader must reject (response cannot be correlated). | Like mailing a letter with no return address - even if the reader acts on it, you will never be able to match the reply to your request. | failure + field named + command_id echoed; state unchanged (read back) |
| 08 | `mqtt/08_mqtt_wrong_command_name.json` *(MQTT only)* | **REJECTED / NO RESPONSE** | Command name 'set_logs_TYPO' does not exist. | Like addressing the envelope to a department that does not exist - nobody should pick it up. | failure + field named + command_id echoed; state unchanged (read back) |

**Rejected scenarios:** always read the value back afterwards — a reject that still half-applied the change is the worst bug class.
