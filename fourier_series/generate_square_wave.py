import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

t = np.linspace(-np.pi,np.pi,1000)

x = square(np.sin(t))

plt.figure()
plt.plot(t,x,label="Square Wave")
plt.title("Square Wave")
plt.legend()
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()
plt.show()