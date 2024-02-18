import asyncio
import websockets
from ipconfig import IP

async def receive(websocket):
    data = await websocket.recv()
    print(f'Server Received: {data}')
    
async def main():
    async with websockets.serve(receive, IP, 8765):
        await asyncio.Future() #Run forever
        
if __name__ == "__main__":
    asyncio.run(main())