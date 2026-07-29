'''
DTFT of a Sinusoidal Pulse

x[n] = sin(0.4πn) for n=0..15
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,16)
x = np.sin(0.4*np.pi*n)
omega = np.linspace(-np.pi,np.pi,500)

X = np.array([np.sum(x*np.exp(-1j*w*n)) for w in omega])

plt.figure()
plt.plot(omega, np.abs(X))
plt.title("Magnitude of Sine Pulse")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.figure()
plt.plot(omega,np.angle(X))
plt.title("phase of Sine Pulse")
plt.xlabel("freq")
plt.ylabel("phase")
plt.grid()

plt.show()