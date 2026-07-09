# set_appled — test scenarios

| | |
|---|---|
| MQTT command | `set_appled` (publish envelope from `mqtt/`) |
| REST endpoint | `PUT /cloud/app-led` (send body from `rest/`) |
| Verify with | matching `get_` command / GET endpoint after every test |

| # | File | Expect | Why / what breaks | Analogy (you are the user) | Verify |
|---|---|---|---|---|---|
| 01 | `mqtt/01_valid_full.json` · `rest/01_valid_full.json` | **ACCEPTED** | The schema's own documented example. The golden path. | Like handing in a perfectly filled-out form - the clerk stamps it and files it. If the reader rejects THIS one, the reader (or the schema) has a bug. | success + setting really applied (read back) + command_id echoed |
| 04 | `mqtt/04_wrong_type_color.json` · `rest/04_wrong_type_color.json` | **REJECTED** | 'color' should be string but a int was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 05 | `mqtt/05_wrong_type_flash.json` · `rest/05_wrong_type_flash.json` | **REJECTED** | 'flash' should be boolean but a str was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 06 | `mqtt/06_wrong_type_seconds.json` · `rest/06_wrong_type_seconds.json` | **REJECTED** | 'seconds' should be number but a str was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 07 | `mqtt/07_invalid_enum_color.json` · `rest/07_invalid_enum_color.json` | **REJECTED** | 'color' must be one of ['red', 'amber', 'green', 'blue', 'off'] - 'NOT_A_VALID_VALUE' is not on the menu. | Like ordering size 'XXL' in a shop that only stocks S, M and L - the value must come from the fixed menu. | failure + field named + command_id echoed; state unchanged (read back) |
| 08 | `mqtt/08_unknown_field.json` · `rest/08_unknown_field.json` | **CHECK BEHAVIOUR** | An extra field the schema does not define. Note whether the reader ignores it or rejects it - and that it is consistent across commands. | Like scribbling an extra line onto an official form - a lenient clerk ignores it, a strict one rejects the whole page. Verify which one the reader is, and that it is consistent. | record behaviour; must be consistent across commands |
| 09 | `mqtt/09_empty_payload.json` · `rest/09_empty_payload.json` | **REJECTED (unless all fields optional)** | Empty payload object. | Like handing in a completely blank form - nothing to act on; the reader should say so clearly, not crash or half-apply defaults. | failure + field named + command_id echoed; state unchanged (read back) |
| 10 | `mqtt/10_mqtt_missing_command_id.json` *(MQTT only)* | **REJECTED** | Envelope without command_id - reader must reject (response cannot be correlated). | Like mailing a letter with no return address - even if the reader acts on it, you will never be able to match the reply to your request. | failure + field named + command_id echoed; state unchanged (read back) |
| 11 | `mqtt/11_mqtt_wrong_command_name.json` *(MQTT only)* | **REJECTED / NO RESPONSE** | Command name 'set_appled_TYPO' does not exist. | Like addressing the envelope to a department that does not exist - nobody should pick it up. | failure + field named + command_id echoed; state unchanged (read back) |

**Rejected scenarios:** always read the value back afterwards — a reject that still half-applied the change is the worst bug class.
