import os

from dataset import load_protocol_file
from preprocess_audio import extract_mfcc


protocol_path = r"D:\DeepFake_AI\datasets\audio\LA\ASVspoof2019_LA_cm_protocols\ASVspoof2019.LA.cm.train.trn.txt"

audio_folder = r"D:\DeepFake_AI\datasets\audio\LA\ASVspoof2019_LA_train\flac"

df = load_protocol_file(protocol_path)

for index, row in df.head(5).iterrows():

    file_name = row["file_name"]
    label = row["label"]

    audio_path = os.path.join(
        audio_folder,
        file_name + ".flac"
    )

    features = extract_mfcc(audio_path)

    print(file_name)
    print(label)
    print(features)
    print("-" * 50)