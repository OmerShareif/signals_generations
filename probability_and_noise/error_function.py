from scipy.special import erfc
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,100)
Q = 0.5*erfc(x/np.sqrt(2))

plt.plot(x, Q)
plt.title("Q-function")
plt.xlabel("x")
plt.ylabel("Q(x)")
plt.grid()
plt.show()