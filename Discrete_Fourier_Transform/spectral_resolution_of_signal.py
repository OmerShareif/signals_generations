import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
N = 128

t = np.arange(N)/Fs

f1 = 100
f2 = 105

x = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) # Generate Two Close Frequencies

# Compute FFT
X = np.fft.fft(x)
freq = np.fft.fftfreq(N,1/Fs)

# Keep only positive frequencies.
half = N//2

plt.figure()
plt.stem(freq[:half],np.abs(X[:half]))
plt.title("FFT spectrum")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()