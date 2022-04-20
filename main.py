import json, datetime
import asyncio
from fastapi import FastAPI
from fastapi import Request
from fastapi import WebSocket
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

import random
randomlist = []
for i in range(0,100):
    n = random.randint(1,30)
    randomlist.append(n)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    i = 0
    while True:
        struct = {
            "time" : "",
            "data" : 0
        }
        await asyncio.sleep(0.5)
        struct["time"] = str(datetime.datetime.now())
        struct["data"] = randomlist[i]
        i += 1
        print(f"Sending: {struct}")
        await websocket.send_json(json.dumps(struct))
        
@app.get("/favicon.ico")
def icon():
    return FileResponse("templates/icon.png")