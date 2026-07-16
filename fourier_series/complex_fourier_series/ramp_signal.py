'''
generate ramp signal for x(t) = t for -pi<=t<=pi

Ck = j(-1^k)/k  for k!=0
C0 = 0          for k=0
'''
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,3000)
x = t

x_fs = np.zeros_like(t,dtype=complex)
K = 30

for k in range(-K,K+1):
    if k!=0:
        Ck = 1j*(-1**k)/k
    x_fs += Ck*np.exp(1j*k*t)

plt.figure()
plt.plot(t,x,label="original")
plt.plot(t,x_fs,'--',label="CFS approximation")
plt.title("Ramp signal")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid()
plt.show()