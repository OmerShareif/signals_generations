# Rectangular Pulse

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-5,5,1000)
T = 1
x = np.where(np.abs(t)<=T/2,1,0)
N = len(t)
plt.figure()
plt.plot(t,x,label="Original signal")
plt.legend()
plt.grid()
plt.xlabel("time")
plt.ylabel("x(t)")

X = np.fft.fft(x)
w = np.fft.fftfreq(N)
plt.figure()
plt.plot(w,np.abs(X), label="fourier transform signal")
plt.legend()
plt.grid()
plt.xlabel("w")
plt.ylabel("|X(w)|")
plt.show()