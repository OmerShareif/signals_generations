import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=1
t = np.linspace(0,T,fs)
N = len(t)

x = (3*np.sin(2*np.pi*5*t + np.pi/6)) + (2*np.sin(2*np.pi*7*t - np.pi-4)) + (0.5*np.sin(2*np.pi*12*t))

X = np.fft.fft(x)
freq = np.fft.fftfreq(N,d=1/fs)
mag = 2*np.abs(X)/N
phase = np.angle(X)

plt.figure()
plt.title("time domain signal")
plt.plot(t,x,label="original signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid()

plt.figure()
plt.title("frequency domain signal")
plt.stem(freq,mag,label="fft signal")
plt.legend()
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.figure()
plt.title("phase spectrum")
plt.stem(freq,phase,label="phase domain")
plt.legend()
plt.xlabel("freq")
plt.ylabel("phase")
plt.grid()

plt.show()

