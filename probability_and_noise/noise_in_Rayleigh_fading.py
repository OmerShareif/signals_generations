import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000)

# signal
signal = np.sin(2*np.pi*5*t)

# Rayleigh fading
h = np.sqrt(np.random.normal(0,1,len(t))**2 + np.random.normal(0,1,len(t))**2)

# noise
noise = np.random.normal(0,0.2,len(t))
received = h*signal + noise

plt.plot(t,received)
plt.title("Signal with Rayleigh Fading + Noise")
plt.show()