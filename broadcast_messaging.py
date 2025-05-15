import socket
import threading
import sys

BROADCAST_PORT = 37020

def start_receiver(callback):
    def listen():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.bind(('', BROADCAST_PORT))
                while True:
                    data, addr = sock.recvfrom(1024)
                    callback(f"{addr[0]}: {data.decode()}")
        except OSError as e:
            if e.errno == 48:  # macOS specific: Address already in use
                print(f"[ERROR] Port {BROADCAST_PORT} is already in use. Is another instance running?")
            else:
                print(f"[ERROR] Socket error: {e}")
            sys.exit(1)

    thread = threading.Thread(target=listen, daemon=True)
    thread.start()

def send_broadcast_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(message.encode(), ('<broadcast>', BROADCAST_PORT))
