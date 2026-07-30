'''
Detecting Two Frequencies
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

fs = 1000
T=1
f1=30
f2 = 80

t = np.arange(0,T,1/fs)
n = np.arange(len(t))

# Generate two-tone signal
x = np.sin(2*np.pi*f1*t) + 0.7*np.sin(2*np.pi*f2*t)

def compute(x,omega):
    X = np.zeros(len(omega), dtype=complex)
    n = np.arange(len(x))
    for i,w in enumerate(omega):
        X[i] = np.sum(x*np.exp(-1j*w*n))
    return X

omega = np.linspace(-np.pi,np.pi,3000)
X = compute(x,omega)
freq_hz = omega*fs/(2*np.pi)

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
