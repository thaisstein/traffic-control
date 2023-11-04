from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi import FastAPI, Depends, HTTPException, Form
import asyncio
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
import subprocess
import threading, websockets
from typing import Set
import json

from fastapi.middleware.cors import CORSMiddleware

from firstconsumer import start_first_consumer
import httpx
from websocket import (
    send_update_to_clients,
    start_rabbitmq_consumer,
    send_periodic_haha_messages,
)

def run_rabbitmq_consumer():
    start_first_consumer()

app = FastAPI()

# Allow all origins for testing purposes.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

websocket_clients = set()
is_connected = False

import json

# Store WebSocket connections in a set
connected_websockets = set()

# Define a WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_websockets.add(websocket)
    
    try:
        while True:
            message = await websocket.receive_text()
            # Process the received message here or send it to RabbitMQ if needed
            print(f"RECEIVED message: {message}")
    except WebSocketDisconnect:
        connected_websockets.remove(websocket)


@app.get("/", response_class=HTMLResponse)
def get_subscribe_page(request: Request):
    return FileResponse("firstpage.html")

# Serve the page
@app.get("/subscribe", response_class=HTMLResponse)
def get_subscribe_page(request: Request):
    return FileResponse("subscription.html")

@app.post("/subscribe")
async def subscribe_to_rabbitmq():

    # Run emit_log.py to subscribe to RabbitMQ
    try:
        #asyncio.create_task(run_rabbitmq_consumer())
        rabbitmq_thread = threading.Thread(target=run_rabbitmq_consumer)
        rabbitmq_thread.start()
        #_process = subprocess.Popen(["python3", "firstconsumer.py"])
        return FileResponse("subscription.html")

    #acho q aqui que vai as condicoes da BD
    except Exception as e:
        return FileResponse("subscriptionerror.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    


