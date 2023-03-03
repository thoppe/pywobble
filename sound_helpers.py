import pyaudio
import torch
import numpy as np


def torch2numpy(sample):
    if torch.is_tensor(sample):
        sample = sample.detach().cpu().numpy().astype(np.float32)
    return sample


def play_sample(sample, volume=0.5, fs=44100):
    sample = torch2numpy(sample)

    output_bytes = (volume * sample).tobytes()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = audio.open(
        format=pyaudio.paFloat32, channels=1, rate=fs, output=True
    )
    stream.write(output_bytes)

    stream.stop_stream()
    stream.close()


audio = pyaudio.PyAudio()
