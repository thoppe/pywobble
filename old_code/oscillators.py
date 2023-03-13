import math
import torch


class Oscillator:
    def __init__(self, sampling_rate=44100):
        self.sampling_rate = sampling_rate

    def __call__(self, duration, frequency, *args, **kwargs):
        T = self.get_time(duration)
        return self.wave_function(T, frequency, *args, **kwargs)

    def get_time(self, duration):
        return torch.arange(self.sampling_rate * duration)


class SineWave(Oscillator):
    def wave_function(self, T, frequency):
        X = (2 * math.pi * T * frequency) / self.sampling_rate
        Y = torch.sin(X)
        return Y


class SquareWave(SineWave):
    def wave_function(self, T, frequency):
        Y = SineWave.wave_function(self, T, frequency)
        return torch.sign(Y)


class TriangleWave(Oscillator):
    def wave_function(self, T, frequency):
        p = 1 / frequency * self.sampling_rate
        Y = 4 / p * torch.abs((((T - p / 4) % p + p) % p - p / 2)) - 1
        return Y


class SawToothWave(Oscillator):
    def wave_function(self, T, frequency):
        p = 1 / frequency * self.sampling_rate
        Y = 2 * (T / p - torch.floor(T / p + 0.5))
        return Y
