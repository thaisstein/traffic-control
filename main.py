from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi import FastAPI, Depends, HTTPException, Form
import asyncio
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
import subprocess
import httpx
from websocket import (
    send_update_to_clients,
    start_rabbitmq_consumer,
    send_periodic_haha_messages,
)

app = FastAPI()


        
@app.get("/", response_class=HTMLResponse)
def get_subscribe_page(request: Request):
    # HTML form to subscribe
    return FileResponse("firstpage.html")

@app.post("/subscribe")
async def subscribe_to_rabbitmq():
    # Run emit_log.py to subscribe to RabbitMQ
    try:
            # Run the emit log script as a separate process
       # emit_log_process = subprocess.Popen(["python", "emit_log.py"])

            # Run the firstconsumer script as a separate process
        firstconsumer_process = subprocess.Popen(["python", "firstconsumer.py"])
        return FileResponse("subscription.html")
    
    #acho q aqui que vai as condicoes da BD
    except Exception as e:
        return FileResponse("subscriptionerror.html")


    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

