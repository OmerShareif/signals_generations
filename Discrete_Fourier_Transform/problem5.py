'''
Low-pass filtering in the frequency domain
low-pass filter (Butterworth) removes high-frequency content -- where a 
lot of noise energy lives -- while preserving low frequencies where our real signal lives.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

sample_rate = 1000

def low_pass_filter():
    t = np.arange(0,1,1/sample_rate)

    clean = np.sin(2*np.pi*5*t)
    noisy = clean + 0.5*np.random.randn(len(t))

    cutoff_hz = 15
    order = 4
    b,a = signal.butter(order,cutoff_hz/(sample_rate/2),btype="low")
    filtered = signal.filtfilt(b,a,noisy)

    plt.figure()
    plt.plot(t,noisy,label="noisy")
    plt.plot(t,clean,"k-",label="original signal")
    plt.plot(t,filtered,label="filtered")
    plt.legend()
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.grid()
    plt.title("Time domain LPF")

    freqs = np.fft.fftfreq(len(t), d=1/sample_rate)
    plt.figure()
    plt.plot(freqs,np.abs(np.fft.fft(noisy)), label="noisy spectrum")
    plt.plot(freqs,np.abs(np.fft.fft(filtered)), label="filtered spectrum")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.legend()
    plt.title("Freq domain LPF")


    plt.show()

low_pass_filter()