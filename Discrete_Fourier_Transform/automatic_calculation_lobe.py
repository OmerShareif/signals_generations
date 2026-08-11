import numpy as np
import matplotlib.pyplot as plt

N = 128

windows = {
    "Rectangular" : np.ones(N),
    "Hann" : np.hanning(N),
    "Hamming": np.hamming(N),
    "Blackman": np.blackman(N)
}

# Calculate the frequency response
def window_freq_response(window,NFFT=65536):
    W = np.fft.fft(window,NFFT)
    W = np.fft.fftshift(W)
    magnitude = np.abs(W)
    magnitude = magnitude/np.max(magnitude)
    magnitude_dB = 20*np.log10(magnitude + 1e-15)
    freq = np.fft.fftshift(np.fft.fftfreq(NFFT))

    return freq,magnitude_dB

# Plot all four windows
plt.figure()
for name,window in windows.items():
    freq,W_dB = window_freq_response(window)
    plt.plot(freq,W_dB,label=name)
    plt.xlabel("normalized freq")
    plt.ylabel("magnitude dB")
    plt.title("Frequency Response of Window Functions")
    plt.grid()
    plt.legend()
    plt.show()

# Find the first null automatically
'''
use the zero crossings of the complex frequency response.
'''
def window_response(window,NFFT=65536):
    W = np.fft.fft(window,NFFT)
    W_shifted = np.fft.fftshift(W)
    magnitude = np.abs(W_shifted)
    magnitude = magnitude/np.max(magnitude)
    magnitude_dB = 20*np.log10(magnitude + 1e-15)
    freq = np.fft.fftshift(np.fft.fftfreq(NFFT))

    return freq,W_shifted,magnitude_dB

# Find the first null
def find_main_lobe(window,NFFT=65536):
    freq,W,magnitude_dB = window_response(window,NFFT)
    center = NFFT//2
    positive_mag = np.abs(W[center:])
    positive_freq = freq[center:]

    # ignote center peak
    positive_mag[0] = 1

    # find first minimum
    for i in range(1,len(positive_mag)-1):
        if(positive_mag[i] < positive_mag[i-1] and positive_mag[i] < positive_mag[i+1]):
            first_null = positive_freq[i]
            break
    main_lobe_width = 2*first_null

    return main_lobe_width

for name,window in windows.items():
    width = find_main_lobe(window)
    print(f"{name} Main-Lobe Width = {width}")

print()

# Automatically find the side-lobe level
'''
first find the first null and then ignore everything inside the main lobe.
'''

def find_side_lobe(window,NFFT=65536):
    freq,W,magnitude_dB = window_response(window,NFFT)
    center = NFFT//2
    positive_db = magnitude_dB[center:]

    # Find first null using minimum magnitude
    positive_mag = np.abs(W[center:])
    positive_mag[0] = 1
    first_null_index = None

    for i in range(1,len(positive_mag) - 1):
        if(positive_mag[i] < positive_mag[i-1] and positive_mag[i] < positive_mag[i+1]):
            first_null_index = i
            break

    # ignore main lobe
    side_lobes = positive_db[first_null_index + 1:]

    # largest side lobe
    side_lobe_level = np.max(side_lobes)

    return side_lobe_level

for name,window in windows.items():
    level = find_side_lobe(window)
    print(f"{name} Side-lobe-level = {level} dB")

