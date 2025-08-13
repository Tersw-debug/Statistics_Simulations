import numpy as np

n = 10
a = 1
b = 3

t_hat = np.random.uniform(a, b, n).mean()

print(t_hat)