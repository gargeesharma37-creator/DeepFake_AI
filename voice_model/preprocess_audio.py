import librosa
import numpy as np


def extract_mfcc(audio_path):
    """
    Extract MFCC features from audio file
    """

    audio, sample_rate = librosa.load(
        audio_path,
        sr=None
    )

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=13
    )

    return np.mean(mfcc.T, axis=0)