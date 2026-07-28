'''
DTFT of an Exponential Signal

Problem:  x[n]=(0.8)^n u[n]
'''

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,50)

x = 0.8**n
omega = np.linspace(-np.pi,np.pi,500)

X = np.zeros_like(omega,dtype=complex)

for k,w in enumerate(omega):
    X[k] = np.sum(x*np.exp(-1j*w*n))

plt.figure()
plt.plot(omega,np.abs(X))
plt.title("DTFT Magnitude of x[n] = (0.8)^n u[n]")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()
plt.show()
