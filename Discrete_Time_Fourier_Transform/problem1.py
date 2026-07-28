'''
DTFT of a Finite-Length Sequence

Compute and plot the DTFT of: x[n]=[1,2,1],n=0,1,2
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,1])
n = np.arange(len(x))
omega = np.linspace(-np.pi,np.pi,500)

X = np.zeros_like(omega,dtype=complex)

for k,w in enumerate(omega):
    X[k] = np.sum(x*np.exp(-1j*w*n))

plt.figure()
plt.plot(omega,np.abs(X))
plt.title("magnitude of DTFT")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.figure()
plt.plot(omega,np.angle(X))
plt.title("phase of DTFT")
plt.xlabel("freq")
plt.ylabel("phase")
plt.grid()

plt.show()