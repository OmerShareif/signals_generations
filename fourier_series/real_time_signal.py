import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.linspace(0,1,fs)

# real time signal
x = 1.0*np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t) + 0.2*np.sin(2*np.pi*300*t)

plt.figure()
plt.plot(t,x,label="sum of 3 sine wave")
plt.title("real time signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid()
plt.show()