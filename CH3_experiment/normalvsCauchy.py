import numpy as np
import matplotlib.pyplot as plt

def normal_vs_cauchy():
    mu, sigma = 0, 1
    s = np.random.normal(mu, sigma, 1000)
    Xi = np.mean(s)
    c = np.random.standard_cauchy(1000)
    print("Mean of normal distribution:", Xi)
    print("Mean of Cauchy distribution:", np.mean(c))


normal_vs_cauchy()