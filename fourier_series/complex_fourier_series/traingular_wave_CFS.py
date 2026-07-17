'''
generate triangular wave at T=2pi for 

x(t) = |t| for -pi<=t<=pi

after solving CFS,

Ck =    pi/2            for n=0
   =    0               for n=even
   =    -2/(pi*k^2)     for n=odd
'''

import numpy as np
import matplotlib.pyplot as plt

N=20
t = np.arange(-N,N+1)
Ck = np.zeros_like(t,dtype=complex)

for i,ki in enumerate(t):
    if ki == 0:
        Ck[i] = np.pi/2
    elif ki%2!=0:
        Ck[i] = -2/(np.pi*ki**2)
    else:
        Ck[i]=0



plt.figure()
plt.title("Triangular Wave-Magnitude Spectrum")
plt.stem(t,np.abs(Ck),'--',label="CFS approx")
plt.xlabel("N harmonics")
plt.ylabel("Magnitude")
plt.legend()
plt.show()
