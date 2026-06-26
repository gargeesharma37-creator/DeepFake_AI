from fastapi import FastAPI, UploadFile, File
from backend.voice_detector import predict_voice
from voice_model.preprocess_audio import extract_mfcc
import shutil
from backend.video_detector import detect_video
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount(
    "/frontend",
    StaticFiles(directory=r"D:\DeepFake_AI\frontend"),
    name="frontend"
)
@app.get("/")
def home():
    return FileResponse(
        r"D:\DeepFake_AI\frontend\index.html"
    )


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    print("PREDICT API HIT")
    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    features = extract_mfcc(temp_file)
    result = predict_voice(features)

    return result
    
@app.post("/predict-video")
async def predict_video_api(file: UploadFile = File(...)):

    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_video(temp_file)

   
    return result
