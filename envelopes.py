import numpy as np

# Attack, Decay, Sustain, Release


class AudioFilter:
    def __init__(self, sampling_rate=44100):
        self.sampling_rate = sampling_rate

    def __call__(self, sample, *args, **kwargs):
        return self.wave_function(sample, *args, **kwargs).astype(np.float32)


class ADSR(AudioFilter):
    def get_envelope(
        self, attack, decay, sustain, release, sustain_level, delay
    ):
        timestamps = np.array([delay, attack, decay, sustain, release])
        timestamps = (timestamps * self.sampling_rate).astype(int)

        x0 = np.linspace(0, 0, timestamps[0])
        x1 = np.linspace(0, 1, timestamps[1])
        x2 = np.linspace(1, sustain_level, timestamps[2])
        x3 = np.linspace(sustain_level, sustain_level, timestamps[3])
        x4 = np.linspace(sustain_level, 0, timestamps[4])

        return np.hstack([x0, x1, x2, x3, x4])

    def wave_function(
        self, Y, attack, decay, sustain, release, sustain_level, delay=0
    ):

        envelope = self.get_envelope(
            attack, decay, sustain, release, sustain_level, delay
        )

        # Cut if too long
        envelope = envelope[: len(Y)]

        # Pad if too short
        remaining_timestamps = len(Y) - len(envelope)
        envelope = np.pad(envelope, (0, remaining_timestamps))

        return Y * envelope
