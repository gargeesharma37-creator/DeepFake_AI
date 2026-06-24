from preprocess_audio import extract_mfcc

audio_path = r"D:\DeepFake_AI\datasets\audio\LA\ASVspoof2019_LA_train\flac\LA_T_1000137.flac"

features = extract_mfcc(audio_path)

print(features)
print()
print("Number of features:", len(features))