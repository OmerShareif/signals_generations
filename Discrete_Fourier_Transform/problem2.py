'''
problem: DFT for Noise Cancellation

Removing unwanted frequencies from a signal
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

class DFTNoiseCancellar:
    def __init__(self,fs=1000,N=512):
        self.fs = fs
        self.N = N
        self.noise_freqs = [60,120,180] # noise and harmonics
        self.noise_bandwidth = 3 #Hz

    def generate_noisy_signal(self,duration=3):
        # Generate a signal with multiple freq components and noise
        t = np.arange(0,duration,1/self.fs)

        # clean signal
        clean = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*130*t) + 0.3*np.sin(2*np.pi*200*t)

        # noise
        noise = np.zeros_like(t)
        for f in self.noise_freqs:
            noise += 0.5*np.sin(2*np.pi*f*t + np.random.randn())

        # add random noise
        noise += 0.1*np.random.randn(len(t))

        noisy = clean + noise
        return t,clean,noise,noisy

    def remove_noise(self,signal):
        X = np.fft.fft(signal,self.N)
        freq = np.fft.fftfreq(self.N,1/self.fs)

        # create filter (remove noise)
        H = np.ones(self.N, dtype=complex)

        for noise_freq in self.noise_freqs:
            id = np.argmin(np.abs(freq - noise_freq)) # find bin indices for the freq
            bandwidth_bins = int(self.noise_bandwidth/(self.fs/self.N)) # zero the bins and neighbours (band stop)
            for i in range(-bandwidth_bins, bandwidth_bins+1):
                if 0 <= id+i < self.N:
                    H[id + i] = 0

            id_neg = np.argmin(np.abs(freq + noise_freq)) # remove symmetric negative freq
            for i in range(-bandwidth_bins, bandwidth_bins+1):
                if 0 <= id_neg + i < self.N:
                    H[id_neg + i] = 0

        X_filtered = X * H # apply filter

        filtered = np.fft.ifft(X_filtered, self.N)

        return freq,X,X_filtered,np.real(filtered)

    def process(self,signal_segment):
        if len(signal_segment) != self.N:
            signal_segment = signal_segment[:self.N]
            if len(signal_segment) < self.N:
                signal_segment = np.pad(signal_segment,(0,self.N - len(signal_segment)), 'constant')

        return self.remove_noise(signal_segment)


    def demo(self):
        t,clean,noise,noisy = self.generate_noisy_signal()

        # Process in chunks (simulating real-time)
        filtered_signal = np.zeros_like(noisy)
        for i in range(0,len(noisy)-self.N,self.N//2):
            chunk = noisy[i:i+self.N]
            freq,X,X_filtered,filtered = self.process(chunk)
            filtered_signal[i:i+self.N] += filtered

        # error
        error = clean - filtered_signal

        # original signals
        plt.figure()
        plt.plot(t[:500],clean[:500],'b-',label="clean")
        plt.plot(t[:500],noise[:500],'r-',label="noise")
        plt.title("signals")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.legend()
        plt.grid()

        # noisy signal
        plt.figure()
        plt.plot(t[:500], noisy[:500],'g-')
        plt.title("noisy signal")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.grid()

        # DFT of noisy signal
        plt.figure()
        plt.plot(freq[:len(freq)//2], np.abs(X[:len(freq)//2]),'b-')
        plt.title("DFT magnitude of noisy signal")
        plt.xlabel("freq")
        plt.ylabel("magnitude")
        plt.grid()

        # filtered signal vs clean
        plt.figure()
        plt.plot(t[:500], clean[:500],'b-',label="clean")
        plt.plot(t[:500],filtered_signal[:500],'g-',label="filtered")
        plt.title("noise cancellation result")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.legend()

        # error
        plt.figure()
        plt.plot(t[:500],error[:500],'r-')
        plt.title(f"error : {np.mean(error**2):.4f}")
        plt.xlabel("time")
        plt.ylabel("error")
        plt.grid()

        plt.show()




cancellar = DFTNoiseCancellar()
cancellar.demo()


        