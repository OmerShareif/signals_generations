'''
x(t) = A    for 0<t<pi
     = -A   for -pi <t<0

this is Odd signal --> x(-t) = -x(t)
a0 = 0
an = 0
bn exists

bn = 4A/(n*pi)  when n is odd
   = 0          when n is even
'''

import numpy as np
import matplotlib.pyplot as plt

A=1
t = np.linspace(-np.pi,np.pi,1000)
N=50

#original square wave signal
x = np.where(t>0,A,-A)

x_fs = np.zeros_like(t)

for n in range(1,N+1,2):
    x_fs += ((4*A)/(np.pi*n))*np.sin(n*t)

plt.figure()
plt.plot(t,x,label="original square wave")
plt.plot(t,x_fs,'--',label="TFS approx")
plt.title("square wave using TFS")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()
plt.legend()
plt.show()