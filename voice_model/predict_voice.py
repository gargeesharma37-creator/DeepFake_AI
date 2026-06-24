import joblib
from preprocess_audio import extract_mfcc

model = joblib.load("saved_models/voice_model.pkl")

audio_path = r"D:\DeepFake_AI\datasets\audio\LA\ASVspoof2019_LA_train\flac\LA_T_1000137.flac"

features = extract_mfcc(audio_path)

prediction = model.predict([features])
probabilities = model.predict_proba([features])
confidence = max(probabilities[0]) * 100
if prediction[0] == 0:
    print("Prediction: BONAFIDE (REAL)")
else:
    print("Prediction: SPOOF (FAKE)")

print("Confidence:", round(confidence, 2), "%")