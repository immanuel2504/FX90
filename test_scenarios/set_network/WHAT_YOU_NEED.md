# set_network — what you should have before testing

## Risk level: 🔴 HIGH — a bad network config can take the reader OFFLINE permanently over the network path you are using

## Equipment & access you need
- FXR90 reader on a bench network you control (never a production reader)
- A SECOND access path that does not depend on the interface under test: USB/serial console, or the other interface (test eth0 changes over Wi-Fi and vice versa)
- DHCP server on the bench network + a reserved static IP range
- Wi-Fi access point you control (for mlan0 tests) supporting WPA2-Personal AND WPA2/WPA3-Enterprise
- A RADIUS server (e.g. FreeRADIUS) for the 802.1x TLS/TTLS/PEAP variants + client certificates installed on the reader beforehand
- For WAN/hotspot/bluetooth variants: SIM/eSIM and a BT test device

## Capture BEFORE the first test (so you can restore)
- `get_network` full response (save to file) — this is your restore payload
- Current IP/mask/gateway/DNS of every interface, and which interface your test session uses

## If it goes wrong — recovery
1. Reconnect over the second access path (console or the other interface)
2. Replay the saved `get_network` snapshot via `set_network`
3. Worst case: factory network reset per FXR90 hardware manual (reset button)

## Command-specific notes
- Run DHCP↔static transitions in both directions.
- After each 802.1x variant, confirm the reader actually re-authenticated (check RADIUS logs), not just accepted the config.
