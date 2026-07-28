'''
Using DTFT to Analyze a System

Given a system with impulse response h[n]=[1,−0.5], find the frequency response H(ejω)
'''

import numpy as np
import matplotlib.pyplot as plt

h = np.array([1,-0.5])
n = np.arange(len(h))
omega = np.linspace(-np.pi,np.pi,500)

H = np.zeros_like(omega,dtype=complex)

for k,w in enumerate(omega):
    H[k] = np.sum(h*np.exp(-1j*w*n))

plt.figure()
plt.plot(omega,np.abs(H))
plt.title("frequency response")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()
plt.show()
