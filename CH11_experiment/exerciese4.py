from math import *
import numpy as np
import pandas as pd
import scipy.stats as st
from matplotlib import pyplot as plt
np.set_printoptions(legacy='1.25')

n = 50
X1 = 30
X2 = 40

p1_hat = X1 / n
p2_hat = X2 / n

t_hat = p2_hat - p1_hat

se = np.sqrt(p1_hat * (1 - p1_hat) / n + p2_hat * (1 - p2_hat) / n)

z_01 = st.norm.ppf(0.95)

ci = (t_hat - z_01 * se, t_hat + z_01 * se)

print("Confidence Interval using delta method:", ci)

B = 10000

XX1 = np.random.binomial(n, p1_hat, size=B)
XX2 = np.random.binomial(n, p2_hat, size=B)

t_boot = XX2/n - XX1/n

ci_boot = (np.percentile(t_boot, 0.05), np.percentile(t_boot, 0.95))
print("Confidence Interval using bootstrap method:", ci_boot)


XXX1 = st.beta.rvs(X1 + 1, n - X1 + 1, size=B)
XXX2 = st.beta.rvs(X2 + 1, n - X2 + 1, size=B)

t_boot_beta = XXX2 - XXX1

ci_boot_beta = (np.percentile(t_boot_beta, 0.05), np.percentile(t_boot_beta, 0.95))
print("Confidence Interval using bootstrap method (beta):", ci_boot_beta)

ψ_hat = np.log((p1_hat * (1 - p1_hat) ) / ( p2_hat * (1 - p2_hat)))

se_ψ = 1 / np.sqrt((1 / (n * p1_hat * (1 - p1_hat))) + (1 / (n * p2_hat * (1 - p2_hat))) )

ci_ψ = (ψ_hat - z_01 * se_ψ, ψ_hat + z_01 * se_ψ)

print("Confidence Interval for ψ using delta method:", ci_ψ)


XXψ1 = st.beta.rvs(X1 + 1, n - X1 + 1, size=B)
XXψ2 = st.beta.rvs(X2 + 1, n - X2 + 1, size=B)


ψ_boot = np.log((XXψ1 * (1 - XXψ1) ) / ( XXψ2 * (1 - XXψ2)))

t_boot_ψ = ψ_boot.mean()

ci_boot_ψ = (np.percentile(t_boot_ψ, 0.05), np.percentile(t_boot_ψ, 0.95))

print("Confidence Interval using bootstrap method (beta):", ci_boot_ψ)
