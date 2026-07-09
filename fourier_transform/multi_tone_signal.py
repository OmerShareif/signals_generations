import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq,ifft
from scipy.signal import find_peaks

def multitone():
    # Create a multi-tone signal and analyze its frequency spectrum.

    fs = 1000
    T=2
    t = np.linspace(0,T,fs)
    N = len(t)

    freqs = [5,12,25,40]
    amplitudes = [1.0,0.7,0.4,0.2]
    phases = [0,np.pi/4,np.pi/3,np.pi/2]

    x = np.zeros_like(t)

    # create multitone signal : sum of sine wave
    for f,A,phi in zip(freqs,amplitudes,phases):
        x += A * np.sin(2*np.pi*f*t + phi)

    # add small DC offset
    x += 0.1

    #compute FT
    X = fft(x)
    freq = fftfreq(N,1/fs)
    mag = 2*np.abs(X)/N


    print(f"signal contains {len(freqs)}")
    print(f"desired frequencies {freqs}")
    print(f"detected frequency : {freq.round(2)}")
    print(f"detected magnitudes : {mag.round(3)}")

    plt.figure()
    plt.plot(t,x,label="original signal")
    plt.title("multi tone signal - time domain")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.legend()
    plt.grid()

    plt.figure()
    plt.stem(freq,mag,label="magnitude spectrum")
    plt.title("Frequency domain - magnitude spectrum")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.legend()
    plt.grid()

    plt.figure()
    phase = 2*np.angle(X)/N
    plt.stem(freq,phase,label="phase spectrum")
    plt.title("phase spectrum")
    plt.xlabel("freq")
    plt.ylabel("phase")
    plt.legend()
    plt.grid()

    plt.show()

    return x,X,freq

x_multitone,X_multitone,freq_multitone =  multitone()