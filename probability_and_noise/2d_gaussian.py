import numpy as np
import matplotlib.pyplot as plt

N = 500

I = np.random.normal(0,1,N)
Q = np.random.normal(0,1,N)

plt.scatter(I,Q)
plt.title("2D Gaussian Noise (I/Q Plane)")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.axis('equal')
plt.grid()
plt.show()