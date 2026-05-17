# Port Scanner

A custom TCP port scanner with service fingerprinting and OS detection, built in Python. This project was built from scratch to demonstrate understanding of low-level networking concepts including the TCP handshake, raw packet crafting, async concurrency, and service banner grabbing.

---

## How It Works

The scanner operates across five modules:

**Scanning** - uses Python's native asyncio `open_connection()` to perform concurrent TCP connect scans across a port range. A semaphore limits concurrency to avoid overwhelming the target.

**Service Fingerprinting** - for each open port, the scanner attempts to grab the service banner by reading the initial response. For HTTP ports (80, 8080) it sends a GET request first to prompt a response.

**OS Detection** - sends an ICMP echo request using Scapy and reads the TTL value from the response. Different operating systems use different default TTL values: Linux uses 64, Windows uses 128, and Cisco devices use 255.

**Reporting** - results are output to the terminal in a structured format, or written to a file if specified.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ambeRAWR/port-scanner.git
cd port-scanner
```

Install dependencies:

```bash
pip install scapy
```
Note: sudo is required to run the scanner as Scapy needs raw socket access for OS detection.
---

## Usage

Basic scan of the default port range (1-1000):

```bash
sudo python3 main.py 192.168.1.1
```

Scan a specific port range:

```bash
sudo python3 main.py 192.168.1.1 -p 1-10000
```

Scan a single port:

```bash
sudo python3 main.py 192.168.1.1 -p 8080
```

Use stealth timing:

```bash
sudo python3 main.py 192.168.1.1 -t stealth
```

Save output to a file:

```bash
sudo python3 main.py 192.168.1.1 -o results.txt
```

Full options:

```
positional arguments:
  target                Target IP address

optional arguments:
  -p, --ports           Port range to scan (default: 1-1000)
  -t, --timing          Timing template: normal/stealth/aggressive (default: normal)
  -d, --decoys          Comma separated list of decoy IPs
  -o, --output          Output file path, defaults to terminal
```

---

## Known Limitations

- **Firewall interference** -- targets with aggressive DROP policies may produce inconsistent results, as simultaneous connection attempts can be silently dropped. This is expected behaviour when scanning hardened targets.
- **Connect scan vs SYN scan** -- the scanner uses a full TCP connect scan rather than a raw SYN scan. This is faster and does not require raw socket access for the scanning itself, but is less stealthy and will appear in target logs.
- **OS detection** -- TTL based OS detection is a best-effort heuristic. Administrators can modify default TTL values, and high hop counts can make results unreliable.

---

## Legal Disclaimer

This tool is intended for use on networks and systems you own or have explicit written permission to test. Unauthorised port scanning may be illegal in your jurisdiction. The author accepts no responsibility for misuse.
