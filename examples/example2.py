#!/usr/bin/env python
# Gets the router bgp config and prints it

from pyFG import FortiOS
import sys

if __name__ == "__main__":
    hostname = sys.argv[1]

    d = FortiOS(hostname, vdom="vpn")
    d.open()
    d.load_config("router bgp")
    d.close()

    for neighbor, config in d.running_config["router bgp"]["neighbor"].iterblocks():
        print(neighbor)
        print(f"   AS: {config.get_param('remote-as')}")
        print(f"   route-map-out: {config.get_param('route-map-out')}")
        print(f"   route-map-in: {config.get_param('route-map-in')}")
