import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model(
    r"D:\DeepFake_AI\saved_models\video_model.keras"
)

def predict_video(video_path):

    cap = cv2.VideoCapture(video_path)

    predictions = []

    frame_number = 0

    while True:

        success, frame = cap.read()

        print("Success:", success)

        if not success:
           break

        frame_number += 1

        

        frame = cv2.resize(frame, (128, 128))

        frame = frame / 255.0

        frame = np.expand_dims(frame, axis=0)
        print("Frame shape:", frame.shape)
        prediction = model.predict(
            frame,
            verbose=0
        )[0][0]
        print("Prediction value:", prediction)
        predictions.append(prediction)

    cap.release()

    print("Predictions collected:", len(predictions))

    if len(predictions) == 0:

      return {
        "prediction": "Unable to Analyze"
    }
    avg_prediction = np.mean(predictions)

    fake_percentage = round(
        avg_prediction * 100,
        2
    )

    real_percentage = round(
        (1 - avg_prediction) * 100,
        2
    )

    if avg_prediction > 0.5:

        label = "FAKE"

    else:

        label = "REAL"

    return {
        "prediction": label,
        "real_percentage": real_percentage,
        "fake_percentage": fake_percentage
    }