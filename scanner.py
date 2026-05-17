from scapy.all import IP, TCP, sr1
import asyncio

async def scan_port(target, port, semaphore):
    async with semaphore:
        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(target, port),
                timeout=1
            )
            writer.close()
            await writer.wait_closed()
            return "open"
        except asyncio.TimeoutError:
            return "filtered"
        except ConnectionRefusedError:
            return "closed"
        except Exception:
            return "filtered"

async def scan_range(target,start_port,end_port):
    semaphore = asyncio.Semaphore(50)
    ports=[]
    for port in range(start_port, end_port + 1):
        ports.append(scan_port(target, port,semaphore))
    results = await asyncio.gather(*ports)
    return results

