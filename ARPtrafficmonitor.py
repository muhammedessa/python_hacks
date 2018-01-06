
from scapy.layers.l2 import ARP, sniff


def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")
sniff(prn=arp_monitor_callback, filter="arp", store=0)

# ARP traffic monitor