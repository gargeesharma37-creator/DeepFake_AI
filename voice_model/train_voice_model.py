import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from dataset import load_protocol_file
from preprocess_audio import extract_mfcc
import joblib

protocol_path = r"D:\DeepFake_AI\datasets\audio\LA\ASVspoof2019_LA_cm_protocols\ASVspoof2019.LA.cm.train.trn.txt"

audio_folder = r"D:\DeepFake_AI\datasets\audio\LA\ASVspoof2019_LA_train\flac"

df = load_protocol_file(protocol_path)

X = []
y = []

for index, row in df.head(500).iterrows():

    file_name = row["file_name"]
    label = row["label"]

    audio_path = os.path.join(
        audio_folder,
        file_name + ".flac"
    )

    try:

        features = extract_mfcc(audio_path)

        X.append(features)

        if label == "bonafide":
            y.append(0)
        else:
            y.append(1)

    except Exception as e:

        print("Error:", file_name)

print("Samples:", len(X))
print("Labels:", len(y))

X = np.array(X)
y = np.array(y)
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

print("Accuracy:", accuracy)
print("X shape:", X.shape)
print("y shape:", y.shape)
joblib.dump(
    model,
    r"D:\DeepFake_AI\saved_models\voice_model.pkl"
)
print("Model saved successfully")