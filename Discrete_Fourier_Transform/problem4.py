'''
AWGN + SNR	
How noise is modeled, and how to measure signal-to-noise ratio in dB
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

sample_rate = 1000

def awgn_snr():
    t = np.arange(0,1,1/sample_rate)
    clean = np.sin(2*np.pi*5*t)

    def add_noise(signal,snr_db):
        signal_power = np.mean(signal**2)
        noise_power = signal_power / (10 ** (snr_db/10))
        noise = np.sqrt(noise_power)*np.random.randn(len(signal))
        return signal + noise, noise

    fig,axs = plt.subplots(3,1,figsize=(9,7))
    for ax,snr_db in zip(axs,[20,5,-5]):
        noisy, noise = add_noise(clean,snr_db)
        measured_snr = 10*np.log10(np.mean(clean**2)/np.mean(noise**2))
        ax.plot(t,noisy)
        ax.set_title(f"Target SNR = {snr_db} dB, measured_snr = {measured_snr} dB")
        ax.set_xlabel("time")
        fig.suptitle("same clean signal at different noise levels")
    plt.show()

awgn_snr()
    