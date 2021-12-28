from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            # parse the incoming string to make any sense
            await manager.broadcast(f"{client_id} says: {data}")

    except WebSocketDisconnect:

        manager.disconnect(websocket)

        await manager.broadcast(f"Client #{client_id} left the chat")


# add a @list command to show all users


# add @dm capabilities
# add @room? All rooms?
# send personal messages (i.e. differentiate between the sender vs. other users)
# add http route with usage instructions
# add http route to list users

# TODO: initially store connections in List then require students to convert to Dictionary to associate client IDs
# TODO: OR start out with connections Dictionary to not send them down wrong path
# TODO: OR (best I think) start with List and make task to explicitly convert to Dictionary

# ROGER: show the conversion process from List to Dictionary - give them the @list functionality
