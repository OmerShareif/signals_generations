'''
Even/Odd symmetry

Even - only Cosine term
Odd - only sine term
'''

# generate even signal

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1,1,1000)
x = np.cos(2*np.pi*t)

plt.figure()
plt.plot(t,x,label="Cosine signal")
plt.title("Even Signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid()
plt.show()
