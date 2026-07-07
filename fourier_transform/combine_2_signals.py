'''
x(t) = sin(2*pi*5t) + 0.5*sin(2*pi*12t)
'''

import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=1
t = np.linspace(0,T,fs)
f = 5
x = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*12*t)

N = len(x)

X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)
mag = 2*np.abs(X)/N

plt.figure()
plt.title("original message signal")
plt.plot(t,x,label="original signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid()

plt.figure()
plt.title("Fourier transform approx")
plt.plot(freq,mag,label="fourier approx")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.legend()
plt.grid()

plt.show()
