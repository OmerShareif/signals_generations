import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
N = 256

t = np.arange(N)/Fs

f0 = 125

x = np.sin(2*np.pi*f0*t) # Generate a sine wave

# Compute FFT
X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/Fs)

# Find the Peak Automatically
peak = np.argmax(np.abs(X))
print("Peak bin = ", peak)
print("peak freq:", freq[peak], 'Hz')

plt.figure()
plt.stem(freq,np.abs(X))
plt.title("FFT magnitude")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()
plt.show()

