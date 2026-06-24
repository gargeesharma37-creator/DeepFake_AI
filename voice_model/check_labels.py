from dataset import load_protocol_file

protocol_path = r"D:\DeepFake_AI\datasets\audio\LA\ASVspoof2019_LA_cm_protocols\ASVspoof2019.LA.cm.train.trn.txt"

df = load_protocol_file(protocol_path)

print(df["label"].value_counts())