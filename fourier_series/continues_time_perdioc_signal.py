'''
x(t) = t        for -pi <= t< 0
     = pi - t   for 0 <= t <= pi 

and x(t+2pi) = x(t)

this is even signal --> x(-t) = x(t) = even = cosine terms - bn=0

a0 = pi/2
an = 4/n^2 when n is odd
   = 0      when n is even
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,2000)

x = np.where(t<0,t,np.pi-t)
N = 15
x_fs = np.pi/2 * np.ones_like(t)

for n in range(1,N+1,2):
    x_fs += (4/n**2)*np.cos(n*t)

plt.figure()
plt.plot(t,x,label="original signal")
plt.plot(t,x_fs,label="fourier approx")
plt.legend()
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("fourier series approx of continues time signal")
plt.grid()
plt.show()