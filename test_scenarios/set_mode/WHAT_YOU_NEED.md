# set_mode — what you should have before testing

## Risk level: 🟠 MEDIUM — wrong RF settings stop tag reads but never brick the reader

## Equipment & access you need
- 1+ RFID tags of known type (Gen2, and Gen2X-capable tags for GEN2X protocol tests)
- Antennas connected on the ports you list (testing port 99 needs nothing — it must just fail)
- Regulatory awareness: transmit power must be legal for your region; use a shielded box if possible

## Capture BEFORE the first test (so you can restore)
- `get_mode` response saved — your restore payload
- Current read performance baseline (tags/second on a known tag population)

## If it goes wrong — recovery
1. Replay the saved get_mode snapshot, or send the documented default mode example
2. `stop` then `start` inventory to confirm reads resumed

## Command-specific notes
- THE key probe here: transmitPower scalar vs array (known schema/example conflict) — record which form firmware accepts.
- After every ACCEPTED change, verify reads still happen (start + watch tag events).
