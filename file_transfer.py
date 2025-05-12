import os
import socket

def send_file(file_path, server_ip, server_port=5001):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            s.send(os.path.basename(file_path).encode())

            with open(file_path, 'rb') as f:
                while chunk:= f.read(1024):
                    s.send(chunk)

        return f"File {file_path} sent successfully."

    except Exception as e:
        return f"Error: {e}"

