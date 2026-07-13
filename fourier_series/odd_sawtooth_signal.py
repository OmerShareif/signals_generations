'''
for T=1, signal x(t) = t for -0.5<t<0.5
'''

import numpy as np
import matplotlib.pyplot as plt

def compute_bn_numeric(n,T=1,num_samples=10000):
    t = np.linspace(-T/2,T/2,num_samples)
    dt = t[1] - t[0]

    x = t 

    w0 = 2*np.pi/T

    integrand = x * np.sin(n*w0*t)
    bn = (2/T)*np.trapezoid(integrand,t)
    return bn

num_harmonics = 30
bn_numeric_integrand = [compute_bn_numeric(n) for n in range(1,num_harmonics+1)]
print("first 5 bn coefficinets")
for n in range(5):
    print(f"b{n+1} = {bn_numeric_integrand[n]:.6f}")

#reconstrunction of signal
def fourier_sawtooth(t_vals,bn_vals,T,num_terms):
    w0 = 2*np.pi/T
    result = np.zeros_like(t_vals)
    for n in range(1,num_terms+1):
        if n <= len(bn_vals):
            result += bn_vals[n-1]*np.sin(n*w0*t_vals)
    return result

t_plot = np.linspace(-1.5,5,1000)
original = (t_plot + 0.5)%1 - 0.5

plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
for N in [5,15,30]:
    approx = fourier_sawtooth(t_plot,bn_numeric_integrand,1,N)
    plt.plot(t_plot,approx,label=f"N={N}")

plt.plot(t_plot,original,'k--',label="original")
plt.title("fourier series reconstrunction")
plt.grid()
plt.legend()
plt.xlabel("time")
plt.ylabel("amplitude")

plt.subplot(1,2,2)
plt.stem(range(1,16), bn_numeric_integrand[:15])
plt.title("bn_coefficeint")
plt.xlabel("harmonics")
plt.ylabel("bn value")
plt.grid()
plt.tight_layout()
plt.show()
