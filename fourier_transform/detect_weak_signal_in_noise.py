import numpy as np
import matplotlib.pyplot as plt

fs = 500
T=2
t = np.linspace(0,T,fs)
N = len(t)

# message signal
x = 1.2*np.sin(2*np.pi*15*t) + 0.8*np.sin(2*np.pi*40*t)

# noise signal
noise = np.random.normal(0,T,N)

# adding noise to message signal
x_noisy = x + noise

X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)
mag = 2*np.abs(X)/N

plt.figure()
plt.title("message signal")
plt.plot(t,x,label="original signal")
plt.legend()
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.title("noisy signal")
plt.plot(t,x_noisy,label="nosiy signal")
plt.legend()
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.title("fourier transform signal")
plt.plot(freq,mag,label="fourier approx")
plt.legend()
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()
