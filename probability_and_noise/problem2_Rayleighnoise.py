'''
Signal: s(t) = cos⁡(2π50t)+0.5cos⁡(2π120t)

Channel / Noise:
- Rayleigh fading amplitude: h(t) ∼ Rayleigh(σ=1)
Additive Gaussian noise:  n(t) ∼ N(0,0.1^2)
'''
import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=2
t = np.arange(0,T,1/fs)
N = len(t)

# Clean signal
s = np.cos(2*np.pi*50*t) + 0.5*np.cos(2*np.pi*120*t)
#Rayleigh fading amplitude
sigma = 1
h = np.random.rayleigh(sigma,N)
# Small Gaussian noise
noise = 0.1*np.random.normal(0,1,N)

#Received signal
x = h*s + noise


X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)
mag = 2*np.abs(X)/N

plt.figure()
plt.plot(t[:500],x[:500])
plt.title("Signal under Rayleigh fading + noise (time domain)")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.plot(freq,mag)
plt.title("FFT of Signal under Rayleigh fading + noise")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()