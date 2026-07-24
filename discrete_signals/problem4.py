'''
Multiply two sine waves.
x1[n]=sin(0.2πn)
x2[n]=sin(0.5πn)

y[n]=x1[n] * x2[n]
'''

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,50)

x1 = np.sin(0.2*np.pi*n)
x2 = np.sin(0.5*np.pi*n)

y = x1+x2

plt.figure()
plt.stem(n, x1)
plt.title("Signal 1")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.figure()
plt.stem(n, x2)
plt.title("Signal 2")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.figure()
plt.stem(n, y)
plt.title("Product of Two Signals")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.show()