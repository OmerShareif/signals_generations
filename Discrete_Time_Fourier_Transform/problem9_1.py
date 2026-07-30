'''
Detecting Two Unknown Frequencies

An unknown discrete-time signal contains two sinusoidal components.
- Generate the signal.
- Plot it in the time domain.
- Compute its DTFT numerically.
- Plot the magnitude spectrum.
- Detect the two frequencies.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

N=64
n = np.arange(N)

#unknown signal
x = np.sin(0.2*np.pi*n) + 0.7*np.sin(0.55*np.pi*n)

#DTFT
omega = np.linspace(-np.pi,np.pi,1024)

X = np.zeros(len(omega), dtype=complex)

for k,w in enumerate(omega):
    X[k] = np.sum(x*np.exp(-1j*w*n))

#time domain
plt.figure()
plt.stem(n,x)
plt.title("time domain")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

# DTFT magnitude
plt.figure()
plt.plot(omega/np.pi,np.abs(X))
plt.title("DTFT magnitude")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

magnitude = np.abs(X)
peaks,properties = find_peaks(magnitude,height=10)
plt.figure()
plt.plot(omega/np.pi, magnitude)
plt.plot(omega[peaks]/np.pi, magnitude[peaks],"ro")
plt.title("Detected peaks")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()

print("==== Detected Freq ====")
for p in peaks:
    print(f"{omega[p]/np.pi:.3f}")