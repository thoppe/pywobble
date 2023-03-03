import pylab as plt
import numpy as np

import noise
from sound_helpers import play_sample

fs = 44100  # sampling rate, Hz, must be integer
duration = 0.25  # in seconds, may be float
T = np.arange(fs * duration)


play_sample(noise.WhiteNoise()(T), 0.25)
play_sample(noise.BlueNoise()(T), 0.25)
play_sample(noise.VioletNoise()(T), 0.25)
play_sample(noise.BrownNoise()(T), 1)
play_sample(noise.PinkNoise()(T), 0.25)


def plot_spectrum(s, **kwargs):
    f = np.fft.rfftfreq(len(s))
    return plt.loglog(f, np.abs(np.fft.rfft(s)), lw=0.5, **kwargs)[0]


alp = 0.75
plot_spectrum(noise.WhiteNoise()(T), color="black", alpha=alp)
plot_spectrum(noise.BlueNoise()(T), color="mediumblue", alpha=alp)
plot_spectrum(noise.VioletNoise()(T), color="darkviolet", alpha=alp)
plot_spectrum(noise.BrownNoise()(T), color="sienna", alpha=alp)
plot_spectrum(noise.PinkNoise()(T), color="pink", alpha=alp)
plt.ylim(0.001, 1000)
plt.tight_layout()
plt.show()
