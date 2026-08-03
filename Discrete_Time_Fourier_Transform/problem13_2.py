'''
Windowing Effects
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window

fs = 1000
N=128
f = 50.5 # Frequency

t = np.arange(N)/fs
x = np.sin(2*np.pi*f*t)

# Different windows
window_names  = ['rectangular','hamming','hann','blackman']
windows = []

for name in window_names:
    if name == 'rectangular':
        w = np.ones(N)
    else:
        w = get_window(name,N)
    windows.append(w)

# compute DTFT and Apply windows
omega = np.linspace(-np.pi,np.pi,2000)
freq = omega * fs/(2*np.pi)

for i,(name,w) in enumerate(zip(window_names,windows)):
    x_windowed = x * w

    X = np.zeros(len(omega), dtype=complex)
    n = np.arange(N)
    for i,w_omega in enumerate(omega):
        X[i] = np.sum(x_windowed*np.exp(-1j*w_omega*n))

    magnitude = np.abs(X)
    magnitude_dB = 20*np.log10(magnitude/np.max(magnitude) + 1e-10)

    plt.figure()
    plt.plot(freq,magnitude,'b-')
    plt.title(f"{name.capitalize()} Window")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.grid()

    plt.axvline(f,color='red',label=f"freq = {f} Hz")
    plt.legend()

# time domain
for i,(name,w) in enumerate(zip(window_names,windows)):
    plt.figure()
    plt.plot(t,x,'b-',label="original")
    plt.plot(t,w,'r-',label="window")
    plt.plot(t,x*w,'g-',label="Windowed")
    plt.title(f"{name.capitalize()} window")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.legend()
    plt.grid()

plt.show()

for name,w in zip(window_names, windows):
    x_windowed = x*w
    X = np.zeros(len(omega), dtype=complex)
    n = np.arange(N)
    for i,w_omega in enumerate(omega):
        X[i] = np.sum(x_windowed*np.exp(-1j*w_omega*n))

    magnitude = np.abs(X)
    magnitude_db = 20*np.log10(magnitude/np.max(magnitude) + 1e-10)

    max_idx = np.argmax(magnitude)
    detected_freq = freq[max_idx]
    freq_error = abs(detected_freq - f)

    mainlobe = np.sum(magnitude_db > -3) * (freq[1] - freq[0])
    sidelobe = np.max(magnitude_db[100:])  # Rough estimate
    
    print(f"{name:^15} {mainlobe:^18.2f} {sidelobe:^18.1f} {freq_error:^15.2f}")

