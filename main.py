from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi import FastAPI, Depends, HTTPException, Form
import asyncio
from websocket import WebSocketState
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
import subprocess
import threading
from typing import Set

from fastapi.middleware.cors import CORSMiddleware

from firstconsumer import start_consumer
import httpx
from websocket import (
    send_update_to_clients,
    start_rabbitmq_consumer,
    send_periodic_haha_messages,
)

def run_rabbitmq_consumer():
    start_consumer()

app = FastAPI()

# Allow all origins for testing purposes.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

websocket_clients: Set[WebSocket] = set()
# Store connected WebSocket clients
websocket_clients = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_clients.add(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            # You can process the message here if needed
            # Ensure the WebSocket connection is open before sending
            if websocket.client_state == WebSocketState.CONNECTED:
                await websocket.send_text("Received your message: " + message)
    except WebSocketDisconnect:
        websocket_clients.remove(websocket)

@app.get("/", response_class=HTMLResponse)
def get_subscribe_page(request: Request):
    # HTML form to subscribe
    return FileResponse("firstpage.html")


@app.post("/subscribe")
async def subscribe_to_rabbitmq():

    # Run emit_log.py to subscribe to RabbitMQ
    try:
        rabbitmq_thread = threading.Thread(target=run_rabbitmq_consumer)
        rabbitmq_thread.start()
       # _process = subprocess.Popen(["python3", "firstconsumer.py"])
        return FileResponse("subscription.html")

    #acho q aqui que vai as condicoes da BD
    except Exception as e:
        return FileResponse("subscriptionerror.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


