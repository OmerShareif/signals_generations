'''
Effect of Gaussian Noise on the Spectrum
The transmitted signal is x[n]=sin(0.25πn)
But during transmission, thermal noise is added.
The receiver gets r[n]=x[n]+w[n]
where
x[n] = desired signal
w[n] = Gaussian noise
r[n] = received signal
determine whether the signal can still be detected.
'''
import numpy as np
import matplotlib.pyplot as plt

N=128
n = np.arange(N)

#Generate the Clean Signal
signal = np.sin(0.25*np.pi*n)

#Generate Gaussian Noise
sigma = 0.2
noise = np.random.normal(0,sigma,N)

#Create the Received Signal
received = signal + noise

# Compute DTFT
omega = np.linspace(-np.pi,np.pi,1024)

X = np.zeros(len(omega),dtype=complex)

for i,w in enumerate(omega):
    X[i] = np.sum(received*np.exp(-1j*w*n))

#Compute Signal Power
signal_power = np.mean(signal**2)
print(signal_power)

#Compute Noise Power
noise_power = np.mean(noise**2)
print(noise_power)

#Compute SNR
snr = signal_power/noise_power
snr_db = 10*np.log10(snr)
print(f"SNR = {snr_db:.2f} dB")

plt.figure()
plt.plot(n, signal)
plt.title("Original Signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.plot(n, noise)
plt.title(f"Gaussian Noise")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

plt.figure()
plt.plot(n, received)
plt.title("Received Signal")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.grid()

#DTFT
plt.figure()
plt.plot(omega/np.pi, np.abs(X))
plt.xlabel("Freq")
plt.ylabel("Magnitude")
plt.title("DTFT of Noisy Signal")
plt.grid()

plt.show()