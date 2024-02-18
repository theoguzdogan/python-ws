import asyncio
import websockets
from ipconfig import IP

async def receive(websocket, path):
    try:
        data = await websocket.recv()
        print(f'Server Received: {data}')
    except websockets.ConnectionClosedOK:
        print("Client connection closed gracefully")
    except websockets.ConnectionClosedError:
        print("Client connection closed unexpectedly")

async def main():
    server = await websockets.serve(receive, IP, 8765)
    print(f"Server started. Listening on {IP}:8765")

    try:
        await server.wait_closed()  # Run forever
    except KeyboardInterrupt:
        print("Server shutting down...")

if __name__ == "__main__":
    asyncio.run(main())
