import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,20)
a = 0.8

x = a**n

plt.figure()
plt.stem(n,x)
plt.title("Discrete time Exponential Signal")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid()
plt.show()