'''
AM signal spectrum - Communication systems

'''

import numpy as np
import matplotlib.pyplot as plt

N=256
n = np.arange(N)

fm = 0.05*np.pi  # Message frequency
fc = 0.40*np.pi  # Carrier frequency

message = np.cos(fm*n)

carrier = np.cos(fc*n)

# AM Modulation
mu = 1
am_signal = (1 + mu*message)*carrier

noise = np.random.normal(0,0.2,N)
received = am_signal + noise

# Compute the DTFT
omega = np.linspace(-np.pi,np.pi,4096)
X = np.zeros(len(omega), dtype=complex)
for i,w in enumerate(omega):
    X[i] = np.sum(am_signal*np.exp(-1j*w*n))


# Message signal
plt.figure()
plt.plot(n,message)
plt.title("Message signal")
plt.xlabel("time")
plt.ylabel("amplitde")
plt.grid()

# Carrier signal
plt.figure()
plt.plot(n,carrier)
plt.title("carrier signal")
plt.xlabel("time")
plt.ylabel("amplitude")

#AM Modulation
plt.figure()
plt.plot(n,received)
plt.title("AM signal")
plt.xlabel("time")
plt.ylabel("amplitude")

# DTFT Spectrum
plt.figure()
plt.plot(omega/np.pi,np.abs(X))
plt.title("AM DTFT spectrum")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()

