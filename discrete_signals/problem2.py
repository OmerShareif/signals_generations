'''
Given Signal: x[n]=sin(0.3πn)
Compute:
Operation 1 — Amplitude Scaling - 2x[n]
Operation 2 — Amplitude Shift - x[n]+1
Operation 3 — Time Delay - x[n−4]
Operation 4 — Time Reversal - x[−n]
Plot each result
'''

import numpy as np
import matplotlib.pyplot as plt

# sample
n = np.arange(-15,16)

# original signal
x = np.sin(0.3*np.pi*n)

plt.figure()
plt.stem(n, x)
plt.title("Original Signal: x[n] = sin(0.3πn)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Operation 1 — Amplitude Scaling
y = 2*x
plt.figure()
plt.stem(n, y)
plt.title("Amplitude Scaling: y[n] = 2x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Operation 2 — Amplitude Shift
y = x+1
plt.figure()
plt.stem(n, y)
plt.title("Amplitude Offset: y[n] = x[n] + 1")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Operation 3 — Time Delay
delay = 4
y = np.concatenate((np.zeros(delay), x[:-delay]))
plt.figure()
plt.stem(n, y)
plt.title("Delayed Signal: x[n-4]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# Operation 4 — Time Reversal
y = x[::-1]
plt.figure()
plt.stem(n, y)
plt.title("Time Reversal: x[-n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.show()