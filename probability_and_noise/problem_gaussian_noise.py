'''
A sinusoidal signal: s(t)=Acos⁡(2πf0t) --> it is transmitted through an AWGN channel.

Given:
A=0.1
f0=75 Hz
Noise variance  σ2=1
Sampling frequency fs=1000
time T=4 seconds

STEP 1 :
Noise: n(t) ∼ N(0,σ^2)
Noisy signal: x(t)=s(t)+n(t)

Theoretical SNR (time-domain):
Signal power: P_s=A^2/2
Noise power: P_n = σ^2
SNR = P_n/​P_s​​

Compute Theoretical SNR:
for A = 0.1: P_s = 0.1^2/2 = 0.005
Noise power = 1, 
SNR=0.005
SNRdB​=10log10​(0.005)≈−23dB
'''
import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=4
t = np.arange(0,T,1/fs)
N = len(t)
A = 0.1
f0 = 75
sigma = 1

signal = A*np.cos(2*np.pi*f0*t)
noise = sigma * np.random.normal(0,1,N)

x = signal + noise
X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)

plt.figure()
plt.plot(freq,np.abs(X))
plt.title("Very Weak Signal in Noise")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()
plt.show()
