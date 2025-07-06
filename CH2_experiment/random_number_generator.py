import numpy as np
import matplotlib.pyplot as plt

def generator_exponential(Beta,n):
    U = np.random.uniform(0,1,size=n)
    X = -Beta * np.log(U)
    plt.hist(X, bins=20,alpha=0.6,density=True,label="Samples")
    x = np.linspace(0,20,10000)
    pdf = (1/Beta) * np.exp(-x/Beta)
    plt.plot(x,pdf,'r-',label='Exponential PDF')
    plt.legend()
    plt.grid(True)
    plt.show()

generator_exponential(2,1000)