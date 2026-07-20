import numpy as np
import matplotlib.pyplot as plt

N=10000

x = np.random.normal(0,1,N)
y = np.random.normal(0,1,N)

r = np.sqrt(x**2 + y**2)

plt.hist(r,bins=60,density=True)
plt.title("Rayleigh Distribution")
plt.xlabel("Amplitude")
plt.ylabel("Density")
plt.show()