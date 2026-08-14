'''
Matched filter: best way to detect a KNOWN pulse buried in noise

If you know the exact shape of a pulse you're looking for (e.g. a
radar chirp, or a known preamble in a data packet), the optimal
way to detect it in noise is a matched filter: correlate the
received signal against the known pulse shape. 

The output peaks exactly where the pulse occurs, even if the pulse is invisible to
the eye in the raw noisy signal.
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

pulse = signal.gausspulse(np.linspace(-1,1,60),fc=5)

noise_signal = 0.3*np.random.randn(400)
true_position = 150
received = noise_signal.copy()
received[true_position:true_position + len(pulse)] += pulse

# Matched filter = correlate with a time-reversed copy of the pulse.
matched_output = np.correlate(received, pulse, mode="full")

detected_position = np.argmax(matched_output) - (len(pulse)-1)

plt.figure()
plt.plot(received)
plt.title("received signal buried under noise, hard to view")
plt.grid()
plt.figure()
plt.plot(matched_output)
plt.title("matched filter output, clearly see the peak of pulse")
plt.grid()

plt.show()

