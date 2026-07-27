import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,64)

x = np.sin(0.2*np.pi*n)

X = np.fft.fft(x)
freq = np.fft.fftfreq(len(x))

plt.figure()
plt.stem(n,x)
plt.title("Time domain signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.stem(freq,2*np.abs(X)/len(x))
plt.title("Frequency spectrum")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()