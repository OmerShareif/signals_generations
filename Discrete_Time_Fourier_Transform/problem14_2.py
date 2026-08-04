'''
AM Signal Spectrum
'''

import numpy as np
import matplotlib.pyplot as plt

fs = 10000 # sampling
T=0.5 # seconds
fc = 1000 # carrier freq
fm = 100 # message freq
m = 0.8 # modulation index

t = np.arange(0,T,1/fs)
n = np.arange(len(t))

# message signal
message = np.cos(2*np.pi*fm*t)

# AM signal
carrier = np.cos(2*np.pi*fc*t)
am_signal = (1 + m*message) * carrier

#compute DTFT
def compute(x,omega):
    X = np.zeros(len(omega), dtype=complex)
    n = np.arange(len(x))
    for i,w in enumerate(omega):
        X[i] = np.sum(x*np.exp(-1j*w*n))
    return X

omega = np.linspace(-np.pi,np.pi,4000)
X = compute(am_signal,omega)
freq = omega*fs/(2*np.pi)

# message signal
plt.figure()
plt.plot(t[:200], message[:200])
plt.title("message signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

# AM signal
plt.figure()
plt.plot(t[:200], am_signal[:200])
plt.plot(t[:200],(1+m*message[:200]), label="envelope")
plt.plot(t[:200],-(1+m*message[:200]))
plt.title("AM signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid()

# DTFT
magnitude = np.abs(X)
plt.plot(freq,magnitude)
plt.title("AM signal spectrum")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()