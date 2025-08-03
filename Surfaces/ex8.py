import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def graphingSurface(start_u, end_u, start_v, end_v):
    # Define parameter ranges
    u = np.linspace(start_u, end_u, 100)
    v = np.linspace(start_v, end_v, 100)
    # Create a grid of (u, v) values
    u, v = np.meshgrid(u, v)

    # Define the parametric equations
    x = np.sin(u) * np.cos(v)
    y = 2 * np.sin(u) * np.sin(v)
    z = 3 * np.cos(u)

    # Create the 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')  
    ax.set_zlabel('Z')

    plt.show()

graphingSurface(0, np.pi, 0,2 * np.pi)  # Example usage