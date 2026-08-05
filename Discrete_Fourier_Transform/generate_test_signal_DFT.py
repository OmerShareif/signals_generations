import numpy as np
import matplotlib.pyplot as plt

N=32
n = np.arange(N)

# Test Signal
x = np.sin(2*np.pi*4*n/N) # its frequency aligns exactly with DFT bin 4.


# Create an Empty DFT Array
X = np.zeros(N,dtype=complex)

# plot input signal
plt.figure()
plt.stem(n,x)
plt.title("Input signal")
plt.xlabel("sample index")
plt.ylabel("amplitude")
plt.grid()

# Implement the DFT
for k in range(N):
    total = 0
    for n in range(N):
        total += x[n] * np.exp(-1j*2*np.pi*k*n/N)
    X[k] = total

# Compare with NumPy FFT
X_fft = np.fft.fft(x)
print(np.allclose(X, X_fft))

# plot magnitude
plt.figure()
plt.stem(np.arange(N), np.abs(X))
plt.title("magnitude spectrum")
plt.xlabel("freq bin")
plt.ylabel("magnitude |X[k]|")
plt.grid()

# plot phase
plt.figure()
plt.stem(np.arange(N), np.angle(X))
plt.title("phase spectrum")
plt.xlabel("freq bin")
plt.ylabel("phase")
plt.grid()

plt.show()