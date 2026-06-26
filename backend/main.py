from fastapi import FastAPI, UploadFile, File
from backend.voice_detector import predict_voice
from voice_model.preprocess_audio import extract_mfcc
import shutil
from backend.video_detector import detect_video

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "DeepFake AI Backend Running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    print("PREDICT API HIT")
    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    features = extract_mfcc(temp_file)

    result = predict_voice(features)

    return {
        "prediction": result
    }
@app.post("/predict-video")
async def predict_video_api(file: UploadFile = File(...)):

    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_video(temp_file)

   
    return {
    "prediction": result
}