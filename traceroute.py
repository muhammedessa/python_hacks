from scapy.layers.inet import traceroute

res,unans = traceroute("8.8.8.8", dport=443, maxttl=5)