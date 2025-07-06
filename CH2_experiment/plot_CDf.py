import numpy as np
import matplotlib.pyplot as plt

x_value = [1,2,3,4.8,5,6]
y_value = [0,0.1,0.2,0.2,1,1]

def draw():
    plt.plot(x_value,y_value)
    plt.xlabel("Value")
    plt.ylabel("CDF")
    plt.title("Problem 2 in chapter 2")
    plt.grid(True)
    plt.show()

draw()