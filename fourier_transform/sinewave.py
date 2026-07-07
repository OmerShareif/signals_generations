import numpy as np
import matplotlib.pyplot as plt

fs = 10000 # sampling freq
T=1 # duration in secs
t = np.linspace(0,T,fs)
f = 5 # freq

x = np.sin(2*np.pi*f*t)

X = np.fft.fft(x) # convert time domain sample into frequency domain bins

N = len(x)

w = np.fft.fftfreq(N,d=1/fs)

magnitude = 2*np.abs(X)/N

plt.figure()
plt.plot(t,x,label="original signal")
plt.title("original signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid()

plt.figure()
plt.plot(w,magnitude,label="FT approx")
plt.title("FFT signal")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.legend()
plt.grid()

plt.show()