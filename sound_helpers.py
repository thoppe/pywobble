import pyaudio


def play_sample(sample, volume=0.5, fs=44100):
    output_bytes = (volume * sample).tobytes()

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    stream.write(output_bytes)

    stream.stop_stream()
    stream.close()


audio = pyaudio.PyAudio()
