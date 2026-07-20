import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm,bernoulli,binom

def random_variable():
    '''
    Demonstrate discrete and continuous random variables
    '''
    # Discrete Random Variable: Binomial
    n,p = 10,0.5
    x_discrete = np.arange(0,n+1)
    pmf_binom = stats.binom.pmf(x_discrete,n,p)
    cdf_binom = stats.binom.cdf(x_discrete,n,p)

    # Continuous Random Variable: Normal
    mu,sigma = 0,1
    x_continues = np.linspace(-4,4,1000)
    pdf_norm = stats.norm.pdf(x_continues,mu,sigma)
    cdf_norm = stats.norm.cdf(x_continues,mu,sigma)

    # Discreate PMF
    plt.figure()
    plt.stem(x_discrete,pmf_binom)
    plt.title(f"Binomial PMF (n={n}, p={p})")
    plt.xlabel("x")
    plt.ylabel("P(X=x)")
    plt.grid()

    # Discrete CDF
    plt.figure()
    plt.step(x_discrete,cdf_binom)
    plt.xlabel("x")
    plt.ylabel("F(x) = P(X<=x)")
    plt.grid()

    # continues PDF
    plt.figure()
    plt.plot(x_continues,pdf_norm)
    plt.title(f"Normal PDF")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()

    # continues CDF
    plt.figure()
    plt.plot(x_continues,cdf_norm)
    plt.title("Normal CDF")
    plt.ylabel("F(x) = P(X<=x)")
    plt.grid()

    plt.tight_layout()
    plt.show()

    return pmf_binom,cdf_binom,pdf_norm,cdf_norm

pmf_binom,cdf_binom,pdf_norm,cdf_norm = random_variable()
