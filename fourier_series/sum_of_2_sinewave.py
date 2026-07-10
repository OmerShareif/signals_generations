import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000)

x = np.sin(2*np.pi*1*t) + 0.5*np.sin(2*np.pi*3*t)

plt.plot(t,x,label="sine signal")
plt.legend()
plt.title("sum of sinosoidal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()
plt.show()
