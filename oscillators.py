"""
SawToothWave, SquareWave, and TriangleWave adapted from:

https://pytorch.org/audio/main/tutorials/additive_synthesis_tutorial.html
"""

import torch
from torchaudio.prototype.functional import oscillator_bank, extend_pitch

PI = torch.pi
PI2 = 2 * torch.pi


class Oscillator:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate

    def ones(self, duration):
        NUM_FRAMES = int(duration * self.sample_rate)
        return torch.ones(NUM_FRAMES)

    def get_time(self, duration):
        return torch.arange(self.sample_rate * duration)

    def __call__(
        self,
        duration,
        frequency,
    ):
        freq = self.get_frequency_response(duration, frequency)
        amp = self.get_amplitude_response(duration, frequency)
        return oscillator_bank(freq, amp, sample_rate=self.sample_rate)


class SimpleOscillator(Oscillator):
    def get_frequency_response(self, t, f):
        f0 = f * self.ones(t)[:, None]
        return extend_pitch(f0, self.freq_mult(f))

    def get_amplitude_response(self, t, f):
        amp = self.ones(t)[:, None]
        return extend_pitch(amp, self.amp_mult(f))


class SineWave(SimpleOscillator):
    def freq_mult(self, f):
        return 1

    def amp_mult(self, f):
        return 1


class SawToothWave(SimpleOscillator):
    def freq_mult(self, f):
        num_pitch = int(self.sample_rate / f)
        return num_pitch

    def amp_mult(self, f):
        num_pitch = int(self.sample_rate / f)
        return [2.0 * -((-1) ** i) / (PI * i) for i in range(1, 1 + num_pitch)]


class SquareWave(SimpleOscillator):
    def freq_mult(self, f):
        num_pitch = int(self.sample_rate / f / 2)
        return [2.0 * i + 1.0 for i in range(num_pitch)]

    def amp_mult(self, f):
        num_pitch = int(self.sample_rate / f / 2)
        return [4.0 / (PI * (2.0 * i + 1.0)) for i in range(num_pitch)]


class TriangleWave(SimpleOscillator):
    def freq_mult(self, f):
        num_pitch = int(self.sample_rate / f / 2)
        return [2.0 * i + 1.0 for i in range(num_pitch)]

    def amp_mult(self, f):
        num_pitch = int(self.sample_rate / f / 2)
        c = 8 / (PI**2)
        return [
            c * ((-1) ** i) / ((2.0 * i + 1.0) ** 2) for i in range(num_pitch)
        ]
