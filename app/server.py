# from crypt import methods
from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn
from app.mod.prediction import *
from pathlib import Path
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from gtts import gTTS


path = Path(__file__).parent

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/app", StaticFiles(directory="app"), name="app")


@app.route('/')
async def homepage(request):
    html_file = path / 'view' / 'index.html'
    return HTMLResponse(html_file.open().read())

@app.route('/analyze', methods=['POST'])
async def analyze(req):
    img_data = await req.form()
    img_bytes = await (img_data['file'].read())
    
    image = read_image(img_bytes)
    predictions = predict(image)
    print(predictions)
    audio = gTTS(text=predictions, lang="en", slow=False)
    audio.save("app/example.mp3")
    return JSONResponse({'result': str(predictions)})

# if __name__ == "__main__":
#     uvicorn.run(app, port=8090, host='0.0.0.0')