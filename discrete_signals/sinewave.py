import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,20)
x = np.sin(0.3*np.pi*n)

plt.figure()
plt.stem(n,x)
plt.title("Discrete time Sine Wave")
plt.xlabel("Sample n")
plt.ylabel("Amplitude")
plt.grid()
plt.show()