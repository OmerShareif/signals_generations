import numpy as np
import matplotlib.pyplot as plt

N=32
n = np.arange(N)

x = np.sin(2*np.pi*4*n/N) + 0.6*np.sin(2*np.pi*9*n/N) # signal with two frequencies

# compute DFT
X = np.fft.fft(x)

# Implement IDFT
def idft(X):
    N = len(X)
    x = np.zeros(N,dtype=complex)
    for n in range(N):
        total = 0
        for k in range(N):
            total += X[k]*np.exp(1j*2*np.pi*k*n/N)
        x[n] = total/N
    return x

# Recover the Signal
x_rec = idft(X)

# original signal
plt.figure()
plt.plot(n,x,'o-',label="original")
plt.stem(n,x,'x--',label="stem")
plt.title("original signal")
plt.xlabel("samples n")
plt.ylabel("amplitude")
plt.legend()
plt.grid()

# DFT signal
plt.figure()
plt.stem(n,np.abs(X))
plt.title("DFT magntude")
plt.xlabel("smples")
plt.ylabel("magnitude")
plt.grid()

# compare original and reconstructed signal
plt.figure()
plt.plot(x,'o-',label="original")
plt.plot(x_rec,'x--',label="Recovered")
plt.legend()
plt.title("Original vs Reconstructed Signal")
plt.grid()

plt.show()