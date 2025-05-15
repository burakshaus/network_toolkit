import threading
import socketserver
import asyncio
from http.server import SimpleHTTPRequestHandler
from web_socket_server import start_websocket_server  # Import your WebSocket server function

# Function to run the HTTP server in a separate thread
def run_http_server():
    handler = SimpleHTTPRequestHandler
    http_port = 8080
    http_server = socketserver.TCPServer(("", http_port), handler)
    print(f"Starting HTTP server on http://localhost:{http_port}")
    http_server.serve_forever()

# Function to run the WebSocket server
async def run_websocket_server():
    print("Starting WebSocket server...")
    await start_websocket_server()

def main():
    # Start the HTTP server in a separate thread
    http_thread = threading.Thread(target=run_http_server, daemon=True)
    http_thread.start()

    # Create a new event loop and run the WebSocket server
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)  # Set the new event loop
    loop.create_task(run_websocket_server())

    # Run the event loop
    loop.run_forever()

if __name__ == "__main__":
    main()
