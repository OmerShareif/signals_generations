import numpy as np
import matplotlib.pyplot as plt

N=32
n = np.arange(N)

x = np.sin(0.3*np.pi*n) # signal

# Compute the DTFT
omega = np.linspace(-np.pi,np.pi,2048)
X_dtft = np.zeros(len(omega),dtype=complex)
for i,w in enumerate(omega):
    X_dtft[i] = np.sum(x*np.exp(-1j*w*n))


# Compute the DFT
X_dft = np.fft.fft(x)
X_dft = np.fft.fftshift(X_dft) # Shift the zero-frequency component to the center
omega_dft = np.linspace(-np.pi,np.pi,N,endpoint=False) #Create the DFT frequency axis.

plt.figure()
plt.plot(omega/np.pi,np.abs(X_dtft),label="DTFT")
plt.stem(omega_dft/np.pi,np.abs(X_dft),linefmt='r-',markerfmt='ro',basefmt=' ',label="DFT")
plt.title(f"DTFT vs DFT")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()
plt.legend()
plt.show()