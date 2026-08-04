'''
FIR Filter Frequency Response

'''

import numpy as np
import matplotlib.pyplot as plt

N = 500
n = np.arange(N)

signal = np.sin(0.10*np.pi*n) # message signal
noise = 0.5*np.random.randn(N) # noise 

# generate noisy signal
x = signal + noise

# define FIR coefficeints
h = np.ones(5)/5 # A 5-point moving average filter. --> [0.2 0.2 0.2 0.2 0.2]

# Apply the Filter
y = np.convolve(x,h,mode='same')

# compute DTFT of filter
omega = np.linspace(-np.pi,np.pi,2048)
H = np.zeros(len(omega), dtype=complex)
for i,w in enumerate(omega):
    H[i] = np.sum(h*np.exp(-1j*w*np.arange(len(h))))

# noise plot
plt.figure()
plt.plot(n,x)
plt.title("Noisy input signal")
plt.xlabel("sample")
plt.ylabel("amplitude")
plt.grid()

# plot FIR
plt.figure()
plt.plot(n,y)
plt.title("filtered signal")
plt.xlabel("sample")
plt.ylabel("amplitude")
plt.grid()

# plot DTFT
plt.figure()
plt.plot(omega/np.pi,np.abs(H))
plt.title("DTFT magnitude")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.show()
