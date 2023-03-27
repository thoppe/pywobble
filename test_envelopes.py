from oscillators import SineWave
from envelopes import ADSR
import pylab as plt


fs = 44100  # sampling rate, Hz, must be integer
t = 0.5  # in seconds, may be float
freq = 440.0  # sine frequency, Hz, may be float

s0 = SineWave()
sample0 = s0(t, freq)
T = s0.get_time(t)

sample1 = ADSR()(sample0)

from sound_helpers import play_sample

play_sample(sample0)
play_sample(sample1)

plt.plot(T[:20000], sample0[:20000])
plt.plot(T[:20000], sample1[:20000])
plt.show()
