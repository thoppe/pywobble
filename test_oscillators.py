import pylab as plt

# from oscillators import SineWave, SawToothWave, SquareWave
from oscillators import SquareWave, TriangleWave, SawToothWave, SineWave

fs = 44100  # sampling rate, Hz, must be integer
t = 0.5  # in seconds, may be float
freq = 440.0  # sine frequency, Hz, may be float

s0 = SineWave()
sample0 = s0(t, freq)
print(sample0)

s1 = SquareWave()
sample1 = s1(t, freq)

s2 = TriangleWave()
sample2 = s2(t, freq)

s3 = SawToothWave()
sample3 = s3(t, freq)

from sound_helpers import play_sample

play_sample(sample0)
play_sample(sample2)
play_sample(sample1)
play_sample(sample3)

exit()

s1 = SquareWave()
sample1 = s1(t, freq)

s2 = TriangleWave()
sample2 = s2(t, freq)


T = s0.get_time(t)

plt.plot(T[:200], sample0[:200])
plt.plot(T[:200], sample1[:200])
plt.plot(T[:200], sample2[:200])
plt.plot(T[:200], sample3[:200])
plt.show()

play_sample(sample0)
play_sample(sample1)
play_sample(sample2)
play_sample(sample3)

# sample1 = s(T, f * 2)
# play_sample(sample1)

# sample = sample0 + sample1
# play_sample(sample)
