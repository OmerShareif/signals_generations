'''
Butterworth Low-Pass Filter : Proper tunable filter with time and frequency domain analysis
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import butter,filtfilt


class ButterworthLowPass:
    def __init__(self,fs=1000,cutoff=50,order=4):
        self.fs = fs
        self.cutoff = cutoff
        self.order = order
        self.b, self.a = self.design_filter()


    def design_filter(self):
        # Design Butterworth LPF
        nyquist = self.fs / 2
        normalized_cutoff = self.cutoff / nyquist
        b,a = butter(self.order,normalized_cutoff,btype='low')
        return b,a

    def filter_signal(self,x):
        # apply filter to signal
        return filtfilt(self.b, self.a,x)

    def frequency_response(self):
        w,h = signal.freqz(self.b,self.a,worN=2000)
        return w,h

    def generate_test_signal(self,duration=2):
        # generate signal with multiple freq component
        t = np.arange(0,duration,1/self.fs)

        signal = np.sin(2*np.pi*10*t) + 0.7*np.sin(2*np.pi*30*t) + 0.5*np.sin(2*np.pi*100*t) + 0.3*np.sin(2*np.pi*200*t)

        return t,signal

    def analyze_filter(self):
        # generate test signal
        t,x = self.generate_test_signal()

        # apply filter
        y = self.filter_signal(x)

        # compute freq response
        w,h = self.frequency_response()
        freq = w * self.fs / (2 * np.pi)

        # time domain - original vs filtered
        plt.figure()
        plt.plot(t[:300], x[:300], 'b-', label="original")
        plt.plot(t[:300], y[:300], 'r-',label="filtered")
        plt.title(f"Time domain cutoff={self.cutoff}Hz, order={self.order}")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.legend()
        plt.grid()

        # freq response - magnitude
        plt.figure()
        plt.plot(freq, 20*np.log10(np.abs(h)),'b-')
        plt.title("magnitude response")
        plt.xlabel("freq")
        plt.ylabel("magntiude")
        plt.grid()

        # freq response - phase
        plt.figure()
        plt.plot(freq,np.unwrap(np.angle(h)), 'b-')
        plt.title("phase response")
        plt.xlabel("freq")
        plt.ylabel("phase")
        plt.grid()

        

        return t,x,y

for order in [2,4,8]:
    filt = ButterworthLowPass(cutoff=50,order=order)
    t,x,y = filt.analyze_filter()

    if order == 2:
        plt.figure()
        for order_val in [2,4,8]:
            filt_temp = ButterworthLowPass(cutoff=50, order=order_val)
            w,h = filt_temp.frequency_response()
            freq = w * filt_temp.fs/(2*np.pi)
            plt.plot(freq,20*np.log10(np.abs(h)), label=f"order{order_val}")

        plt.title("Butterworth filter comparison - Different order")
        plt.xlabel("freq")
        plt.ylabel("magnitude")
        plt.legend()
        plt.grid()
        plt.show()
        break


    