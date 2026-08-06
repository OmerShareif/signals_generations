import numpy as np
import matplotlib.pyplot as plt

N = 4

n = np.arange(N)
k = n.reshape((N,1))

W = np.exp(-2j*np.pi*k*n/N) # DFT Matrix
print(W)

# Create an Input Signal
x = np.array([1,2,3,4])
print(x)

# Compute the DFT Using Matrix Multiplication
X = W @ x  #The @ operator performs matrix multiplication.
print(X)

# Verify with NumPy FFT
X_fft = np.fft.fft(x)
print(X_fft)

# compare
print(np.allclose(X, X_fft))

plt.figure()
plt.imshow(np.abs(W), cmap='viridis')
plt.colorbar(label="magnitude")
plt.title("magntidue of DFT matrix")
plt.xlabel("time sample (n)")
plt.ylabel("freq bin (k)")

plt.figure()
plt.imshow(np.angle(W), cmap='twilight')
plt.colorbar(label="phase")
plt.title("phase of DFT matrix")
plt.xlabel("time sample (n)")
plt.ylabel("freq bin (k)")

plt.show()