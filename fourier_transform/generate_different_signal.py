import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,fftfreq,ifft


def plot_time_freq(t,x,fs,title):
    X = fft(x)
    freq = fftfreq(len(x),1/fs)

    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,4))

    # time domain
    ax1.plot(t,x)
    ax1.set_title(f"{title} - time domain")
    ax1.set_xlabel("time")
    ax1.set_ylabel("amplitude")
    ax1.grid()

    # frequency domain
    ax2.plot(freq,2*np.abs(X)/len(x))
    ax2.set_title(f"{title} - frequency domain")
    ax2.set_xlabel("frequency")
    ax2.set_ylabel("magnitude")
    ax2.grid()

    plt.tight_layout()
    plt.show()

# sampling parameters
fs = 1000
t = np.arange(-5,5,1/fs)

# Exponential decay
a = 2
x_exp = np.exp(-a*t) * (t>=0)
plot_time_freq(t,x_exp,fs,"Expoential Decay")

# rectangular pulse
T=1
x_rect = np.where(np.abs(t) <= T/2,1,0)
plot_time_freq(t,x_rect,fs,"rectangular pulse")

# Sinc function
f0 = 2
x_sinc = np.sinc(2*f0*t)
plot_time_freq(t,x_sinc,fs,"Sinc funtion")

# cosine signal
f_cos = 5
x_cos = np.cos(2*np.pi*f_cos*t) * (np.abs(t) <= 2)
plot_time_freq(t,x_cos,fs,"cosine wave")


# ---- Inverse FT ----
def inverse_FT():
    t_recon = np.arange(-2,2,1/1000)
    x_original = np.sin(2*np.pi*3*t_recon) + 0.5*np.cos(2*np.pi*10*t_recon)
    # x_original *- np.exp(-0.5*abs(t_recon))

    # FFT 
    X = fft(x_original)

    # IFFT 
    x_reconstructed = ifft(X)

    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,4))

    ax1.plot(t_recon,x_original,label="original")
    ax1.plot(t_recon,x_reconstructed.real,'--',label="reconstructed")
    ax1.set_title("original vs reconstructed signal")
    ax1.set_xlabel("time")
    ax1.set_ylabel("amplitude")
    ax1.legend()
    ax1.grid()

    error = np.abs(x_original - x_reconstructed.real)
    ax2.plot(t_recon,error)
    ax2.set_title("reconstruction error")
    ax2.set_xlabel("time")
    ax2.set_ylabel("error magnitude")
    ax2.grid()

    plt.tight_layout()
    plt.show()


inverse_FT()