# set_eSimConfig — test scenarios

| | |
|---|---|
| MQTT command | `set_eSimConfig` (publish envelope from `mqtt/`) |
| REST endpoint | `PUT /cloud/eSimConfig` (send body from `rest/`) |
| Verify with | matching `get_` command / GET endpoint after every test |

| # | File | Expect | Why / what breaks | Analogy (you are the user) | Verify |
|---|---|---|---|---|---|
| 01 | `mqtt/01_valid_full.json` · `rest/01_valid_full.json` | **ACCEPTED** | The schema's own documented example. The golden path. | Like handing in a perfectly filled-out form - the clerk stamps it and files it. If the reader rejects THIS one, the reader (or the schema) has a bug. | success + setting really applied (read back) + command_id echoed |
| 04 | `mqtt/04_wrong_type_operation.json` · `rest/04_wrong_type_operation.json` | **REJECTED** | 'operation' should be string but a int was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 05 | `mqtt/05_wrong_type_profileNickName.json` · `rest/05_wrong_type_profileNickName.json` | **REJECTED** | 'profileNickName' should be string but a int was sent. | Like writing the word 'blue' in the phone-number box - right form, wrong kind of answer in that field. | failure + field named + command_id echoed; state unchanged (read back) |
| 06 | `mqtt/06_invalid_enum_operation.json` · `rest/06_invalid_enum_operation.json` | **REJECTED** | 'operation' must be one of ['enable', 'disable'] - 'NOT_A_VALID_VALUE' is not on the menu. | Like ordering size 'XXL' in a shop that only stocks S, M and L - the value must come from the fixed menu. | failure + field named + command_id echoed; state unchanged (read back) |
| 07 | `mqtt/07_unknown_field.json` · `rest/07_unknown_field.json` | **CHECK BEHAVIOUR** | An extra field the schema does not define. Note whether the reader ignores it or rejects it - and that it is consistent across commands. | Like scribbling an extra line onto an official form - a lenient clerk ignores it, a strict one rejects the whole page. Verify which one the reader is, and that it is consistent. | record behaviour; must be consistent across commands |
| 08 | `mqtt/08_empty_payload.json` · `rest/08_empty_payload.json` | **REJECTED (unless all fields optional)** | Empty payload object. | Like handing in a completely blank form - nothing to act on; the reader should say so clearly, not crash or half-apply defaults. | failure + field named + command_id echoed; state unchanged (read back) |
| 09 | `mqtt/09_mqtt_missing_command_id.json` *(MQTT only)* | **REJECTED** | Envelope without command_id - reader must reject (response cannot be correlated). | Like mailing a letter with no return address - even if the reader acts on it, you will never be able to match the reply to your request. | failure + field named + command_id echoed; state unchanged (read back) |
| 10 | `mqtt/10_mqtt_wrong_command_name.json` *(MQTT only)* | **REJECTED / NO RESPONSE** | Command name 'set_eSimConfig_TYPO' does not exist. | Like addressing the envelope to a department that does not exist - nobody should pick it up. | failure + field named + command_id echoed; state unchanged (read back) |

**Rejected scenarios:** always read the value back afterwards — a reject that still half-applied the change is the worst bug class.


**Before you start:** read [WHAT_YOU_NEED.md](WHAT_YOU_NEED.md) — equipment, pre-test state, risks and recovery for `set_eSimConfig`.
