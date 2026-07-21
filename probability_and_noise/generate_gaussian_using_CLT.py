import numpy as np
import matplotlib.pyplot as plt


N=10000
samples = np.sum(np.random.uniform(-1,1,(N,10)),axis=1)

plt.hist(samples,bins=50, density=True)
plt.title("CLT in Action (Uniform → Gaussian-like)")
plt.show()