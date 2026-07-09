import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq


def AM_modulation():
    # Implement AM modulation and demodulation using the modulation property.
    fs = 2000
    T=0.5
    t = np.linspace(0,T,fs)
    N = len(t)

    # message signal
    f_message = 10
    message = np.sin(2*np.pi*f_message*t) * np.exp(-5*t)
    message = message/np.max(np.abs(message)) # normalize

    # carrier signal
    f_carrier = 200
    carrier = np.cos(2*np.pi*f_carrier*t)

    # modulation index
    m = 0.8

    # AM modulated signal
    modulated = (1 + m * message) * carrier

    plt.figure()
    plt.plot(t,message)
    plt.title("messagesignal")
    plt.xlabel("Time")
    plt.ylabel("amplitude")
    plt.grid()

    plt.figure()
    zoom_N = int(0.02*fs)
    plt.plot(t[:zoom_N],carrier[:zoom_N])
    plt.title("carrier signal")
    plt.xlabel("Time")
    plt.ylabel("amplitude")
    plt.grid()

    plt.figure()
    plt.plot(t,modulated)
    plt.title("AM modulated signal")
    plt.xlabel("Time")
    plt.ylabel("amplitude")
    plt.grid()

    X_message = fft(message)
    X_modulated = fft(modulated)
    freqs = fftfreq(N,1/fs)

    plt.figure()
    plt.plot(freqs,2*np.abs(X_message)/N)
    plt.title("magnitude spectrum signal")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.grid()

    plt.figure()
    plt.plot(freqs,2*np.abs(X_modulated)/N)
    plt.title("magnitude spectrum signal")
    plt.xlabel("freq")
    plt.ylabel("magnitude")
    plt.grid()


    plt.show()

AM_modulation()