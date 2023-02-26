import numpy as np


class Oscillator:
    def __init__(self, sampling_rate=44100):
        self.sampling_rate = sampling_rate

    def __call__(self, T, frequency):
        return self.wave_function(T, frequency).astype(np.float32)


class SineWave(Oscillator):
    def wave_function(self, T, frequency):
        X = (2 * np.pi * T * frequency) / self.sampling_rate
        Y = np.sin(X)
        return Y


class SquareWave(Oscillator):
    def wave_function(self, T, frequency):
        X = (2 * np.pi * T * frequency) / self.sampling_rate
        Y = np.sign(np.sin(X))
        return Y


class TriangleWave(Oscillator):
    def wave_function(self, T, frequency):
        p = 1 / frequency * self.sampling_rate
        Y = 4 / p * np.abs((((T - p / 4) % p + p) % p - p / 2)) - 1
        return Y


class SawToothWave(Oscillator):
    def wave_function(self, T, frequency):
        p = 1 / frequency * self.sampling_rate
        Y = 2 * (T / p - np.floor(T / p + 0.5))
        return Y
