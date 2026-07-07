import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=1
t = np.linspace(0,T,fs)
N = len(t)

# message signal - original
x = 3*np.sin(2*np.pi*5*t) + 2*np.sin(2*np.pi*7*t) + 0.5*np.sin(2*np.pi*12*t)

# adding noise
x += 0.2*np.random.randn(N)

#fft
X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)
magnitude = 2*np.abs(X)/N

plt.figure()
plt.title("original message signal")
plt.plot(t,x,label="original signal")
plt.legend()
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.title("fourier approximation signal")
plt.plot(freq,magnitude,label="fourier approx")
plt.legend()
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()