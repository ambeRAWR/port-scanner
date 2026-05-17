import argparse
import sys
import utils

parser = argparse.ArgumentParser(description="Custom Port Scanner by ambeRAWR!") #defines argyments for program usage
parser.add_argument("target", help="Target IP address")
parser.add_argument("-p", "--ports", default="1-1000", help="Port range to scan")
parser.add_argument("-t", "--timing", default="normal", choices=["normal", "stealth", "aggressive"],help="Alternative timing/aggression template: normal/stealth/agressive")
parser.add_argument("-d", "--decoy", default=None, help="Comma separated list of decoy IPs e.g. 192.168.1.5,192.168.1.6")
parser.add_argument("-o", "--output", default=None, help="Output file path, defaults to terminal")
args = parser.parse_args()

def main(targets, port_range, decoyIPs):
    if utils.validate_ip(targets):
        if utils.validate_ports(port_range):
            if decoyIPs!=None:
                decoy_list = decoyIPs.split(",")
                for decoy in range(len(decoy_list)):
                    if utils.validate_ip(decoy_list[decoy]):
                        continue
                    else:
                        raise ValueError("decoy IP range is incorrectly formatted")
    else:
        raise ValueError("target IP format incorrect")

if __name__ == "__main__":
    try:
        main(args.target, args.ports, args.decoy)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit()
