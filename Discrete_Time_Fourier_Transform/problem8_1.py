'''
To identify Frequency Detection i.e 
Suppose someone gives a signal and we don't know its frequency.
'''

import numpy as np
import matplotlib.pyplot as plt

N=64
n = np.arange(N)

# Generate Unknown Signal
x = np.sin(0.35*np.pi*n)

# Compute DTFT
omega = np.linspace(-np.pi,np.pi,1024)

X = np.zeros(len(omega), dtype=complex)

for k,w in enumerate(omega):
    X[k] = np.sum(x*np.exp(-1j*w*n))

plt.figure()
plt.stem(n,x)
plt.title("unknown signal")
plt.xlabel("sample n")
plt.ylabel("magnitude")
plt.grid()

plt.figure()
plt.stem(omega/np.pi, np.abs(X))
plt.title("DTFT of unknown signal")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()

peak_index = np.argmax(np.abs(X))
estimated_freq = omega[peak_index]
print(f"Estimated freq : {estimated_freq/np.pi}")