import numpy as np

p = 0.3
n_values = [10,100,1000]
trials = 10000

for n in n_values:
    flips = np.random.binomial(n=n,p=p,size=trials)
    average_heads = flips / trials
    expected_heads = n * p
    difference = average_heads - expected_heads
    print(f"n = {n}")
    print(f"Average Heads over {trials} trials: {average_heads}")
    print(f"Expected Heads {expected_heads}")
    print(f"Difference: {difference}")