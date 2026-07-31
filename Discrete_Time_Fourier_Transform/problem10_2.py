'''
Effect of Gaussian Noise on the Spectrum
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

fs = 1000
T=2
f = 45

t = np.arange(0,T,1/fs)
n = np.arange(len(t))

# signal
signal = np.sin(2*np.pi*f*t)

#add gauusian noise
noise_power = 0.5
noise = np.sqrt(noise_power) * np.random.randn(len(t))

# creating noise signal with different SNRs
SNR_dB_values = [10,0,-10] #dB
signals = []

for SNR_dB in SNR_dB_values:
    # signal power
    signal_power = np.mean(signal**2)
    noise_power = signal_power/(10**(SNR_dB/10))
    noise_scaled = np.sqrt(noise_power) * np.random.randn(len(t))
    signals.append(signal + noise_scaled)

def compute(x,omega):
    X = np.zeros(len(omega), dtype=complex)
    n = np.arange(len(x))
    for i,w in enumerate(omega):
        X[i] = np.sum(x*np.exp(-1j*w*n))
    return X

omega = np.linspace(-np.pi,np.pi,4000)
freq_hz = omega*fs/(2*np.pi)

for i,(SNR_dB,x_noisy) in enumerate(zip(SNR_dB_values,signals)):
    X = compute(x_noisy,omega)
    magnitude = np.abs(X)

    #time domain
    plt.figure()
    plt.plot(t[:500],x_noisy[:500])
    plt.title(f"SNR = {SNR_dB} dB")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.grid()

    # freq domain
    plt.figure()
    plt.plot(freq_hz,magnitude)
    plt.title("DTFT magnitude")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.grid()

    peaks,properties = find_peaks(magnitude,height=10)
    plt.figure()
    plt.plot(omega/np.pi,magnitude)
    plt.plot(omega[peaks]/np.pi,magnitude[peaks],"ro")
    plt.title("Detected peaks")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.grid()

plt.show()