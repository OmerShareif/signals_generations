'''
build a signal out of a few sine waves we CHOOSE, then run
the DFT on it and check that it correctly finds those same frequencies.

"Given a wave, tell me which frequencies it's made of."
'''
import numpy as np
import matplotlib.pyplot as plt

sample_rate = 500
duration = 1.0
t = np.linspace(0,duration, int(sample_rate*duration))

freq1,amp1 = 5,1.0  # slow wave
freq2,amp2 = 50,0.5  # fast wave

signal = amp1*np.sin(2*np.pi*freq1*t) + amp2*np.sin(2*np.pi*freq2*t)


def dft(x):
    N = len(x)
    X = np.zeros(N,dtype=complex)
    for k in range(N):
        total = 0
        for n in range(N):
            angle = -2j*np.pi*k*n/N
            total += x[n] * np.exp(angle)
        X[k] = total
    return X

X = dft(signal)
freqs = np.fft.fftfreq(len(signal),d=1/sample_rate)
magnitude = np.abs(X)/len(signal)

half = len(signal)//2
freqs_positive = freqs[:half]
magnitude_positive = magnitude[:half]*2

plt.figure()
plt.plot(t,signal)
plt.title("original signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.stem(freqs_positive,magnitude_positive)
plt.title("Freq Domain")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()
