import numpy as np
from scipy.special import erfc

N = 1000 # number of bits

bits = np.random.randint(0,2,N)

# BPSK mapping
symbols = 2*bits-1 # 0 -> -1, 1 -> +1

# Add Gaussian Noise
EbN0_dB = 5
EbN0 = 10**(EbN0_dB/10)

sigma = np.sqrt(1/(2*EbN0))

noise = sigma * np.random.randn(N)

received = symbols + noise

# Detection (Receiver)
detected_bits = (received > 0).astype(int)

# Compute BER
error = np.sum(bits != detected_bits)
BER_sim = error/N

print("Simulated BER:",BER_sim)

# Theoretical BER (Q-function)
BER_theory = 0.5*erfc(np.sqrt(EbN0))
print("Theoritical BER:", BER_theory)
