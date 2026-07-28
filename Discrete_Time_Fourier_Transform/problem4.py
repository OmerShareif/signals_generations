'''
DTFT of a Shifted and Reversed Signal

Given x[n]=[1,2,3], find the DTFT of:
1. x[n−1]
2. x[−n]
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3])
n = np.array(len(x))
omega = np.linspace(-np.pi,np.pi,500)

X = np.array([np.sum(x*np.exp(-1j*w*n)) for w in omega])

# Shift x[n-1]
x_shift = np.roll(x,1)
x_shift[0] = 0
X_shift = np.array([np.sum(x_shift*np.exp(-1j*w*n)) for w in omega])

# Reverse x[-n]
x_rev = x[::-1]
X_rev = np.array([np.sum(x_rev*np.exp(-1j*w*n)) for w in omega])

plt.figure()
plt.plot(omega,np.abs(X), label="original")
plt.plot(omega,np.abs(X_shift), label="X shift")
plt.plot(omega,np.abs(X_rev), label="X Rev")
plt.title("Magnitude DTFT of x[n], x[n-1], x[-n]")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.legend()
plt.grid()
plt.show()