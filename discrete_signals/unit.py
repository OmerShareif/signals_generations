import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,6)

u = np.array([1 if i>=0 else 0 for i in n])

plt.figure()
plt.stem(n,u)
plt.title("Discrete Time Unit Signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid()
plt.show()