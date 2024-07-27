from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.utils import center, find_box_contours
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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

    shape = np.frombuffer(await soc.receive_bytes(), dtype=np.uint8)
    canvas = np.zeros(shape, np.uint8)

    try:
        while True:
            pixel = np.frombuffer(await soc.receive_bytes(), dtype=np.uint8)

            if not len(pixel):
                canvas = np.zeros(shape, np.uint8)
                continue
            else:
                canvas[pixel[0]][pixel[1]] = 1
            
            r = []
            for x, y, w, h in find_box_contours(canvas):
                s = canvas[y:y+h,x:x+w]
                s = center(s)

                r.append((x, y+h, str(network(np.expand_dims(s, 0), training=False).numpy().argmax())))

            response = ''.join(p[2] for p in sorted(r, key=lambda t: t[0]))

            await soc.send_text(response)
    except WebSocketDisconnect:
        ...
