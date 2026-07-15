'''
given signal at T=2
one period x(t) =1 for |t|<0.5 and 0 otherwise

a. find trignometric fourier series coffiecint a0,an,bn
b. plot original signal and its approximation using N=5,15,30 harmonics
'''

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,cos,pi,integrate,summation,Piecewise,lambdify

t,n,T,w0 = symbols('t n T w0',real=True)

T_val = 2
w0_val = 2*np.pi/T_val

t_sym = symbols('t')
x_sym = Piecewise((1,(t_sym > -0.5) & (t_sym < 0.5)), (0,True))

a0 = (1/T_val) * integrate(x_sym, (t_sym,-T_val/2,T_val/2))
a0 = a0.evalf()

def compute_an(n_val):
    integrand =  x_sym * cos(2*np.pi*n_val*t_sym/T_val)
    an = (2/T_val) * integrate(integrand,(t_sym,-T_val/2,T_val/2))
    return an.evalf()

num_terms = 30
an_vals = [compute_an(i) for i in range(1,num_terms+1)]
bn_vals = [0] * num_terms

print(f"a0 = {a0}")
print(f"a1(first 5) : {an_vals[:5]}")
                               
def fourier_approx(t_vals,a0,an_vals,bn_vals,T,num_terms):
    w0 = 2*np.pi/T
    result = a0*np.ones_like(t_vals)
    for n in range(1,num_terms+1):
        result += an_vals[n-1]*np.cos(n*w0*t_vals)
        result += bn_vals[n-1]*np.sin(n*w0*t_vals)
    return result

t_plot = np.linspace(-2,2,1000)
original = np.where((t_plot % T_val) < 1,1,0)

fig,axs = plt.subplots(1,3,figsize=(15,4))
for i,N in enumerate([5,15,30]):
    approx = fourier_approx(t_plot,a0,an_vals,bn_vals,T_val,N)
    axs[i].plot(t_plot,approx,label=f"N={N}")
    axs[i].plot(t_plot,original,'r--',label="original")
    axs[i].set_title(f"N={N}")
    axs[i].grid()
    axs[i].legend()
plt.tight_layout()
plt.show()
