import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0,1,10000)

plt.hist(data,bins=50,density=True)
plt.xlabel("x")
plt.ylabel("Density")
plt.title("PDF - Gaussian")
plt.show()