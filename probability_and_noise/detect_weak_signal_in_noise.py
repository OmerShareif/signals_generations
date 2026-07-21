'''
A weak sinusoidal signal:

s(t)=Acos⁡(2πf0t)

it is buried inside Gaussian noise: x(t)=s(t)+n(t)

Given:

A=0.2 (very small)
f0=50
SNR ≈ -10 dB (very noisy)

- Detect whether the 50 Hz signal exists using FFT.
'''

import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=2
t = np.arange(0,T,1/fs)
N = len(t)

A = 0.2
f0 = 50

signal = A * np.cos(2*np.pi*f0*t)
noise_std = 1 # much larger thans signal
noise = noise_std * np.random.normal(0,1,N)

x = signal + noise

X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)

plt.figure()
plt.plot(t[:500],x[:500])
plt.title("Weak signal hidden in noise")
plt.xlabel("time")
plt.ylabel("amplitude")

plt.figure()
plt.plot(freq,np.abs(X))
plt.title("FFT magnitude spectrum")
plt.xlabel("freq")
plt.ylabel("magnitude")

plt.show()