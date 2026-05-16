import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP-Alt"
}

HTTP_PORTS = {80, 8080}

def grab_banner(target, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        banner = s.recv(1024)
        s.close()
        return banner.decode().strip()
    except socket.timeout:
        return None
    except ConnectionRefusedError:
        return None
    except Exception:
        return None


def probe_http(target, port):
    try:
        request = (
                f"GET / HTTP/1.1\r\n"#standard HTTP request. GET is the method, / is root of website. HTTP/1.1. is the version
                f"Host: {target}\r\n"#HTTP requires the server your asking for.the \r\n is a carriage return and newline.HTTP requires each header to end with these two characters
                f"\r\n" #2 mean its the end of the header, means http can send a response now.
            )
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))
        s.send(request.encode())
        banner = s.recv(1024)
        s.close()
        return banner.decode().strip()
    except socket.timeout:
        return None
    except ConnectionRefusedError:
        return None
    except Exception:
        return None

def fingerprint(target, port):
    if port in COMMON_PORTS:
        if port in HTTP_PORTS:
            probed = probe_http(target, port)
            if probed == None:
                return grab_banner(target, port)
            else:
                return probed
        else:
            return grab_banner(target, port)     
    else:         
        return None 
