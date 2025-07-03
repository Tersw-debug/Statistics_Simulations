import numpy as np
import matplotlib.pyplot as plt

def simulate_coin_flips(p,n):
    flips = np.random.binomial(1, p, size=n)
    cumlative_heads = np.cumsum(flips)
    proportion = cumlative_heads / np.arange(1, n + 1)


    plt.figure(figsize=(20,10))
    plt.plot(proportion, label=f"Simulated proportion (p={p})")
    plt.axhline(y=p, color='red', linestyle='--', label='True p')
    plt.title(f"Proportion of Heads as number of flips goes higher (p = {p})")
    plt.xlabel("Number of Flips")
    plt.ylabel("Proportion of Heads")
    plt.legend()
    plt.grid(True)
    plt.show()
    




p = 0.3 #Proportion of Heads
n = 100  # Number of times

simulate_coin_flips(p,n)

