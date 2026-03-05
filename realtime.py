from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import asyncio

app = FastAPI()

class ConnectionManager:

    def __init__(self):
        self.connections: List[WebSocket] = []
        self.lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        async with self.lock:
            self.connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        async with self.lock:
            if websocket in self.connections:
                self.connections.remove(websocket)

    async def broadcast(self, message: dict):
        async with self.lock:
            dead = []
            print(f"Broadcasting message: {message}")
            for ws in self.connections:
                try:
                    await ws.send_json(message)
                    print(f"Broadcasting message: {message}")
                except:
                    dead.append(ws)

            for ws in dead:
                self.connections.remove(ws)


manager = ConnectionManager()


@app.websocket("/ws/admin")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@app.post("/broadcast")
async def broadcast(message: dict):
    print(f"Received message to broadcast: {message}")
    await manager.broadcast(message)

    return {"status": "sent"}
