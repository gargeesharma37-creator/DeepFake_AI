import joblib

model = joblib.load(
    r"D:\DeepFake_AI\saved_models\voice_model.pkl"
)

def predict_voice(features):

    prediction = model.predict([features])[0]

    probabilities = model.predict_proba([features])[0]

    real_percentage = round(
        probabilities[0] * 100,
        2
    )

    fake_percentage = round(
        probabilities[1] * 100,
        2
    )

    if prediction == 0:

        return {
            "prediction": "BONAFIDE",
            "real_percentage": real_percentage,
            "fake_percentage": fake_percentage
        }

    else:

        return {
            "prediction": "SPOOF",
            "real_percentage": real_percentage,
            "fake_percentage": fake_percentage
        }