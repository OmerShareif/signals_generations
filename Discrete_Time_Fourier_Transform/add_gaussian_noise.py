import numpy as np
import matplotlib.pyplot as plt

N=64
n = np.arange(N)

x = np.sin(0.2*np.pi*n) + 0.5*np.sin(0.5*np.pi*n)
noise = np.random.normal(0,0.3,N)
received = x+noise

omega = np.linspace(-np.pi,np.pi,512)

X_noise = np.zeros(len(omega), dtype=complex)

for k,w in enumerate(omega):
    X_noise[k] = np.sum(received*np.exp(-1j*w*n))

plt.figure()
plt.stem(n,received)
plt.title("signal + gaussian noise")
plt.xlabel("n")
plt.grid()

plt.figure()
plt.plot(omega/np.pi,2*np.abs(X_noise)/len(x))
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.title("DTFT signal")
plt.grid()



plt.show()