# Signal and Systems with Python

A collection of Python programs, simulations, and notes for learning **Signals and Systems**.

The purpose of this repository is to understand the mathematical concepts behind signal processing by implementing them from scratch in Python rather than relying only on theory.

This repository is a personal learning project and will continue to grow as new topics are studied.

---

## Topics Covered

### Fourier Series

* Continuous-Time Fourier Series (CTFS)
* Fourier coefficients
* Reconstruction of periodic signals
* Square wave
* Triangle wave
* Sawtooth wave
* Gibbs phenomenon
* Effect of increasing harmonics
* Magnitude and phase spectrum

---

### Fourier Transform

* Continuous Fourier Transform
* Discrete Fourier Transform (DFT)
* Fast Fourier Transform (FFT)
* Frequency spectrum analysis
* Time-domain vs Frequency-domain
* Signal reconstruction
* Sampling theorem
* Aliasing
* Windowing techniques
* Spectrograms

### Probability & Random Processes

Module 1 – Probability Foundations
- Probability
- Joint probability
- Statistical independence

Module 2 – Random Variables
- Definition
- CDF
- PDF
- Relation between probability & density
- Joint distributions

Module 3 – Statistics of Random Variables
- Mean
- Variance
- Chebyshev’s inequality

Module 4 – Important Distributions
- Gaussian (Normal)
- Error function
- Rayleigh distribution
- Mean & variance of Gaussian and Rayleigh

---

## Repository Structure

```text
signal_and_system/
│
├── README.md
│
├── fourier_series/
│   ├── ...
│   └── examples
│
└── fourier_transform/
    ├── ...
    └── examples
```

---

## Requirements

* Python 3.11+
* NumPy
* Matplotlib
* SciPy (for selected examples)

Install dependencies:

```bash
pip install numpy matplotlib scipy
```

---

## Running Examples

Navigate to the desired folder and execute the Python program.

Example:

```bash
cd fourier_series
python square_wave.py
```

or

```bash
cd fourier_transform
python fft_example.py
```

---

## Learning Goals

* Understand signals in both the time and frequency domains.
* Visualize Fourier Series approximations.
* Learn how the Fourier Transform converts signals into their frequency components.
* Gain practical experience using NumPy and Matplotlib.
* Build intuition for digital signal processing concepts.

---

## Future Topics

* Laplace Transform
* Z-Transform
* Convolution
* Correlation
* Sampling Theorem
* Discrete-Time Signals
* Linear Time-Invariant (LTI) Systems
* Impulse Response
* Frequency Response
* Digital Filters
* FIR Filters
* IIR Filters
* FFT Applications
* Audio Signal Processing
* Image Frequency Analysis

---

## References

* Signals and Systems by Alan V. Oppenheim
* Signals and Systems by Simon Haykin
* Digital Signal Processing by Proakis
* MIT OpenCourseWare
* NumPy Documentation
* SciPy Documentation

---

## License

This repository is intended for educational and learning purposes.
