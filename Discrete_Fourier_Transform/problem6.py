'''
Simple communication channel model

A basic communication channel model: received = attenuation * transmitted + noise
 
We'll "transmit" a simple digital bit sequence (as short pulses),
pass it through a noisy channel, and see how a filter helps
recover it correctly on the receiving end.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

bits = [1,0,1,1,0,0,1,0]
samples_per_bit = 50
tx_signal = np.repeat(bits,samples_per_bit).astype(float)

attenuation = 0.6
noise_std = 0.4
channel_noise = noise_std * np.random.randn(len(tx_signal))
rx_signal = attenuation * tx_signal + channel_noise

#  Receiver: low-pass filter to clean up noise, then threshold to recover bits
b,a = signal.butter(4,0.05,btype="low")
rx_filtered = signal.filtfilt(b,a,rx_signal)

recovered_bits = []
for i in range(len(bits)):
    block = rx_filtered[i * samples_per_bit:(i+1) * samples_per_bit]
    recovered_bits.append(1 if block.mean() > attenuation / 2 else 0)


print(f"Transmitted bits : {bits}")
print(f"recovered bits : {recovered_bits}")
print(f"correct : {recovered_bits == bits}")

plt.figure()
plt.plot(tx_signal)
plt.title("transmitted bits")
plt.grid()

plt.figure()
plt.plot(rx_signal)
plt.title("received signal (attenuated + noisy over the channel)")
plt.grid()

plt.figure()
plt.plot(rx_filtered)
plt.title("after receiver LPF")
plt.grid()

plt.show()