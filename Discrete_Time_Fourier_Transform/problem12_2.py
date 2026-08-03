'''
 Frequency Resolution using DTT
'''

import numpy as np
import matplotlib.pyplot as plt

fs = 1000
f1,f2 = 50,55 # Very close frequencies

N_values = [64,128,256,512]

def create_signal(N,fs,f1,f2):
    t = np.arange(N)/fs
    return np.sin(2*np.pi*f1*t) + 0.8*np.sin(2*np.pi*f2*t)

for i,N in enumerate(N_values):
    x = create_signal(N,fs,f1,f2)
    t = np.arange(N)/fs

    # compute DTFT
    omega = np.linspace(-np.pi,np.pi,2000)
    X = np.zeros(len(omega), dtype=complex)
    n = np.arange(N)
    for i,w in enumerate(omega):
        X[i] = np.sum(x*np.exp(-1j*w*n))

    freq = omega*fs/(2*np.pi)
    magnitude = np.abs(X)

    plt.figure()
    plt.plot(freq,magnitude,'b-')
    plt.title(f"N={N} samples")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.grid()

    plt.axvline(f1,color='red',label=f"{f1}Hz")
    plt.axvline(f2,color='green',label=f"{f2}Hz")


plt.legend()
plt.show()


