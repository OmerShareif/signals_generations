'''
Frequency Resolution using DTFT

Imagine a receiver that gets two signals:
Signal 1: 0.30π rad/sample
Signal 2: 0.32π rad/sample
These frequencies are very close.

seperate these two signals using DTFT

Increase N=32,64,128,256,512
'''

import numpy as np
import matplotlib.pyplot as plt

N=32
n = np.arange(N)

x = np.sin(0.30*np.pi*n) + np.sin(0.32*np.pi*n)

omega = np.linspace(-np.pi,np.pi,2048)

X = np.zeros(len(omega), dtype=complex)

for i,w in enumerate(omega):
    X[i] = np.sum(x*np.exp(-1j*w*n))

plt.figure()
plt.plot(omega/np.pi,np.abs(X))
plt.title("N=32")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()
plt.show()