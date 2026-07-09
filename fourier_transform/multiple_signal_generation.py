import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq,ifft

def define_fft():
    fs = 1000
    t = np.linspace(-3,3,fs)

    # create a complex signal
    x = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*12*t) + 0.3*np.sin(2*np.pi*25*t)
    x *= np.exp(-0.3*abs(t))

    #compute FT
    X = fft(x)
    freq = fftfreq(len(t),1/fs)
    
    #find dominant freq
    mag = np.abs(X)

    print("\nDominant frequencies")
    for f,m in zip(freq,mag):
        print(f"{f:.2f}Hz magnitude:{m:.2f}")


    #reconstuction of signal
    X_reconstructed = np.zeros_like(X)
    x_reconstructed = ifft(X_reconstructed)

    #  plot
    plt.figure()
    plt.plot(t,x)
    plt.title("original signal")
    plt.xlabel("time" )
    plt.grid()
    plt.figure()
    plt.stem(freq,2*mag/len(t))
    plt.title("frequency spectrum")
    plt.xlabel("freq")
    plt.grid()



    plt.tight_layout()
    plt.show()

define_fft()