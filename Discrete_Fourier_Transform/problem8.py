'''
CHANNEL MODEL
Received = attenuation × transmitted + noise, then recovering transmitted bits
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

class CommunicationChannel:
    def __init__(self,fs=1000,bit_duration=0.1):
        self.fs = fs
        self.bit_duration = bit_duration
        self.samples_per_bit = int(fs * bit_duration)

    def generate_bits(self,num_bits):
        return np.random.randint(0,2,num_bits)

    def modulate_bits(self,bits):
        # convert bits to signal(BPSK)
        signal = np.array([])
        for bit in bits:
            # map 0 -> -1, 1 -> +1
            symbol = 1 if bit == 1 else -1
            symbol_signal = symbol * np.ones(self.samples_per_bit)
            signal = np.concatenate([signal, symbol_signal])
        return signal

    def add_channel_effects(self,signal,attenuation=0.7,snr_db=20):
        # apply channel effects : attenuation and AWGN
        # attenuation
        attenuated = attenuation * signal

        #add noise
        signal_power = np.mean(attenuated**2)
        noise_power = signal_power/(10**(snr_db/10))
        noise = np.sqrt(noise_power)*np.random.randn(len(attenuated))

        received = attenuated + noise
        return received,noise

    def demodulate_bits(self,received):
        bits = []
        for i in range(0,len(received), self.samples_per_bit):
            # average over bit duration
            symbol = np.mean(received[i:i+self.samples_per_bit])
            #decision : positive -> 1, negative -> 0
            bit = 1 if symbol > 0 else 0
            bits.append(bit)
        return np.array(bits)

    def low_pass_filter(self,received,cutoff_freq=100):
        # apply LPF
        nyquist = self.fs/2
        normalized_cutoff = cutoff_freq / nyquist
        b,a = signal.butter(4,normalized_cutoff,btype='low')
        return signal.filtfilt(b,a,received)

    def simulate_channel(self):
        # compute channel simulation
        # generate bits
        num_bits = 20
        bits = self.generate_bits(num_bits)

        # modulate
        trasmitted = self.modulate_bits(bits)
        t = np.arange(len(trasmitted))/self.fs

        # channel effects
        attenuation = 0.5
        snr_db = 10
        received, noise = self.add_channel_effects(trasmitted,attenuation,snr_db)


        #filter at receiver
        filtered = self.low_pass_filter(received)

        # demodulate
        recovered_bits = self.demodulate_bits(filtered)

        # 1. trasmitted signal
        plt.figure()
        plt.plot(t[:200],trasmitted[:200],'b-')
        plt.title("Trasnmitted bits")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.grid()

        # 2. received signal
        plt.figure()
        plt.plot(t[:200],received[:200],'r-',label="received")
        plt.plot(t[:200],trasmitted[:200],'b-',label="original")
        plt.title("received signal (attenuated + noise)")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.legend()
        plt.grid()        

        #3. filtered signal
        plt.figure()
        plt.plot(t[:200],filtered[:200],'g-',label="filtered")
        plt.plot(t[:200],trasmitted[:200],'b-',label="original")
        plt.title("filtered signal")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.legend()
        plt.grid()     

        #4. bit comparison
        plt.figure()
        plt.plot(bits,'bo-',markersize=8,label="orignal")
        plt.plot(recovered_bits,'rx-',markersize=8,label="receovered")
        plt.title("bit recovery")
        plt.xlabel("time")
        plt.ylabel("amplitude")
        plt.legend()
        plt.grid()     

        #5 . constellation diagram
        symbols = []
        for i in range(0,len(received), self.samples_per_bit):
            symbols.append(np.mean(received[i:i+self.samples_per_bit]))

        plt.figure()
        plt.scatter(np.arange(len(symbols)), symbols, s=50)
        plt.title("constellation diagram (received symbols)")
        plt.xlabel("symbol index")
        plt.ylabel("amplitude")
        plt.grid()

        errors = np.sum(bits != recovered_bits)
        ber = errors / num_bits

        plt.show()

        return bits,recovered_bits,ber

channel = CommunicationChannel()
bits,recovered, ber = channel.simulate_channel()

        
