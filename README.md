# ping-pwn
ICMP tunneling can be used to bypass firewalls rules through obfuscation of the actual traffic. Without proper deep packet inspection or log review, network administrators will not be able to detect this type of traffic through their network.

Work in progress

## Usage:
- Victim: ping.py <interface> <attacker IP>
- Attacker: pwn.py <interface> <victim IP>
