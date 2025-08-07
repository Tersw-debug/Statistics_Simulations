import numpy as np
import matplotlib.pyplot as plt

n = 10000
num_simulations = 5
plt.figure(figsize=(10, 6))

def simulation(size, number_of_simulations):
    for i in range(number_of_simulations):
        s = np.random.choice([-1, 1], size=size)
        X_n = np.cumsum(s)
        plt.plot(range(1,1+size) ,X_n, label=f'Simulation {i+1}')
    plt.title("Simulated Stock price")
    plt.xlabel("Day (n)")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.show()
simulation(n,num_simulations)