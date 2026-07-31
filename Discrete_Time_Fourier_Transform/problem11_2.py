'''
Detect unknown frequencies in a signal
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

fs = 2000
T=2

hidden_freq = [67,134,289,456]
hidden_amps = [1.0,0.7,0.5,0.3]

t = np.arange(0,T,1/fs)
n = np.arange(len(t))

# generating signal with unknown freq
x = np.zeros_like(t)
for f,A in zip(hidden_freq,hidden_amps):
    x += A * np.sin(2*np.pi*f*t + np.random.rand() * 2 * np.pi)

# add small noise
x += 0.05*np.random.randn(len(t))

def compute(x,omega):
    X = np.zeros(len(omega), dtype=complex)
    n = np.arange(len(x))
    for i,w in enumerate(omega):
        X[i] = np.sum(x*np.exp(-1j*w*n))
    return X

omega = np.linspace(-np.pi,np.pi,5000)
X = compute(x,omega)
freq_hz = omega*fs/(2*np.pi)
magnitude = np.abs(X)

peaks,properties = find_peaks(magnitude,height=np.max(magnitude), distance=20)

# Received Signal
plt.figure()
plt.plot(n,x)
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