#!/usr/bin/env python

#Gets router bgp config from the device, then loads a file with the new bgp config we want and we
#compute the difference

from pyFG import FortiOS
import sys

if __name__ == "__main__":
    with open("candidate.conf", "r") as f:
        candidate = f.read()

    hostname = sys.argv[1]

    d = FortiOS(hostname, vdom="vpn")
    d.open()
    d.load_config("router bgp", empty_candidate=True)
    d.load_config(config_text=candidate, in_candidate=True)
    d.close()

    print("This is the diff of the configs:")
    print(d.compare_config(text=True))
    print("--------------------")
    print("This is how to reach the desired state:")
    print(d.compare_config())