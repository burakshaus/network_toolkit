import platform
import subprocess
import threading

def ping(ip, results):
    command = ["ping", "-n" if platform.system() == "Windows" else "-c", "1", ip]
    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        results.append(ip)
    except subprocess.CalledProcessError:
        pass  # host did not respond


def scan_network(base_ip):
    if not base_ip.endswith('.'):
        base_ip += '.'

    threads = []
    active_ips = []

    for i in range(1, 255):
        ip = f"{base_ip}{i}"
        thread = threading.Thread(target=ping, args=(ip, active_ips))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return active_ips
