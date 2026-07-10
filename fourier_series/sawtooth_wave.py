'''
Generate Sawtooth Wave x(t) = t for -pi<t<pi with period T=2*pi

this is odd signal -> x(-t) = -x(t)

a0 = 0
an = 0
bn = exists

bn = 2((-1)^(n+1))/n
'''

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi,np.pi,1000)
x = t

N=50

x_fs = np.zeros_like(t)

for n in range(1,N+1):
    bn = 2*((-1)**(n+1))/n
    x_fs += bn*np.sin(n*t)

plt.figure()
plt.plot(t,x,label="original sawtooth")
plt.plot(t,x_fs,label="fourier approx")
plt.title("sawtooth wave using TFS")
plt.xlabel("t")
plt.ylabel("amplitude")
plt.legend()
plt.grid()
plt.show()