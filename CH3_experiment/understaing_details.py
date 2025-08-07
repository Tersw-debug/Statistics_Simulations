# import numpy as np
# import matplotlib.pyplot as plt

# # let X1 to Xn be IID with mean μ and standart devation σ
# # let the δ = E(Xn) = summation of Xi / n Then δ is random variable
# # now to clarify the difference between Fx and δ because they are not the same
# # we will simulate the process of δ
# n = 1000  # number of samples
# mu = 0  # mean
# sigma = 1  # standard deviation
# X = np.random.uniform(mu, sigma, n)
# # first plot the distribution of X
# # plt.figure(figsize=(10, 6))
# # plt.hist(X, bins=30, density=True, alpha=0.6, color='r')
# # plt.title("Distribution of X")
# # plt.xlabel("Value")
# # plt.ylabel("Density")
# # plt.show()

# # now we will calculate the mean of X
# # and plot the distribution of δ

# for i in range(100):
#     delta = np.mean(X)
#     theta = np.var(X)
#     plt.scatter(delta, theta, color='blue', label='δ (Mean)' if i == 0 else "")

# plt.xlabel("Sample Number")
# plt.ylabel("δ (Mean)")
# plt.title("Simulation of δ (Mean) Over Samples")
# plt.legend()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Step 1: Plot the density of Uniform(0, 1)
x = np.linspace(-0.2, 1.2, 500)
fx = np.where((x >= 0) & (x <= 1), 1, 0)

plt.figure(figsize=(6, 3))
plt.plot(x, fx, label='f_X (Uniform[0,1])')
plt.title('PDF of Uniform(0,1)')
plt.xlabel('x')
plt.ylabel('Density')
plt.grid(True)
plt.legend()
plt.show()

# Step 2: Theoretical mean and variance of X̄_n
n_vals = np.arange(1, 101)
mean_vals = np.full_like(n_vals, 0.5)
var_vals = 1 / (12 * n_vals)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(n_vals, mean_vals)
plt.title('E[X̄ₙ] vs n')
plt.xlabel('n')
plt.ylabel('Mean')

plt.subplot(1, 2, 2)
plt.plot(n_vals, var_vals)
plt.title('Var(X̄ₙ) vs n')
plt.xlabel('n')
plt.ylabel('Variance')

plt.tight_layout()
plt.show()

# Step 3: Simulate sampling distribution of X̄ₙ for different n
sample_sizes = [1, 5, 25, 100]
num_samples = 10000

plt.figure(figsize=(12, 8))

for i, n in enumerate(sample_sizes, 1):
    samples = np.random.uniform(0, 1, size=(num_samples, n))
    xbar_n = samples.mean(axis=1)
    plt.subplot(2, 2, i)
    plt.hist(xbar_n, bins=50, density=True, alpha=0.7)
    plt.title(f'Sampling Distribution of X̄ₙ (n={n})')
    plt.xlabel('X̄ₙ')
    plt.ylabel('Density')
    sim_mean = xbar_n.mean()
    sim_var = xbar_n.var()
    plt.axvline(sim_mean, color='red', linestyle='--', label=f'Mean ≈ {sim_mean:.3f}\nVar ≈ {sim_var:.4f}')
    plt.legend()

plt.tight_layout()
plt.show()