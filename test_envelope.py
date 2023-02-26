import numpy as np
from oscillators import SquareWave, TriangleWave, SawToothWave, SineWave

fs = 44100  # sampling rate, Hz, must be integer
duration = 1.50  # in seconds, may be float
freq = 440.0  # sine frequency, Hz, may be float

T = np.arange(fs * duration)
s = SawToothWave()

# Attack, Decay, Sustain, Release


class AudioFilter:
    def __init__(self, sampling_rate=44100):
        self.sampling_rate = sampling_rate

    def __call__(self, sample, *args, **kwargs):
        return self.wave_function(sample, *args, **kwargs).astype(np.float32)


class ADSR(AudioFilter):
    def get_envelope(self, attack, decay, sustain, release, sustain_level):
        timestamps = np.array([attack, decay, sustain, release])
        timestamps = (timestamps * self.sampling_rate).astype(int)

        x0 = np.linspace(0, 1, timestamps[0])
        x1 = np.linspace(1, sustain_level, timestamps[1])
        x2 = np.linspace(sustain_level, sustain_level, timestamps[2])
        x3 = np.linspace(sustain_level, 0, timestamps[3])

        return np.hstack([x0, x1, x2, x3])

    def wave_function(self, Y, attack, decay, sustain, release, sustain_level):

        envelope = self.get_envelope(attack, decay, sustain, release, sustain_level)

        remaining_timestamps = len(Y) - len(envelope)
        envelope = np.pad(envelope, (0, remaining_timestamps))

        return Y * envelope


sample = s(T, freq)

f = ADSR()
envelope = f.get_envelope(0.5, 0.25, 0.25, 0.25, 0.5)

import pylab as plt

plt.plot(envelope)
plt.title("Sample Envelope")
plt.show()

sample2 = ADSR()(sample, 0.5, 0.25, 0.25, 0.25, 0.5)


from sound_helpers import play_sample

play_sample(sample2)
play_sample(sample)
