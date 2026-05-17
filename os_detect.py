from scapy.all import IP, ICMP, sr1


def detect_os(target):
    response = sr1(IP(dst=target)/ICMP(), timeout=2)
    if response != None:
        TTL = response[IP].ttl
        if TTL in range(1,65):
            return 'Linux'
        if TTL in range (65, 129):
            return 'Windows'
        if TTL in range (129, 256):
            return 'Cisco'
    else:
        return "Unknown"
