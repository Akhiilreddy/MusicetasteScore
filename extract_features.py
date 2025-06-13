
import os
import librosa
import numpy as np

def extract_all_features(audio_dir):
    features = []
    for file in os.listdir(audio_dir):
        if file.endswith(".wav"):
            path = os.path.join(audio_dir, file)
            y, sr = librosa.load(path, sr=None)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            mean = np.mean(mfcc.T, axis=0)
            features.append(mean)
    return np.array(features)
