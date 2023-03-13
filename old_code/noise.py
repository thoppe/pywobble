import numpy as np
from oscillators import Oscillator


class NoiseModulation(Oscillator):
    epsilon = 0.00001

    def wave_function(self, T):
        n = len(T)
        X = np.fft.rfft(np.random.randn(n))
        S = np.fft.rfftfreq(n)

        S = self.modulation(S)

        S = S / np.sqrt(np.mean(S ** 2))
        X = X * S
        Z = np.fft.irfft(X)
        return Z


class WhiteNoise(NoiseModulation):
    def modulation(self, S):
        return 1


class BlueNoise(NoiseModulation):
    def modulation(self, S):
        return np.sqrt(S)


class VioletNoise(NoiseModulation):
    def modulation(self, S):
        return S


class PinkNoise(NoiseModulation):
    def modulation(self, S):
        return 1 / (np.sqrt(S + self.epsilon))


class BrownNoise(NoiseModulation):
    def modulation(self, S):
        return 1 / (S + self.epsilon)


class GreyNoise(NoiseModulation):
    def modulation(self, S):
        # Need a psychoacoustics weighting scale like
        # https://en.wikipedia.org/wiki/ITU-R_468_noise_weighting
        raise NotImplementedError
