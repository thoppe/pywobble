import numpy as np
from oscillators import SawToothWave
from envelopes import ADSR

fs = 44100  # sampling rate, Hz, must be integer
duration = 1.50  # in seconds, may be float
freq = 440.0  # sine frequency, Hz, may be float

T = np.arange(fs * duration)
s = SawToothWave()
f = ADSR()

"""
import pylab as plt
envelope = f.get_envelope(0.5, 0.25, 0.25, 0.25, 0.5)
plt.plot(envelope)
plt.title("Sample Envelope")
plt.show()

sample0 = s(T, freq)
sample1 = ADSR()(sample0, 0.5, 0.25, 0.25, 0.25, 0.5)

from sound_helpers import play_sample

play_sample(sample1)
play_sample(sample0)
"""

w0 = s(T, freq)
w1 = s(T, freq / 8)

f = ADSR(fs)
x0 = f(w0, 0.5, 0.25, 0.25, 0.25, 0.5, delay=0.10)
x1 = f(w1, 0.25, 0.25, 0.0, 0.25, 0.25)

import pylab as plt

plt.plot(x0)
plt.plot(x1)
plt.show()

from sound_helpers import play_sample

# play_sample(x0)
# play_sample(x1)
play_sample(x0 + x1)
