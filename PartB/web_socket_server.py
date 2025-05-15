import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WebSocketServer")

clients = set()


async def chat_handler(websocket):
    clients.add(websocket)
    print(f"New client connected. Total clients: {len(clients)}")

    try:
        async for message in websocket:
            print(f"Server received: {message}")
            # Create a list of clients to remove (if any are closed)
            to_remove = set()

            for client in clients:
                try:
                    # Try sending to all clients including sender
                    await client.send(message)
                    print(f"Sent to client: {message}")
                except:
                    # Mark disconnected clients for removal
                    to_remove.add(client)

            # Remove any disconnected clients
            for client in to_remove:
                clients.remove(client)
                print(f"Removed disconnected client")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        clients.discard(websocket)
        print(f"Client disconnected. Total clients: {len(clients)}")

async def start_websocket_server(host="localhost", port=8765):
    server = await websockets.serve(
        chat_handler,  # Note: we're passing just the handler function now
        host,
        port,
        ping_interval=None,
        ping_timeout=None
    )
    logger.info(f"WebSocket server started on ws://{host}:{port}")
    return server


if __name__ == "__main__":
    asyncio.run(start_websocket_server())