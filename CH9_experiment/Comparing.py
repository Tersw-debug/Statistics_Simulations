from math import *
import numpy as np
import pandas as pd
import scipy.stats as st
from matplotlib import pyplot as plt


average_data = np.random.normal(loc=5, scale=1,size=100)

theta_hat = np.exp(average_data.mean())
# delta method
se_delta = np.exp(average_data.mean()) / 10

Ci = (theta_hat - 1.96 * se_delta, theta_hat + 1.96 * se_delta)

print("Delta method CI:", Ci)

# parameteric Bootstrap 
B = 10000
b = np.empty(B)
for i in range(B):
    theta_star = np.random.normal(average_data.mean(), scale=1, size=100).mean()
    b[i] = np.exp(theta_star)


se = b.std(ddof=1)

Ci_b = (theta_star - 1.96 * se, theta_star + 1.96 * se)

print("parametric Bootstrap CI:", Ci_b)

plt.hist(b, bins=30, alpha=0.5, label='Bootstrap')
plt.axvline(Ci[0], color='red', linestyle='--', label='95% CI')
plt.axvline(Ci[1], color='red', linestyle='--')
plt.legend()
plt.show()


# Non-parametric Bootstrap

b_non = np.empty(B)
for i in range(B):
    theta_star_non = np.mean(np.random.choice(average_data, size=100, replace=True))
    b_non[i] = np.exp(theta_star_non)

se_non = b_non.std(ddof=1)

Ci_non = (theta_star_non - 1.96 * se_non, theta_star_non + 1.96 * se_non)

print("Non-parametric Bootstrap CI:", Ci_non)

plt.hist(b_non, bins=30, alpha=0.5, label='Non-parametric Bootstrap')
plt.show()