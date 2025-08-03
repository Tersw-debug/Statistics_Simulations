import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
    
    # Define parameter ranges
u = np.linspace(-1, 1, 50)
v = np.linspace(0, 2*np.pi, 50)

# Create a grid of (u, v) values
u, v = np.meshgrid(u, v)

# Define the parametric equations
x = np.power(u, 3)
y = u * np.sin(v)
z = u * np.cos(v)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()