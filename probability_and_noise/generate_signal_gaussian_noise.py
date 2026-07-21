'''
A signal is given by: s(t) = 2cos⁡(2π50t) + cos⁡(2π120t)

The signal is corrupted by Additive White Gaussian Noise (AWGN) with SNR = 10 dB.

Signal has:
-> 50 Hz component
-> 120 Hz component

Gaussian noise has: n(t) ∼ N(0,σ^2)

Noisy signal: x(t)=s(t)+n(t)
'''

import numpy as np
import matplotlib.pyplot as plt

fs = 1000 # sampling freq
T=1
t = np.arange(0,T,1/fs)

# signal
s = 2*np.cos(2*np.pi*50*t) + np.cos(2*np.pi*120*t)

# add gaussian noise with SNR control
SNR_dB = 10

# signal power
signal_power = np.mean(s**2)

# convert SNR from dB
SNR_linear = 10**(SNR_dB/10)

# noise power
noise_power = signal_power/SNR_linear

# generate gaussian noise
noise = np.sqrt(noise_power) * np.random.normal(0,1,len(t))

# noisy signal
x = s + noise

N = len(x)
X = np.fft.fft(x)

# freq
freq = np.fft.fftfreq(N,d=1/fs)

plt.figure()
plt.plot(t,x)
plt.title("noisy signal time domain")
plt.xlabel("time")

plt.figure()
plt.plot(freq,np.abs(X))
plt.title("magnitude spectrum with gaussian noise")
plt.xlabel("freq")
plt.show()