# Plot tail probabilities and Markov/Mill bounds for standard normal
import numpy as np
import math
import matplotlib.pyplot as plt

# t values
t = np.linspace(0.01, 6, 400)

# Standard normal PDF and CDF using erf
def std_phi(x):
    return math.exp(-x*x/2)/math.sqrt(2*math.pi)

vec_phi = np.vectorize(std_phi)

def std_cdf(x):
    return 0.5*(1 + math.erf(x/np.sqrt(2)))

vec_cdf = np.vectorize(std_cdf)

# True two-sided tail
true_tail = 2*(1 - vec_cdf(t))

# Moments E|Z|^k for standard normal: E|Z|^k = 2^(k/2) * Gamma((k+1)/2) / sqrt(pi)
import scipy.special as sps

def moment_abs_standard_normal(k):
    return (2**(k/2)) * sps.gamma((k+1)/2) / math.sqrt(math.pi)

ks = [1,2,3,4,5]
markov_bounds = {}
for k in ks:
    m = moment_abs_standard_normal(k)
    markov_bounds[k] = m / (t**k)

# Mill's inequality (two-sided): P(|Z|>t) <= 2 * phi(t) / t
mills_bound = 2 * vec_phi(t) / t

# Plotting
plt.figure(figsize=(8,5))
plt.plot(t, true_tail, label='True $P(|Z|>t)$')
for k in ks:
    plt.plot(t, markov_bounds[k], label=f'Markov k={k}')
plt.plot(t, mills_bound, linestyle='--', label="Mill's bound $2\\phi(t)/t$")

plt.yscale('log')
plt.ylim(1e-7, 2)
plt.xlim(0,6)
plt.xlabel('t')
plt.ylabel('Tail probability (log scale)')
plt.title('Two-sided tail $P(|Z|>t)$ and Markov / Mill bounds')
plt.legend()
plt.grid(True, which='both', ls=':', lw=0.5)

plt.show()