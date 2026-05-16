from scapy.all import IP, TCP, sr1
import asyncio

async def scan_port(target,port):
    response = await asyncio.get_event_loop().run_in_executor(
        None, lambda: sr1(IP(dst=target) / TCP(dport=port, flags="S"), timeout=1)
    )
    if response is None:
        return "filtered"
    else:
        flag = response[TCP].flags 
        if flag == "SA":
            return "open"
        elif flag == "R":
            return "closed"
        else:
            return "malformed"

async def scan_range(target,start_port,end_port):
    ports=[]
    for port in range(start_port, end_port + 1):
        ports.append(scan_port(target, port))
    results = await asyncio.gather(*ports)
    return results

