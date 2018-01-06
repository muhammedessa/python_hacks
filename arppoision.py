
from scapy.layers.l2 import ARP, Ether, sniff

DB = {}
def scarpwatch_callback(pkt):
    if ARP in pkt:
        ip,mac = pkt[ARP].psrc, pkt[ARP].hwsrc
        if ip in DB:
            if mac != DB[ip]:
                if Ether in pkt:
                    target = pkt[Ether].dst
                else:
                    target = "%s?" % pkt[ARP].pdst
                return "poisoning attack: target=%s victim=%s attacker=%s" %  (target, ip, mac)
        else:
            DB[ip]=mac
            return "Oh !!!! gathering info from router %s=%s" % (mac,ip)

sniff(store=0, prn=scarpwatch_callback)


