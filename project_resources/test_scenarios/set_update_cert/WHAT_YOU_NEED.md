# set_update_cert — what you should have before testing

## Risk level: 🟠 MEDIUM — a bad cert breaks TLS connections that used the old one

## Equipment & access you need
- Test certificates: valid PFX/PEM (self-signed CA is fine), with and without password
- An HTTPS server hosting the cert files (python http.server + TLS, or any web server)
- Basic-auth protected URL for the auth variants
- Know which live connections currently use the cert type you overwrite

## Capture BEFORE the first test (so you can restore)
- `get_certs` response saved (names, types, expiry) — so you know what was installed

## If it goes wrong — recovery
1. Re-install the previous certificate from your archive
2. If a TLS link broke: fix cert first, then restart the affected connection via set_config

## Command-specific notes
- unreachable-URL probe: measure the timeout; >60s with no feedback is a usability bug.
- BASIC auth without options must fail BEFORE any network fetch is attempted.
