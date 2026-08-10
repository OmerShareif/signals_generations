'''
write one reusable Python function that lets you apply any window, 
calculate its FFT, and inspect the effect in the frequency domain.

automatically get:
Original signal
      |
Apply window
      |
FFT
      |
Magnitude spectrum
      |
dB spectrum
      |
Plot

frequency resolution is: Δf= 1000/128 = 7.8125 Hz
103 Hz doesn't fall exactly on a bin. Therefore, leakage will be visible.
'''
import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
N = 128

n = np.arange(N)
f0 = 103

# create test signal
x = np.sin(2*np.pi*f0*n/Fs)

# build the window selector
def get_window(name,N):
    if name == "rectangular":
        return np.ones(N)

    elif name == "hann":
        return np.hanning(N)

    elif name == "hamming":
        return np.hamming(N)

    elif name == "blackman":
        return np.blackman(N)

    else:
        raise ValueError("Unknown Window")

w = get_window("hann",N)
# print(w)

# Build the Window Analyzer
def analyze_window(x,Fs,window_name):
    N = len(x)

    # create window
    w = get_window(window_name,N)

    #apply window
    x_windowed = x * w

    # FFT
    X = np.fft.fft(x_windowed)

    # frequency
    freq = np.fft.fftfreq(N,1/Fs)

    # positive freq
    half = N//2

    magnitude = np.abs(X[:half])

    # normalize
    magnitude = magnitude/np.max(magnitude)

    # convert to dB
    magnitude_dB = 20*np.log10(magnitude + 1e-12)

    #plot
    plt.figure()
    plt.plot(freq[:half],magnitude_dB)
    plt.title(f"{window_name.capitalize()} window")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.grid()

    plt.show()

analyze_window(x,Fs,"rectangular")
analyze_window(x,Fs,"hann")
analyze_window(x,Fs,"hamming")
analyze_window(x,Fs,"blackman")

