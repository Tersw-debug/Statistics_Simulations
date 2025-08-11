import numpy as np
import scipy.stats as stats
cl = 0.95
for i in range(1000):
    obs_norm = np.random.normal(loc=0, scale=1, size=100)
    obs_cauchy = np.random.standard_cauchy(size=100)

    # Compute confidence intervals
    ci_norm = stats.t.interval(cl, len(obs_norm)-1, loc=np.mean(obs_norm), scale=stats.sem(obs_norm))
    ci_cauchy = stats.t.interval(cl, len(obs_cauchy)-1, loc=np.mean(obs_cauchy), scale=stats.sem(obs_cauchy))
    print(f"normal: {ci_norm}, cauchy: {ci_cauchy}")

