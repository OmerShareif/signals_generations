'''
problem: Frequency Resolution vs Window Type

investigate: How close can two frequencies be before the FFT can no longer distinguish them?

compare:
    Rectangular
    Hann
    Hamming
    Blackman

gradually reduce the frequency separation and observe when the two peaks merge.

Suppose we have: f1 =100 Hz and f2=120 Hz
Now bring them closer: 100 Hz and 105 Hz and Now they may merge.

FFT bin spacing: Δf= Fs/N
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

Fs = 1000
N = 256

n = np.arange(N)

f1 = 100

df = Fs/N
print(f"Freq bin spacing = {df} Hz\n") #Frequency bin spacing

# Create the windows
windows = {
    "Rectangular": np.ones(N),
    "Hann":np.hanning(N),
    "Hamming": np.hamming(N),
    "Blackman":np.blackman(N)
}

# Create a two-tone signal
f2 = 120
x = np.sin(2*np.pi*f1*n/Fs) + np.sin(2*np.pi*f2*n/Fs) # Separation = 20 Hz

# Create an FFT function - use zero padding to make the spectrum easier to inspect.
def spectrum(x,window,Fs,NFFT=16384):
    N = len(x)
    xw = x * window
    X = np.fft.fft(xw,NFFT)
    freq = np.fft.fftfreq(NFFT,1/Fs)
    half = NFFT//2
    magnitude = np.abs(X[:half])
    magnitude = magnitude/np.max(magnitude)
    magnitude_db = 20*np.log10(magnitude + 1e-12)
    return freq[:half], magnitude_db

plt.figure()
for name,window in windows.items():
    freq,mag_db = spectrum(x,window,Fs)
    plt.plot(freq,mag_db,label=name)

plt.xlabel("freq")
plt.ylabel("magnitude")
plt.title("Two-Tone Frequency Resolution")
plt.grid()
plt.legend()

# Automatically find peaks
def count_peaks(f1,f2,Fs,N,window):
    n = np.arange(N)
    x = np.sin(2*np.pi*f1*n/Fs) + np.sin(2*np.pi*f2*n/Fs)
    freq,mag_db = spectrum(x,window,Fs)
    mask = (freq > f1 - 20) & (freq < f2 + 20)
    local_freq = freq[mask]
    local_mag = mag_db[mask]
    peaks,properties = find_peaks(local_mag,prominence=1)
    return (local_freq[peaks], local_mag[peaks])

peaks_f,peaks_mag = count_peaks(100,110,Fs,N,windows["Hann"])
print(f"Peak freq : {peaks_f}")
print()
print(f"Peak Magnitude : {peaks_mag}")

plt.show()
