'''
Windowing is one of the main techniques used to control spectral leakage.

Calculate the Frequency Resolution: Δf=Fs/N
Δf = 1000 / 128 = 7.8125 Hz
The DFT bins are:
0
7.8125
15.625
23.4375
...
93.75
101.5625
109.375
...
100 Hz is not exactly a DFT bin. 
The closest bins are: 93.75 Hz and 101.5625 Hz. This is going to create leakage.
'''

import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
N = 128

n = np.arange(N)
f0 = 100

# create signal at 100 Hz.
x = np.sin(2*np.pi*f0*n/Fs)

# Rectangular Window - When simply take the first N samples, its effectively applying a rectangular window
w_rect = np.ones(N)
x_rect = x * w_rect

# calculate FFT for Rectangular Window
X_rect = np.fft.fft(x_rect)
freq = np.fft.fftfreq(N,1/Fs)
half = N//2


# Hann Window
w_hann = np.hanning(N)
x_hann = x * w_hann
X_hann = np.fft.fft(x_hann)


# Hamming Window
w_hamming = np.hamming(N)
x_hamming = x * w_hamming
X_hamming = np.fft.fft(x_hamming)


# Blackman Window
w_blackman = np.blackman(N)
x_blackman = x * w_blackman
X_blackman = np.fft.fft(x_blackman)


# plt signal
plt.figure()
plt.stem(n,x)
plt.title("100Hz sine signal")
plt.xlabel("sample n")
plt.ylabel("amplitude")
plt.grid()

# plot rectangular window
plt.figure()
plt.plot(freq[:half], np.abs(X_rect[:half])) # will see energy spread around the 100 Hz component.
'''
Because 100 Hz doesn't complete an integer number of cycles inside the observation window, 
the signal doesn't join smoothly at the boundaries.
'''
plt.title("rectangular window")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

# plot Hann Window
plt.figure()
plt.plot(freq[:half], np.abs(X_hann[:half]))
'''
side-lobes are significantly reduced.
main peak becomes wider.
'''
plt.title("Hann Window")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()


# plot Hamming Window
plt.figure()
plt.plot(freq[:half], np.abs(X_hamming[:half]))
'''
Hamming provides strong side-lobe suppression while maintaining a relatively narrow main lobe.
'''
plt.title("Hamming window")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()


# plot Blackman Window
plt.figure()
plt.plot(freq[:half], np.abs(X_blackman[:half]))
'''
Blackman has even better side-lobe suppression, but its main lobe is wider.
'''
plt.title("Blackman window")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()


plt.show()