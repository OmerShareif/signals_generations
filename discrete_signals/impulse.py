import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,6)

delta = np.array([1 if i==0 else 0 for i in n])

plt.figure()
plt.stem(n,delta)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("Discrete time Impulse Signal")
plt.grid()
plt.show()