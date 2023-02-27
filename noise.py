import numpy as np
import pylab as plt
from oscillators import Oscillator


def plot_spectrum(s, **kwargs):
    f = np.fft.rfftfreq(len(s))
    return plt.loglog(f, np.abs(np.fft.rfft(s)), lw=0.5, **kwargs)[0]


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


fs = 44100  # sampling rate, Hz, must be integer
duration = 0.25  # in seconds, may be float
T = np.arange(fs * duration)


from sound_helpers import play_sample


play_sample(WhiteNoise()(T), 0.25)
play_sample(BlueNoise()(T), 0.25)
play_sample(VioletNoise()(T), 0.25)
play_sample(BrownNoise()(T), 1)
play_sample(PinkNoise()(T), 0.25)


alp = 0.75
plot_spectrum(WhiteNoise()(T), color="black", alpha=alp)
plot_spectrum(BlueNoise()(T), color="mediumblue", alpha=alp)
plot_spectrum(VioletNoise()(T), color="darkviolet", alpha=alp)
plot_spectrum(BrownNoise()(T), color="sienna", alpha=alp)
plot_spectrum(PinkNoise()(T), color="pink", alpha=alp)
plt.ylim(0.001, 1000)
plt.tight_layout()
plt.show()
