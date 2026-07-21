'''
Signal in Uniform Noise

A signal: s(t)=1.5cos⁡(2π40t)+cos⁡(2π90t) is corrupted by Uniform noise: n(t) ∼ U(−a,a)

Given:
a=1
fs=1000 Hz
T=2 seconds

STEP 1 — Theory
Uniform PDF: f(x) = 1/2a, −a ≤ x ≤ a
Mean: E[n]=0
Variance: σ^2 = a^2/3
For a=1: σ^2=1/3≈0.333
Noise power = 0.333
'''
import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=2
t = np.arange(0,T,1/fs)
N = len(t)

s = 1.5*np.cos(2*np.pi*40*t) + np.cos(2*np.pi*90*t)
a = 1
noise = np.random.uniform(-a,a,N)

x = s + noise

print("mean:", np.mean(noise))
print("varience:",np.var(noise))

X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)


plt.figure()
plt.plot(t,s)
plt.title("original signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.plot(freq,np.abs(X))
plt.title("Signal in Uniform Noise FFT")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()