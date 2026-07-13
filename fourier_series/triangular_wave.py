'''
let periodic signal T=2*pi
x(t) = t    for 0<=t<-pi
       -t   for -pi<=t<0

this is symmetrical signal with x(-t) = x(t)

this is even signal  i.e bn=0. only cosine term exists

a0 = pi/2
an = (-4/((pi*n^2))     for n is odd
   = 0              for n is even
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,1000)

x = np.abs(t)
N = 50

x_fs = (np.pi/2) * np.ones_like(t)

for n in range(1,N+1,2):
    an = -4/(np.pi * n**2)
    x_fs += an*np.cos(n*t)

plt.figure()
plt.plot(t,x,label="original tirangle")
plt.plot(t,x_fs,'--',label="TFS approx")
plt.title("triangular wave using TFS")
plt.xlabel("t")
plt.ylabel("amplitude")
plt.legend()
plt.grid()
plt.show()