'''
Generate a noisy sine wave
compute:
Energy
Average Power
Signal classification
Noise power
SNR
'''

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,1000)
x = np.sin(0.2*np.pi*n)

energy = np.sum(x**2)
print(f"Energy = {energy}")

signal_power = np.mean(x**2)
print(f"power = {signal_power}")

noise = np.random.normal(0,0.3,len(n))

noise_power = np.mean(noise**2)
print(f"Noise Power = {noise_power}")

received = x + noise
received_power = np.mean(received**2)
print(f"Received power = {received_power}")

snr = signal_power/noise_power
snr_db = 10*np.log10(snr)
print(f"SNR = {snr}")
print(f"SNR dB = {snr_db}")


plt.figure()
plt.plot(n,received)
plt.title("received signal with noise")
plt.grid()
plt.show()

