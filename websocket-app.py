from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import Set

app = FastAPI()

# Allow all origins for testing purposes.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

websocket_clients: Set[WebSocket] = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.add(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            # Process the message if needed
            # Send the message to all connected clients
            for client in websocket_clients:
                await client.send_text(message)
    except WebSocketDisconnect:
        websocket_clients.remove(websocket)
