import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

fs = 1000 # sampling freq
T=1 # duration in secs
t = np.linspace(0,T,fs)
N = len(t)
f = 5

# message signal
x = square(2*np.pi*f*t)

X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)
magnitude = 2*np.abs(X)/N

plt.figure()
plt.title("square wave signal")
plt.plot(t,x,label="original square signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid()

plt.figure()
plt.title("fourier approx of Square wave")
plt.plot(freq,magnitude,label="fourier approx signal")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.legend()
plt.grid()

plt.show()