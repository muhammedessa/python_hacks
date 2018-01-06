from scapy.layers.inet import traceroute

res4,unans=traceroute(["127.0.0.1", "10.0.2.1", "192.168.0.1"])
res4.show( )
res4.graph()