import ipaddress

def validate_ip(ip): #validates IPs
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
