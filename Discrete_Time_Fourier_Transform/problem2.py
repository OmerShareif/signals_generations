'''
based on problem1: DTFT of a Finite-Length Sequence

Compute and plot the DTFT of: x[n]=[1,2,1],n=512 Using FFT Approximation

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,1])
N=512
X = np.fft.fftshift(np.fft.fft(x,N))
omega = np.linspace(-np.pi,np.pi,N)

plt.figure()
plt.plot(omega,2*np.abs(X)/len(x))
plt.title("magnitude of DTFT signal")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()
plt.show()