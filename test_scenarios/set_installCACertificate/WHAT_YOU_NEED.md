# set_installCACertificate — what you should have before testing

## Risk level: 🟠 MEDIUM — a corrupt CA can break TLS verification chains

## Equipment & access you need
- A test CA certificate in PEM (generate with openssl: `openssl req -x509 -newkey rsa:2048 ...`)
- Nothing production-critical relying on the CA store of this bench reader

## Capture BEFORE the first test (so you can restore)
- Current CA list (via get_certs / REST GET /cloud/certificates) saved

## If it goes wrong — recovery
1. del_CACertificate for anything you installed
2. Verify the original CA list matches your snapshot afterwards

## Command-specific notes
- invalid-PEM probe: reader must reject at parse time — if it stores garbage and TLS fails later, that is the bug to report.
- reinstall-same-name: replace vs reject vs duplicate must be consistent and documented.
