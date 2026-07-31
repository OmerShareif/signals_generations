'''
Unknown Signal Frequency Detection
Given an unknown signal:
- Compute its DTFT
- Plot the spectrum
- Automatically detect the dominant frequencies
- Estimate their amplitudes
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

N=128
n = np.arange(N)

# Three sinusoidal components
x = 1.0*np.sin(0.15*np.pi*n) + 0.8*np.sin(0.35*np.pi*n) + 0.4*np.sin(0.70*np.pi*n)

# add gauusian noise
sigma = 0.2
noise = np.random.normal(0,sigma,N)
received = x + noise # doesnt know what frequencies are inside.

# Compute the DTFT
omega = np.linspace(-np.pi,np.pi,2048)
X = np.zeros(len(omega), dtype=complex)
for i,w in enumerate(omega):
    X[i] = np.sum(x*np.exp(-1j*w*n))
magnitude = np.abs(X)

# detect large peaks
peaks,properties = find_peaks(magnitude,height=20,distance=30)

print("=== Detected Frequencies ===")
for p in peaks:
    print(f"{omega[p]/np.pi:.3f}")

# strongest freq
largest_peak = peaks[np.argmax(properties["peak_heights"])]
print("strongest freq")
print(omega[largest_peak]/np.pi)

# Received Signal
plt.figure()
plt.plot(n,received)
plt.title("received signal")
plt.xlabel("samples")
plt.ylabel("amplitude")
plt.grid()

# plot DTFT spectrum
plt.figure()
plt.plot(omega/np.pi, magnitude)
plt.title("DTFT spectrum")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

#plot large peaks
plt.figure()
plt.plot(omega/np.pi,magnitude)
plt.plot(omega[peaks]/np.pi, magnitude[peaks],"ro")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()
