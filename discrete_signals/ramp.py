import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,6)

r = n*(n>=0)

plt.figure()
plt.stem(n,r)
plt.title("Discrete time Ramp signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid()
plt.show()