import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def f(x, y, z):
    return x ** 2 + y
    
def g(x, y, z):
    return x ** 2 + z + 5

def equation_system(x0, y0, z0, x1, h):
    x_points = []
    y_points = []
    z_points = []
    
    x = x0
    y = y0
    z = z0
    
    n = (int) ((x1 - x0) / h)
    
    for _ in range(n): 
        δy1 = f(x, y, z) * h
        δz1 = g(x, y, z) * h
        
        δy2 = f(x + h / 2, y + δy1 / 2, z + δz1 / 2) * h
        δz2 = g(x + h / 2, y + δy1 / 2, z + δz1 / 2) * h
        
        δy3 = f(x + h / 2, y + δy2 / 2, z + δz2 / 2) * h
        δz3 = g(x + h / 2, y + δy2 / 2, z + δz2 / 2) * h
        
        δy4 = f(x + h, y + δy3 / 2, z + δz3) * h
        δz4 = g(x + h, y + δy3 / 2, z + δz3) * h
        
        y += (δy1 / 6 + δy2 / 3 + δy3 / 3 + δy4 / 6)
        z += (δz1 / 6 + δz2 / 3 + δz3 / 3 + δz4 / 6)
        x += h
        
        x_points.append(x)
        y_points.append(y)
        z_points.append(z)  
        
    return (x_points, y_points, z_points)
            
# Plotting

points = equation_system(0, 0, 25, 10, 0.1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[0], points[1], points[2], c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

 # x**3/3 + x*y 
 # x*3*/4 + x*z +5*x
plt.show()