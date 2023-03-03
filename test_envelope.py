import numpy as np
from oscillators import SawToothWave
from envelopes import ADSR

# from sound_helpers import play_sample
# import pylab as plt

fs = 44100  # sampling rate, Hz, must be integer
duration = 1.50  # in seconds, may be float
freq = 440.0  # sine frequency, Hz, may be float

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

w0 = s(duration, freq)
w1 = s(duration, freq / 8)

f = ADSR(fs)
x0 = f(w0, [0.5, 0.25, 0.25, 0.25, 0.5, 0.10])

print(x0)
exit()


x1 = f(w1, 0.25, 0.25, 0.0, 0.25, 0.25)

plt.plot(x0)
plt.plot(x1)
plt.show()

# play_sample(x0)
# play_sample(x1)
play_sample(x0 + x1)
