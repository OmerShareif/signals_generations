'''
A transmitted signal: s(t) = cos⁡(2π60t)
passes through a Rayleigh fading channel and is corrupted by small Gaussian noise.

Received signal model:
			x(t)=h(t)s(t)+n(t)
Where:
h(t) ∼ Rayleigh(σ) → fading amplitude
n(t) ∼ N(0,σ^2_n)

Given:
fs=1000Hz
T=2 seconds
Rayleigh parameter  σ=1
Small AWGN noise

STEP 1 — Theory
Rayleigh PDF: f(x) = x/σ^2 * ​e(−x^2/2σ^2)
Mean:  E[h]=σ sqrt(π/2)
Variance: Var(h) = (4−π)σ^2 /2

Unlike Gaussian noise: -> Rayleigh affects amplitude multiplicatively, not additively.
That means: x(t)=h(t)s(t)
This causes:
Random amplitude fluctuations
Spectral broadening
'''

import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=2
t = np.arange(0,T,1/fs)
N = len(t)

f0 = 60
s = np.cos(2*np.pi*f0*t)

sigma = 1
h = np.random.rayleigh(sigma,N)

noise = 0.1*np.random.normal(0,1,N)

x = h*s + noise

X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)
mag = 2*np.abs(X)/N

plt.figure()
plt.plot(t[:500],x[:500])
plt.title("signal under Rayleigh fading")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.plot(freq,mag)
plt.title("FFT under Rayleigh Fading")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()