import asyncio
import websockets
from ipconfig import IP

async def transmit():
    uri = f"ws://{IP}:8765"  # Adjust the URI based on your server's host and port
    print(f"Connected to {uri}")
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                data = input("Enter data (or type 'exit' to stop): ")

                if data.lower() == 'exit':
                    break

                await websocket.send(data)
                print(f'Client Sent: {data}')

        except websockets.ConnectionClosedError:
            print("Connection closed. Retrying...")

if __name__ == "__main__":
    asyncio.run(transmit())
