'''
FIR Filter Frequency Response
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def design_lowpass(N,fc,fs):
    # normalized cutoff freq
    Wn = fc/(fs/2)
    # hamming window
    b = signal.firwin(N,Wn,window='hamming',pass_zero='lowpass')
    return b

def design_highpass(N,fc,fs):
    Wn = fc/(fs/2)
    b = signal.firwin(N,Wn,window='hamming',pass_zero='highpass')
    return b

def design_bandpass(N,fc1,fc2,fs):
    Wn = [fc1 / (fs/2), fc2/(fs/2)]
    b = signal.firwin(N,Wn,window='hamming', pass_zero='bandpass')
    return b


fs = 1000
N=51

# design filters
b_lp = design_lowpass(N,200,fs)
b_hp = design_highpass(N,200,fs)
b_bp = design_bandpass(N,100,300,fs)

def compute(b,omega):
    H = np.zeros(len(omega), dtype=complex)
    n = np.arange(len(b))
    for i,w in enumerate(omega):
        H[i] = np.sum(b*np.exp(-1j*w*n))
    return H

omega = np.linspace(-np.pi,np.pi,2000)
freq = omega*fs/(2*np.pi)

H_lp = compute(b_lp, omega)
H_hp = compute(b_hp, omega)
H_bp = compute(b_bp, omega)


# lowpass filter
plt.figure()
plt.stem(np.arange(len(b_lp)), b_lp)
plt.title("Lowpass impulse response")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid()

plt.figure()
plt.plot(freq,20*np.log10(np.abs(H_lp) + 1e-10))
plt.title("Lowpass Magnitude response")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.figure()
plt.plot(freq,np.unwrap(np.angle(H_lp)))
plt.title("lowpass phase response")
plt.xlabel("freq")
plt.ylabel("phase")
plt.grid()

# highpass filter
plt.figure()
plt.stem(np.arange(len(b_hp)), b_hp)
plt.title("highpass impulse response")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid()

plt.figure()
plt.plot(freq,20*np.log10(np.abs(H_hp) + 1e-10))
plt.title("highpass Magnitude response")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.figure()
plt.plot(freq,np.unwrap(np.angle(H_hp)))
plt.title("highpass phase response")
plt.xlabel("freq")
plt.ylabel("phase")
plt.grid()

# bandpass filter
plt.figure()
plt.stem(np.arange(len(b_bp)), b_bp)
plt.title("bandpass impulse response")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid()

plt.figure()
plt.plot(freq,20*np.log10(np.abs(H_bp) + 1e-10))
plt.title("bandpass Magnitude response")
plt.xlabel("freq")
plt.ylabel("magnitude")
plt.grid()

plt.figure()
plt.plot(freq,np.unwrap(np.angle(H_bp)))
plt.title("bandpass phase response")
plt.xlabel("freq")
plt.ylabel("phase")
plt.grid()


plt.show()