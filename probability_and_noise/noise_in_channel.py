import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000)

signal = np.sin(2*np.pi*5*t) # create clean signal

noise = np.random.normal(0,0.5,len(t)) # create Gauusian noise

received = signal + noise # add noise to signal in channel

plt.figure()
plt.plot(t,signal,label="signal")
plt.title("Clean Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.figure()
plt.plot(t,received,label="noisy signal received in channel")
plt.title("noisy received signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()