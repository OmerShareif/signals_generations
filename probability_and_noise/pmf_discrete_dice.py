import numpy as np
import matplotlib.pyplot as plt

N=10000
dice = np.random.randint(1,7,N)

values = np.arange(1,7)
pmf = [np.sum(dice == v)/N for v in values]

plt.stem(values,pmf)
plt.xlabel("Dice values")
plt.ylabel("probability")
plt.title("PMF of dice")
plt.show()