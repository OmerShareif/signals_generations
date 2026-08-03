'''
Windowing Effects & Spectral Leakage
Why peaks spread instead of becoming perfect impulses (spectral leakage)
Why a rectangular window creates sidelobes
comparison of Hamming, Hann, and Blackman windows
How the choice of window affects frequency resolution and leakage
'''

import numpy as np
import matplotlib.pyplot as plt

N=128
n = np.arange(N)
f = 0.25*np.pi

x = np.sin(f*n)

omega = np.linspace(-np.pi,np.pi,4096)

X = np.zeros(len(omega), dtype=complex)

for i,w in enumerate(omega):
    X[i] = np.sum(x*np.exp(-1j*w*n))

plt.figure()
plt.plot(omega/np.pi,np.abs(X))
plt.title("DTFT")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

#create the simplest window
window = np.ones(N)
plt.figure()
plt.stem(window)
plt.title("Rectangular Window")
plt.grid()

#create the Hann Window
window1 = np.hanning(N)
plt.figure()
plt.stem(window1)
plt.title("Hanning Window")
plt.grid()

#create the Blackman windows
window2 = np.blackman(N)
plt.figure()
plt.stem(window2)
plt.title("Blackman windows")
plt.grid()

#Apply the Rectangular Window
x_window = x * window

X = np.zeros(len(omega), dtype=complex)

for i,w in enumerate(omega):
    X[i] = np.sum(x_window*np.exp(-1j*w*n))

plt.figure()
plt.plot(omega/np.pi,np.abs(X))
plt.title("DTFT with Rect Window")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

#Apply the Hanning Window
x_window1 = x * window1

X = np.zeros(len(omega), dtype=complex)

for i,w in enumerate(omega):
    X[i] = np.sum(x_window1*np.exp(-1j*w*n))

plt.figure()
plt.plot(omega/np.pi,np.abs(X))
plt.title("DTFT with Hanning Window")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

#Apply the Blackman Window
x_window2 = x * window2

X = np.zeros(len(omega), dtype=complex)

for i,w in enumerate(omega):
    X[i] = np.sum(x_window2*np.exp(-1j*w*n))

plt.figure()
plt.plot(omega/np.pi,np.abs(X))
plt.title("DTFT with Blackman Window")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()