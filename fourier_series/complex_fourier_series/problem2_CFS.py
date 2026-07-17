'''
consider  x(t) = cos(t)^2 for T=2pi

after solving CFS,


C0 = 1/2
C2 = 1/4
C-2 = 1/4
Cn = 0
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,1000)
x = np.cos(t)**2

T = 2*np.pi
N=10

n_vals = np.arange(-N,N+1)
Cn = []

for n in n_vals:
    C = (1/T)*np.trapezoid(x*np.exp(-1j*n*t),t)
    Cn.append(C)

plt.figure()
plt.stem(n_vals,np.abs(Cn))
plt.title("magnitude spectrum")
plt.xlabel("harmonics n")
plt.ylabel("magnitude")
plt.grid()
plt.show()