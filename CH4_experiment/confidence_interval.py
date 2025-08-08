import numpy as np
import matplotlib.pyplot as plt
from math import log, ceil, sqrt

alpha = 0.05
p = 0.4
# choose n values spaced log-wise between 1 and 10000
n_values = np.unique(np.round(np.logspace(0, 4, 80)).astype(int))
trials = 1000  # Monte Carlo trials per n

# precompute epsilon_n (half-width) from Hoeffding
eps_n = lambda n: np.sqrt((1.0/(2*n)) * np.log(2.0/alpha))

coverages = []
lengths = 2 * eps_n(n_values)  # theoretical lengths (before truncation)

rng = np.random.default_rng(42)
for n in n_values:
    # simulate binomial counts directly (efficient)
    counts = rng.binomial(n, p, size=trials)
    means = counts / n
    eps = eps_n(n)
    lower = np.maximum(0, means - eps)
    upper = np.minimum(1, means + eps)
    contains = (lower <= p) & (p <= upper)
    coverages.append(contains.mean())

coverages = np.array(coverages)

# Plot coverage vs n
plt.figure(figsize=(9,5))
plt.plot(n_values, coverages, marker='o', linestyle='-', label='Empirical coverage (MC)')
plt.axhline(1-alpha, color='red', linestyle='--', label=f'Target coverage = {1-alpha:.2f}')
plt.xscale('log')
plt.xlabel('n (log scale)')
plt.ylabel('Coverage probability')
plt.title(f'Coverage of Hoeffding CI (alpha={alpha}, p={p}) — {trials} MC trials per n')
plt.grid(True, which='both', ls=':')
plt.legend()
plt.ylim(0.8,1.02)
plt.show()

# Plot length vs n (theoretical half-width doubled)
plt.figure(figsize=(9,4))
plt.plot(n_values, lengths, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n (log scale)')
plt.ylabel('Length of interval (theoretical, not truncated)')
plt.title('Length of Hoeffding CI (2*eps_n) vs n')
plt.grid(True, which='both', ls=':')
plt.show()

# Find n needed so that length <= 0.05
desired_length = 0.05
desired_half = desired_length / 2.0
# solve eps_n = sqrt((1/(2n)) ln(2/alpha)) <= desired_half
# => n >= (1/(2 * desired_half^2)) * ln(2/alpha)
n_needed = (1.0/(2 * desired_half**2)) * np.log(2.0/alpha)
n_needed = ceil(n_needed)
n_needed, desired_half, eps_n(n_needed)