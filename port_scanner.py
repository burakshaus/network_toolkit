import socket

def scan_ports(host, start_port, end_port, timeout=0.5):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((host, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port)
                    except OSError as e:
                        service = "Unknown"
                    open_ports.append(port)
        except Exception:
            continue
    return open_ports