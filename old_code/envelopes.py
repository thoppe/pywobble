import torch

# Attack, Decay, Sustain, Release


class AudioFilter:
    def __init__(self, sampling_rate=44100):
        self.sampling_rate = sampling_rate

    def __call__(self, sample, *args, **kwargs):
        return self.wave_function(sample, *args, **kwargs)


class ADSR(AudioFilter):
    def get_envelope(
        self,
        params,
    ):

        # Force cast to torch if input is not
        if not torch.is_tensor(params):
            params = torch.tensor(params, dtype=float)

        timestamps = (params * self.sampling_rate).type(torch.int32)

        print(timestamps.sum().value)
        exit()
        envelope = torch.zeros(size=timestamps.sum())
        print(envelope)
        exit()
        # x0 = np.linspace(0, 0, timestamps[0])
        # x1 = np.linspace(0, 1, timestamps[1])
        # x2 = np.linspace(1, sustain_level, timestamps[2])
        # x3 = np.linspace(sustain_level, sustain_level, timestamps[3])
        # x4 = np.linspace(sustain_level, 0, timestamps[4])

        return np.hstack([x0, x1, x2, x3, x4])

    def wave_function(
        self,
        Y,
        params,
    ):
        # Params: Attack, decay, sustain, release, sustain_level, delay
        envelope = self.get_envelope(params)

        # Cut if too long
        envelope = envelope[: len(Y)]

        # Pad if too short
        remaining_timestamps = len(Y) - len(envelope)
        envelope = np.pad(envelope, (0, remaining_timestamps))

        return Y * envelope
