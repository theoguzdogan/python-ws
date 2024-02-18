import asyncio
import websockets
from ipconfig import IP

async def transmit():
    uri = f"ws://{IP}:8765"  # Adjust the URI based on your server's host and port

    async with websockets.connect(uri) as websocket:
        data = input("Enter data: ")
        
        await websocket.send(data)
        print(f'Client Sent: {data}')
        
if __name__ == "__main__":
    asyncio.run(transmit())