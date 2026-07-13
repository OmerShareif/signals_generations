'''
for continues time periodic signal x(t) with period T=2pi

x(t)    = sint  for 0<t<pi
        = 0     for pi<t<2pi

a0 = 1/pi

an  =   0                   when n is odd
    =   -2/(pi(n^2 - 1))    when n is even

bn  =   1/2 when n=1
    =   0   when n != 1
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2*np.pi,2000)
x = np.where((t >=0) & (t < np.pi), np.sin(t),0)

N=20
x_fs = (1/np.pi)*np.ones_like(t)

# bn term
x_fs += 0.5*np.sin(t)

# cosine term
for n in range(2,N+1,2):
    x_fs -= (2/np.pi)*(1/(n**2 - 1))* np.cos(n*t)

plt.figure()
plt.plot(t,x,label="original signal")
plt.plot(t,x_fs,label="fourier approx")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.show()