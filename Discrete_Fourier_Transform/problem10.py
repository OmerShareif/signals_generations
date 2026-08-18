'''
AWGN + SNR MODELING
Understanding Additive White Gaussian Noise and Signal-to-Noise Ratio
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

class AWGNModel:
    def __init__(self,fs=1000,duration=1):
        self.fs = fs
        self.duration = duration
        self.t = np.arange(0,duration,1/fs)

    def generate_signal(self,freq=50,amplitude=1.0):
        return amplitude*np.sin(2*np.pi*freq*self.t)

    def add_noise(self,signal,snr_db):
        """
        Add AWGN to signal with specified SNR in dB
        SNR = 10 * log10(P_signal / P_noise)
        """
        # calculate signal power
        signal_power = np.mean(signal**2)

        # Calculate noise power for desired SNR
        # P_noise = P_signal / 10^(SNR_dB/10)
        noise_power = signal_power/(10**(snr_db/10))

        # generate AWGN
        noise = np.sqrt(noise_power) * np.random.randn(len(signal))

        return signal + noise, noise

    def calculate_snr(self,signal,noise):
        # calculate SNR in dB from signal and noise
        signal_power = np.mean(signal**2)
        noise_power = np.mean(noise**2)
        snr = 10*np.log10(signal_power/(noise_power + 1e-10))
        return snr

    def plot_snr(self):
        # generate clean signal
        clean = self.generate_signal()

        # different SNR level
        snr_levels = [-10,0,10,20,30]

        # clean signal
        plt.figure()
        plt.plot(self.t[:200], clean[:200], 'b-')
        plt.title("clean signal - no noise")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.grid()

        # noisy signal
        plt.figure()
        for id,snr in enumerate(snr_levels):
            noisy,noise = self.add_noise(clean,snr)
            plt.plot(self.t[:200], noisy[:200], 'r-' )
            plt.title(f"SNR = {snr} dB")
            plt.xlabel("time")
            plt.ylabel("amplitude")
            plt.grid()
        plt.show()
        return clean,noisy,noise

awgn = AWGNModel()
clean,noisy,noise = awgn.plot_snr()
        
