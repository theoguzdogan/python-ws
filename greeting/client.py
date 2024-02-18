import asyncio
import websockets
from ipconfig import IP

async def hello():
    uri = f"ws://{IP}:8765"  # Adjust the URI based on your server's host and port

    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        
        await websocket.send(name)
        print(f'Client Sent: {name}')
        
        greeting = await websocket.recv()
        
        print(f"Client Received: {greeting}")
        
if __name__ == "__main__":
    asyncio.run(hello())