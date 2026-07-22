'''
Signal: s(t)=0.3cos⁡(2π50t)+0.2cos⁡(2π120t)
Channel / Noise:
Rayleigh fading:  h(t)∼Rayleigh(σ=1)
Additive Gaussian noise:  n(t)∼N(0,0.1^2)
'''

import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=4
t = np.arange(0,T,1/fs)
N = len(t)

# clean signal
s = 0.3*np.cos(2*np.pi*50*t) + 0.2*np.cos(2*np.pi*120*t)

#Rayleigh fading
sigma = 1
h = np.random.rayleigh(sigma,N)

# add AWGN
noise = 0.1*np.random.normal(0,1,N)

# received signal
x = h*s + noise

# FFT
X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)
mag = 2*np.abs(X)/N

plt.figure()
plt.plot(t[:500],x[:500])
plt.title("Weak Signal under Rayleigh + Noise (Time Domain)")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.plot(freq,mag)
plt.title("FFT Magnitude Spectrum (Weak Signal)")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()