'''
To identify Frequency Detection i.e 
Suppose someone gives a signal and we don't know its frequency.
'''
import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T=1
f = 50

t = np.arange(0,T,1/fs)
n = np.arange(len(t))

# sinewave
x = np.sin(2*np.pi*f*t)

def compute(x,omega):
    X = np.zeros(len(omega), dtype=complex)
    n = np.arange(len(x))
    for i,w in enumerate(omega):
        X[i] = np.sum(x*np.exp(-1j*w*n))
    return X

omega = np.linspace(-np.pi,np.pi,2000)
X = compute(x,omega)

#convert to freq in Hz
freq_hz = omega * fs/(2*np.pi)

#time domain
plt.figure()
plt.plot(t[:200],x[:200])
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title(f"sine wave {f} Hz")
plt.grid()

#DTFT magnitude
plt.figure()
plt.plot(freq_hz,2*np.abs(X)/len(x))
plt.title("DTFT magnitude")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

#DTFT phase
plt.figure()
plt.plot(freq_hz,np.angle(X))
plt.title("DTFT phase")
plt.xlabel("freq")
plt.ylabel("phase")
plt.grid()

plt.show()