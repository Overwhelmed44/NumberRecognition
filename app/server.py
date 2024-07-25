from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.utils import center
import numpy as np

app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'))

from app import network


@app.get('/')
@app.get('/index')
async def index():
    return FileResponse('app/canvas.html')


@app.websocket('/ws')
async def ws(soc: WebSocket):
    await soc.accept()

    canvas = np.zeros((28, 28), np.uint8)

    try:
        while True:
            pixel = np.frombuffer(await soc.receive_bytes(), dtype=np.uint8)

            if not len(pixel):
                canvas = np.zeros((28, 28), np.uint8)
                continue
            else:
                canvas[pixel[0]][pixel[1]] = 1
            
            predict = network(np.expand_dims(center(canvas), 0), training=False)[0].numpy()

            response = {k: str(v) for k, v in enumerate(predict)}
            response.update(l=str(predict.argmax()))

            await soc.send_json(response)
    except WebSocketDisconnect:
        ...
