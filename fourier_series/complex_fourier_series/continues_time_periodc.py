'''
consider a continues time periodic signal x(t) with period T=2pi

x(t) = t    for -pi<=t<=0
     = 0    for 0<=t<=pi

Ck =    -pi/4                           for k=0
   =    (1-jpik - e^(jpik))/(2pik^2)    for k!=0
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,3000)

x = np.where(t<0,t,0)

K = 20
x_hat = np.zeros_like(t,dtype=complex)

for k in range(-K,K+1):
    if k == 0:
        Ck = -np.pi/4

    else:
        Ck = (1 - 1j*np.pi*k - np.exp(1j*np.pi*k))/(2*np.pi*k**2)

    x_hat += Ck * np.exp(1j*k*t)

plt.figure()
plt.plot(t,x,label="original signal")
plt.plot(t,np.real(x_hat),'--',label="fourier approx")
plt.xlabel("time")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.title("CFS approximation")
plt.show()