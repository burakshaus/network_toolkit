import socket
import os 

def start_file_server(host='0.0.0.0', port=5001,save_dir='received_files'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(1)
        print(f"Server listening on {host}:{port}...")

        conn, addr = server.accept()
        print(f"Accepted connection from {addr}")

        with conn:
            filename = conn.recv(1024).decode()
            filepath = os.path.join(save_dir, filename)

            with open(filepath, 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)

        print(f"File received and saved as {filepath}")
