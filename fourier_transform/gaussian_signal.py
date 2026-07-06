# Generation of Gaussian signal

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10,10,2000)
N = len(t)
x = np.exp(-t**2)

X = np.fft.fft(x)
w = np.fft.fftfreq(N)

plt.figure()
plt.plot(w,np.abs(X))
plt.title("Magnitude spectrum")
plt.xlabel("freq")
plt.ylabel("magntide")
plt.grid()
plt.show()