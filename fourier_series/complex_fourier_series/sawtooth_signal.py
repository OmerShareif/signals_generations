'''
consider x(t) = t for -pi < t< pi

from TFS, bn = (2(-1)^(n+1))/n

convert to CFS
Cn = -j((-1)^(n+1))/n
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,1000)
x = t

T=2*np.pi
N=20

Cn = []
n_vals = np.arange(-N,N+1)

for n in n_vals:
    C = (1/T)*np.trapezoid(x*np.exp(-1j*n*t),t)
    Cn.append(C)

Cn = np.array(Cn)

plt.figure()
plt.stem(n_vals,np.abs(Cn))
plt.xlabel("N")
plt.ylabel("magnitude")
plt.title("magnitude spectrum")
plt.grid()

plt.figure()
plt.stem(n_vals,np.angle(Cn))
plt.xlabel("N")
plt.ylabel("phase")
plt.title("phase spectrum")
plt.grid()

plt.show()
