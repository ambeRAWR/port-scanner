import argparse
import ipaddress
import sys

parser = argparse.ArgumentParser(description="Custom Port Scanner by ambeRAWR!") #defines argyments for program usage
parser.add_argument("target", help="Target IP address")
parser.add_argument("-p", "--ports", default="1-1000", help="Port range to scan")
parser.add_argument("-t", "--timing", default="normal", choices=["normal", "stealth", "aggressive"],help="Alternative timing/aggression template: normal/stealth/agressive")
parser.add_argument("-d", "--decoy", default=None, help="Comma separated list of decoy IPs e.g. 192.168.1.5,192.168.1.6")
parser.add_argument("-o", "--output", default=None, help="Output file path, defaults to terminal")
args = parser.parse_args()

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_ports(port_string): #checks format legitimacy of port range inputs
    port_numbers = port_string.split("-")
    if len(port_numbers)!=2:
        raise ValueError("improper port input syntax: port must include 2 numbers")
    else:
        if port_numbers[0].isdigit() and port_numbers[1].isdigit():
            port_numbers[0] = int(port_numbers[0])
            port_numbers[1] = int(port_numbers[1])
            if port_numbers[0]>port_numbers[1]:
                raise ValueError("first port in range must be smaller than second")
            else:
                if (port_numbers[0]>0 and port_numbers[0]<65535) and (port_numbers[1]>0 and port_numbers[1]<65535):
                    return True
                else:
                    raise ValueError("ports not in possible port range")
        else:
            raise ValueError("port input must be numeric")




def main(targets, port_range, decoyIPs):
    if validate_ip(targets):
        if validate_ports(port_range):
            if decoyIPs!=None:
                decoy_list = decoyIPs.split(",")
                for decoy in range(len(decoy_list)):
                    if validate_ip(decoy_list[decoy]):
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
