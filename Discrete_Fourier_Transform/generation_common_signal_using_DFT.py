'''
interpret the DFT of:

Unit impulse
Unit step
Sinusoid
Cosine
Square wave
Triangular wave
Sawtooth wave
Gaussian pulse
Random noise

For each signal, look at:
Time-domain waveform
DFT magnitude
DFT phase
What the spectrum tells us
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square,sawtooth

# Create a reusable DFT analyzer
def analyzer(x,title):
    N = len(x)
    X = np.fft.fft(x)
    X_shifted = np.fft.fftshift(X)

    freq = np.fft.fftfreq(N)
    freq_shifted = np.fft.fftshift(freq)

    plt.figure()
    plt.stem(np.arange(N),x)
    plt.title(f"{title} - Time Domain")
    plt.xlabel("sample n")
    plt.ylabel("Amplitude")
    plt.grid()

    plt.figure()
    plt.stem(freq_shifted, np.abs(X_shifted))
    plt.title(f"{title} - DFT magnitude")
    plt.xlabel("freq")
    plt.ylabel("|X[k]|")
    plt.grid()

    plt.figure()
    plt.stem(freq_shifted, np.angle(X_shifted))
    plt.title(f"{title} - DFT phase")
    plt.xlabel("phase")
    plt.ylabel("phase")
    plt.grid()

    plt.show()

N = 32
n = np.arange(N)

# unit Impulse
x = np.zeros(N)
x[0] = 1
analyzer(x,"Unit Impulse")

# unit step
x = np.ones(N)
analyzer(x,"Unit Step")

# constant signal
x = 3*np.ones(N)
analyzer(x,"Constant signal")

# sinosoidal signal
x = np.sin(2*np.pi*4*n/N)
analyzer(x,"sine signal")

# cosine signal
x = np.cos(2*np.pi*4*n/N)
analyzer(x,"cosine signal")

# Two-Tone Signal
x = np.sin(2*np.pi*3*n/N) + 0.5*np.sin(2*np.pi*9*n/N)
analyzer(x,"Two-Tone Signal")

# square wave
x = square(2*np.pi*3*n/N)
analyzer(x,"square wave")

# triangular wave
x = sawtooth(2*np.pi*3*n/N, width=0.5)
analyzer(x,"Triangular wave")

# Gaussian Pulse
center = N//2
sigma = 8
x = np.exp(
    -((n-center)**2)/(2*sigma**2)
)
analyzer(x,"Gaussian pulse")

# Random Noise
x = np.random.randn(N)
analyzer(x,"Gaussian noise")