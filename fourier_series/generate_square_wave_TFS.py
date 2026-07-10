import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

T = 2*np.pi
t = np.linspace(-np.pi,np.pi,1000)

# generate Square Wave
x = square(np.sin(t))

N = 10 # number of harmonics

a0 = (1/T)*np.trapezoid(x,t)

an = []
bn = []

for n in range(1,N+1):
    an.append((2/T)*np.trapezoid(x*np.cos(n*t),t))
    bn.append((2/T)*np.trapezoid(x*np.sin(n*t), t))

x_approx = a0*np.ones_like(t)

for n in range(1,N+1):
    x_approx += an[N-1]*np.cos(n*t) + bn[n-1]*np.sin(n*t)

plt.figure()
plt.plot(t,x,label="original signal")
plt.plot(t,x_approx,'--',label="fourier approx")
plt.legend()
plt.title("Fourier Series approximation")
plt.grid()
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()