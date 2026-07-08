# set_config — what you should have before testing

## Risk level: 🔴 HIGH — READER-GATEWAY changes can disconnect the reader from its cloud/data path

## Equipment & access you need
- Bench reader + a test MQTT broker you control (e.g. mosquitto on your laptop)
- For endpoint variants: reachable test endpoints per type — MQTT broker, HTTP POST receiver (e.g. `python -m http.server` + logger), TCP socket listener, WebSocket echo server, AWS IoT Core / Azure IoT Hub test instances (or record CHECK results as 'endpoint unreachable' if not available)
- GPIO/LED tests: visual access to the reader's LEDs and a way to trigger GPI lines (button box / jumper wire)
- A tag in antenna range for TAG_READ event-action tests

## Capture BEFORE the first test (so you can restore)
- `get_config` full response saved to file — your restore payload
- Which broker/topic your OWN test session uses (do not clear the connection you are talking through!)

## If it goes wrong — recovery
1. If the data path died: your control channel usually still works — replay the saved get_config snapshot
2. If the control channel died too: reconnect over REST (PUT /cloud/config) with the snapshot
3. Keep the `set_config_data_clear` scenario for LAST — it wipes data connections

## Command-specific notes
- Thresholds (cpu/ram/flash) have NO schema bounds — probe 0/100/900 and record clamp vs reject.
- batching:null is a known schema/firmware ambiguity — record the exact response.
- Duplicate connection names must be rejected; if accepted, that is a bug.
