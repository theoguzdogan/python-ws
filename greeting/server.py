import asyncio
import websockets
from ipconfig import IP

async def hello(websocket):
    name = await websocket.recv()
    print(f'Server Received: {name}')
    greeting = f'Hello {name}!'
    
    await websocket.send(greeting)
    print(f'Server Sent: {greeting}')
    
async def main():
    async with websockets.serve(hello, IP, 8765):
        await asyncio.Future() #Run forever
        
if __name__ == "__main__":
    asyncio.run(main())