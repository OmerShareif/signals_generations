'''
DTFT of a Windowed Exponential
	x[n] = (0.9)^n u[n] − (0.9)^n u[n−10]
'''
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,10)
x = 0.9**n
omega = np.linspace(-np.pi,np.pi,500)

X = np.array([np.sum(x*np.exp(-1j*w*n)) for w in omega])

plt.figure()
plt.plot(omega,2*np.abs(X)/len(x))
plt.title("DTFT of finite-length decaying exponential")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()
plt.show()
