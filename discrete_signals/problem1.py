'''
Generate the discrete-time signal
        x[n]=sin(0.1πn)     for     0≤n≤40
'''

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,41)
x = np.sin(0.1*np.pi*n)

for i in range(len(n)):
    print(f"n = {n[i]:2d}, x[n] = {x[i]:.4f}")

plt.figure()
plt.stem(n,x)
plt.title("Discrete-Time Signal x[n] = sin(0.1πn)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()
plt.show()