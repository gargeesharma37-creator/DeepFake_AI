from fastapi import FastAPI
from backend.voice_detector import predict_voice

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "DeepFake AI Backend Running"
    }

@app.get("/predict")
def predict():
    
    sample_features = [
        -247.76,
        77.11,
        -10.09,
        29.62,
        -6.38,
        -4.65,
        -17.60,
        -14.64,
        -11.31,
        -21.16,
        -8.75,
        -11.13,
        -14.56
    ]

    result = predict_voice(sample_features)

    return {
        "prediction": result
    }