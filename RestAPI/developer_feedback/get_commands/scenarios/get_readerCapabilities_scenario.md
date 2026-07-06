# `get_readerCapabilities` — schema clarification (scenario)

**Command:** `get_readerCapabilities`  
**REST endpoint:** `GET /cloud/readerCapabilities`  
**Reference:** `openAPISpec.yaml`  

Hi,

I reviewed the `get_readerCapabilities` command for `/cloud/readerCapabilities` in `openAPISpec.yaml`.

When I call `GET /cloud/readerCapabilities`, the MQTT `get_readerCapabilities` command in the Zebra IoT Connector (IoTC) documentation on the Zebra portal returns richly-typed entries, e.g.:

```json
{
  "capabilities": {
    "antennas": [ { "port": 1, "type": "external" }, { "port": 5, "type": "internal" } ],
    "supportedPowerSource": ["POWERBRICK", "POE", "POE+"],
    "networkInterfaces": [ { "type": "ETHERNET", "ipAssignment": ["STATIC", "DHCP"], "ipStack": ["IPv4", "IPv6"] } ]
  }
}
```

But `openAPISpec.yaml` types these as free-form objects:

```yaml
antennas:
  items:
    type: object          # no properties → port/type undocumented
supportedPowerSource:
  items:
    type: object          # Zebra IoTC docs: array of string
networkInterfaces:
  type: object
  properties: {}          # Zebra IoTC docs: array of interface objects
```

So Swagger cannot tell a consumer that `antennas[].type` is `external`/`internal`, or that `supportedPowerSource` is a list of strings.

Could you please type these arrays with their real item shapes (and add the enums such as `antennas[].type: [external, internal]`, `ipAssignment: [STATIC, DHCP]`, `ipStack: [IPv4, IPv6]`)? The example also uses unrealistic values (`numGPIs: 491980688`, `networkInterfaces: null`) — please align it with a real reader response.
