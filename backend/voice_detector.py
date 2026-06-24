import joblib

model = joblib.load(
    r"D:\DeepFake_AI\saved_models\voice_model.pkl"
)

def predict_voice(features):
    prediction = model.predict([features])

    if prediction[0] == 0:
        return "BONAFIDE"
    else:
        return "SPOOF"