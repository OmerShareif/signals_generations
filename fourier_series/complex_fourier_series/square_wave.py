'''
generate square wave using

x(t) = 1    for 0<t<pi
     = 0    for -pi<t<0

complex fourier series,

Ck = 0          for k is even
   = -2j/(pik)  for k is odd
'''

import numpy as np
import matplotlib.pyplot as plt

K=20
t = np.arange(-K,K+1)
x = np.where(t<0,1,0)

x_fs = np.zeros_like(t,dtype=complex)

for k in range(-K,K+1):
    if k != 0 and k%2 !=0:
        Ck = 2j/(np.pi*k)
    
        x_fs -= Ck*np.exp(1j*k*t)

plt.figure()
plt.plot(t,x,label="original signal")
plt.plot(t,x_fs,'--',label="CFS approx")
plt.title("Square wave")
plt.legend()
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.show()