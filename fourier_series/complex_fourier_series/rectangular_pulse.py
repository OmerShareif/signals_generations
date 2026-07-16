'''
plot rectangular pulse for T=2pi with

x(t) =  1 for|t|<pi/2
     =  0 for otherwise

after calculations,
Ck = sin(kpi/2)/kpi
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,3000)
x = np.where(np.abs(t)<np.pi/2,1,0)

K=20
x_fs = np.zeros_like(t,dtype=complex)

for k in range(-K,K+1):
    if k == 0:
        Ck = 0.5
    else:
        Ck = np.sin(k*np.pi/2)/(k*np.pi)
    x_fs += Ck * np.exp(1j*k*t)

plt.figure()
plt.plot(t,x,label="original")
plt.plot(t,x_fs,'--',label="CFS approximation")
plt.title("Reactangular pulse")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.show()