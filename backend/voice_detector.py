import joblib

model = joblib.load(
    r"D:\DeepFake_AI\saved_models\voice_model.pkl"
)

def predict_voice(features):

    prediction = model.predict([features])[0]

    #probabilities = model.predict_proba([features])[0]

    if prediction == 0:
        return {
            "prediction": "BONAFIDE",
            "real_percentage": 100,
            "fake_percentage": 0
        }

    else:
        return {
            "prediction": "SPOOF",
            "real_percentage": 0,
            "fake_percentage": 100
        }