import os

AUDIO_EXTENSIONS = (".wav", ".flac", ".mp3")


def get_audio_files(folder_path):
    """
    Return all supported audio files inside a folder.
    """

    audio_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(AUDIO_EXTENSIONS):
                audio_files.append(
                    os.path.join(root, file)
                )

    return audio_files
import pandas as pd


def load_protocol_file(protocol_path):
    """
    Read ASVspoof protocol file and return labels.
    """

    columns = [
        "speaker_id",
        "file_name",
        "unused",
        "attack_type",
        "label"
    ]

    df = pd.read_csv(
        protocol_path,
        sep=" ",
        header=None,
        names=columns
    )

    return df