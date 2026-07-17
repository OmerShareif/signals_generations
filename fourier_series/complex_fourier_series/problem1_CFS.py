'''
consider a periodic signal with T=2pi for

x(t) = t for 0<t<2pi. 

this signal is not even or odd

after solving CFS,

    Cn = j/n    for n != 0
    Cn = 0      for n=0
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,1000)
x = t

T=2*np.pi
N=20

n_vals = np.arange(-N,N+1)
Cn = []

for n in n_vals:
    C = (1/T)*np.trapezoid(x*np.exp(-1j*n*t),t)
    Cn.append(C)

plt.figure()
plt.stem(n_vals,np.abs(Cn))
plt.title("magnitude spectrum")
plt.xlabel("Harmonics")
plt.ylabel("magnitude")
plt.grid()
plt.show()