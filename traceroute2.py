from scapy.layers.inet import traceroute

res4,unans=traceroute(["www.google.com", "www.facebook.com", "www.yahoo.com"])
res4.show( )